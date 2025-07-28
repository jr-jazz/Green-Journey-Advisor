from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    """Connect to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host='localhost',          # Update if using remote host
            user='your_username',      # Replace with MySQL username
            password='your_password',  # Replace with MySQL password
            database='green_journey'   # Replace with your database name
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/options')
def options():
    """Display all travel options."""
    conn = get_db_connection()
    if conn is None:
        return "Database connection failed", 500
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM travel_options')
    options = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('options.html', options=options)

@app.route('/add', methods=['GET', 'POST'])
def add_option():
    """Handle adding a new travel option."""
    if request.method == 'POST':
        destination = request.form['destination']
        transport_mode = request.form['transport_mode']
        carbon_footprint = float(request.form['carbon_footprint'])
        
        conn = get_db_connection()
        if conn is None:
            return "Database connection failed", 500
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO travel_options (destination, transport_mode, carbon_footprint) VALUES (%s, %s, %s)',
            (destination, transport_mode, carbon_footprint)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('options'))
    
    return render_template('add_option.html')

if __name__ == '__main__':
    app.run(debug=True)