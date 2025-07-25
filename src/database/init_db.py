import sqlite3

def init_db():
    """Initialize the SQLite database and create the travel_options table."""
    conn = sqlite3.connect('green_journey.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS travel_options (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            destination TEXT NOT NULL,
            transport_mode TEXT NOT NULL,
            carbon_footprint REAL NOT NULL
        )
    ''')
    
    # Insert sample data
    cursor.execute('INSERT OR IGNORE INTO travel_options (destination, transport_mode, carbon_footprint) VALUES (?, ?, ?)',
                   ('Paris', 'Train', 0.05))
    cursor.execute('INSERT OR IGNORE INTO travel_options (destination, transport_mode, carbon_footprint) VALUES (?, ?, ?)',
                   ('London', 'Bicycle', 0.01))
    cursor.execute('INSERT OR IGNORE INTO travel_options (destination, transport_mode, carbon_footprint) VALUES (?, ?, ?)',
                   ('Amsterdam', 'Electric Car', 0.1))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()