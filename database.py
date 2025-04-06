import sqlite3

def create_tables():
    conn = sqlite3.connect('candidates.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            match_score INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def store_candidate(candidate):
    conn = sqlite3.connect('candidates.db')
    c = conn.cursor()
    c.execute("INSERT INTO candidates (name, match_score) VALUES (?, ?)", 
              (candidate['name'], candidate['match_score']))
    conn.commit()
    conn.close()
