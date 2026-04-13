import sqlite3

def init_db():
    conn = sqlite3.connect("motiva.db")
    cursor = conn.cursor()
    # Table for subscribers
    cursor.execute('''CREATE TABLE IF NOT EXISTS subscribers (user_id INTEGER PRIMARY KEY)''')
    # Table to track the last used quote index for variety
    cursor.execute('''CREATE TABLE IF NOT EXISTS state (key TEXT PRIMARY KEY, value INTEGER)''')
    cursor.execute("INSERT OR IGNORE INTO state (key, value) VALUES ('last_quote_index', -1)")
    conn.commit()
    conn.close()

def subscribe_user(user_id):
    conn = sqlite3.connect("motiva.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO subscribers (user_id) VALUES (?)", (user_id,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def unsubscribe_user(user_id):
    conn = sqlite3.connect("motiva.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subscribers WHERE user_id = ?", (user_id,))
    success = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return success

def get_all_subscribers():
    conn = sqlite3.connect("motiva.db")
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM subscribers")
    users = [row[0] for row in cursor.fetchall()]
    conn.close()
    return users

def get_last_index():
    conn = sqlite3.connect("motiva.db")
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM state WHERE key = 'last_quote_index'")
    idx = cursor.fetchone()[0]
    conn.close()
    return idx

def update_last_index(new_index):
    conn = sqlite3.connect("motiva.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE state SET value = ? WHERE key = 'last_quote_index'", (new_index,))
    conn.commit()
    conn.close()
