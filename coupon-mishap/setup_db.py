import sqlite3

def setup_database():
    conn = sqlite3.connect('coupons.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS coupons (
        code TEXT PRIMARY KEY,
        use_count INTEGER DEFAULT 0
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()