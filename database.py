import sqlite3

def get_connection():
    return sqlite3.connect('task.db')

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email UNIQUE NOT NULL
        )
    ''')

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dramas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,   
        title TEXT NOT NULL,                    
        description TEXT,                       
        watch_date TEXT,                          
        completed INTEGER DEFAULT 0,            
        user_id INTEGER,                        
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)
    conn.commit()
    conn.close()