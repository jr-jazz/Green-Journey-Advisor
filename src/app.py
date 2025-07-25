from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    """Connect to the SQLite database."""
    conn = sqlite3.connect('src/database/green_journey.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/options')
def options():
    """Display all travel options."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM travel_options')
    options = cursor.fetchall()
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
        cursor = conn.cursor()
        cursor.execute('INSERT INTO travel_options (destination, transport_mode, carbon_footprint) VALUES (?, ?, ?)',
                       (destination, transport_mode, carbon_footprint))
        conn.commit()
        conn.close()
        return redirect(url_for('options'))
    
    return render_template('add_option.html')

if __name__ == '__main__':
    app.run(debug=True)