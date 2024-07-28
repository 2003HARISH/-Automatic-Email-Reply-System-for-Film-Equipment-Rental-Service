import sqlite3

def setup_database():
    conn = sqlite3.connect('emaildb.db')
    cursor = conn.cursor()
    
    # Create equipment table
    cursor.execute('''CREATE TABLE IF NOT EXISTS equipment (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price REAL NOT NULL,
                        availability BOOLEAN NOT NULL
                      )''')
    
    # Create reviews table
    cursor.execute('''CREATE TABLE IF NOT EXISTS reviews (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT NOT NULL,
                        review TEXT NOT NULL,
                        rating INTEGER NOT NULL
                      )''')
    
    # Create assistance_requests table
    cursor.execute('''CREATE TABLE IF NOT EXISTS assistance_requests (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT NOT NULL,
                        issue TEXT NOT NULL
                      )''')
    
    # Insert sample data into equipment table
    cursor.executemany('''INSERT INTO equipment (name, price, availability)
                          VALUES (?, ?, ?)''', [
                          ('Camera A', 1200.00, True),
                          ('Camera B', 1500.00, False),
                          ('Lens X', 300.00, True),
                          ('Tripod Z', 100.00, True)])
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
