from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash
from flask_bcrypt import Bcrypt
import mysql.connector
from mysql.connector import Error
import logging
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session
bcrypt = Bcrypt(app)

logging.basicConfig(filename='email.log', level=logging.INFO)

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='green_journey'
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def login_required(f):
    def wrap(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__
    return wrap

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        if conn is None:
            flash('Database connection failed', 'error')
            return redirect(url_for('register'))
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM users WHERE email = %s OR username = %s", (email, username))
            if cursor.fetchone():
                flash('Email or username already exists.', 'error')
                cursor.close()
                conn.close()
                return redirect(url_for('register'))
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                (username, email, hashed_password)
            )
            conn.commit()
            cursor.close()
            conn.close()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Error as e:
            print(f"Database error: {e}")
            flash('Registration failed. Please try again.', 'error')
            return redirect(url_for('register'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        if conn is None:
            flash('Database connection failed', 'error')
            return redirect(url_for('login'))
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, password FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
            cursor.close()
            conn.close()
            if user and bcrypt.check_password_hash(user[1], password):
                session['user_id'] = user[0]
                flash('Login successful!', 'success')
                return redirect(url_for('index'))
            flash('Invalid email or password.', 'error')
            return redirect(url_for('login'))
        except Error as e:
            print(f"Database error: {e}")
            flash('Login failed. Please try again.', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/get_price', methods=['POST'])
def get_price():
    start_point = request.form.get('start_point')
    end_point = request.form.get('end_point')
    if not start_point or not end_point or start_point == end_point:
        return jsonify({'error': 'Invalid start or end point'}), 400
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Database connection failed'}), 500
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT price FROM travel_options WHERE start_point = %s AND end_point = %s LIMIT 1",
            (start_point, end_point)
        )
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return jsonify({'price': float(result[0])})
        return jsonify({'error': 'No price found for this route'}), 404
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({'error': 'Database query failed'}), 500

@app.route('/select_route', methods=['POST'])
def select_route():
    start_point = request.form['start_point']
    end_point = request.form['end_point']
    inbound_date = request.form.get('inbound_date', '')
    outbound_date = request.form.get('outbound_date', '')
    adults = int(request.form.get('adults', '1'))
    children = int(request.form.get('children', '0'))
    session['adults'] = adults
    session['children'] = children
    if start_point == end_point:
        return render_template('index.html', error="Start and end points cannot be the same.")
    conn = get_db_connection()
    if conn is None:
        return "Database connection failed", 500
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, start_point, end_point, transport_mode, carbon_footprint, price FROM travel_options WHERE start_point = %s AND end_point = %s",
            (start_point, end_point)
        )
        options = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('options.html', options=options, start_point=start_point, end_point=end_point, inbound_date=inbound_date, outbound_date=outbound_date, adults=adults, children=children)
    except Error as e:
        print(f"Database error: {e}")
        return "Database query failed", 500

@app.route('/pricing/<int:option_id>')
@login_required
def pricing(option_id):
    adults = session.get('adults', 1)
    children = session.get('children', 0)
    conn = get_db_connection()
    if conn is None:
        return "Database connection failed", 500
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, start_point, end_point, transport_mode, carbon_footprint, price FROM travel_options WHERE id = %s",
            (option_id,)
        )
        option = cursor.fetchone()
        cursor.close()
        conn.close()
        if option:
            total_price = float(option[5]) * adults + float(option[5]) * 0.5 * children
            return render_template('pricing.html', option={
                'id': option[0],
                'start_point': option[1],
                'end_point': option[2],
                'transport_mode': option[3],
                'carbon_footprint': option[4],
                'price': total_price
            }, adults=adults, children=children)
        return "Option not found", 404
    except Error as e:
        print(f"Database error: {e}")
        return "Database query failed", 500

@app.route('/payment/<int:option_id>')
@login_required
def payment(option_id):
    adults = session.get('adults', 1)
    children = session.get('children', 0)
    conn = get_db_connection()
    if conn is None:
        return "Database connection failed", 500
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, start_point, end_point, transport_mode, carbon_footprint, price FROM travel_options WHERE id = %s",
            (option_id,)
        )
        option = cursor.fetchone()
        cursor.close()
        conn.close()
        if option:
            total_price = float(option[5]) * adults + float(option[5]) * 0.5 * children
            return render_template('payment.html', option={
                'id': option[0],
                'start_point': option[1],
                'end_point': option[2],
                'transport_mode': option[3],
                'carbon_footprint': option[4],
                'price': total_price
            }, adults=adults, children=children)
        return "Option not found", 404
    except Error as e:
        print(f"Database error: {e}")
        return "Database query failed", 500

@app.route('/process_payment', methods=['POST'])
@login_required
def process_payment():
    option_id = request.form['option_id']
    payment_method = request.form['payment_method']
    email = request.form['email']
    card_number = request.form.get('card_number', '')
    expiry = request.form.get('expiry', '')
    cvv = request.form.get('cvv', '')
    paypal_id = request.form.get('paypal_id', '')
    adults = session.get('adults', 1)
    children = session.get('children', 0)
    conn = get_db_connection()
    if conn is None:
        return "Database connection failed", 500
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, start_point, end_point, transport_mode, carbon_footprint, price FROM travel_options WHERE id = %s",
            (option_id,)
        )
        option = cursor.fetchone()
        cursor.close()
        conn.close()
        if option:
            total_price = float(option[5]) * adults + float(option[5]) * 0.5 * children
            try:
                msg = MIMEText(
                    f"Payment Confirmation\n\n"
                    f"Route: {option[1]} to {option[2]}\n"
                    f"Transport Mode: {option[3]}\n"
                    f"Carbon Footprint: {option[4]} kg CO2\n"
                    f"Price: £{total_price:.2f}\n"
                    f"Travelers: {adults} Adult(s), {children} Child(ren)\n"
                    f"Payment Method: {payment_method}\n"
                    f"Email: {email}\n"
                    f"Thank you for choosing Green Journey Advisor!"
                )
                msg['Subject'] = 'Green Journey Advisor - Payment Confirmation'
                msg['From'] = 'no-reply@greenjourneyadvisor.com'
                msg['To'] = email
                logging.info(f"Mock email sent to {email}: {msg.as_string()}")
                return render_template('confirmation.html', option={
                    'id': option[0],
                    'start_point': option[1],
                    'end_point': option[2],
                    'transport_mode': option[3],
                    'carbon_footprint': option[4],
                    'price': total_price
                }, payment_method=payment_method, email=email, adults=adults, children=children)
            except Exception as e:
                logging.error(f"Mock email error: {e}")
                return "Failed to process confirmation", 500
        return "Option not found", 404
    except Error as e:
        print(f"Database error: {e}")
        return "Database query failed", 500

if __name__ == '__main__':
    app.run(debug=True)