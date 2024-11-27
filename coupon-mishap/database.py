import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('coupons.db', check_same_thread=False)
        # self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS coupons (
                code TEXT PRIMARY KEY,
                use_count INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

    def add_coupon(self, coupon):
        cursor = self.conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO coupons (code) VALUES (?)", (coupon,))
        self.conn.commit()

    def is_coupon_valid(self, coupon, app):
        cursor = self.conn.cursor()
        cursor.execute("SELECT use_count FROM coupons WHERE code = ?", (coupon,))
        result = cursor.fetchone()
        app.logger.info('im here', result[0])
        return result is not None and result[0] == 0

    def get_coupon_use_count(self, coupon, app):
        cursor = self.conn.cursor()
        cursor.execute("SELECT use_count FROM coupons WHERE code = ?", (coupon,))
        result = cursor.fetchone()
        app.logger.info('im here', result[0])
        return result[0] if result else 0

    def increment_coupon_use(self, coupon):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE coupons SET use_count = use_count + 1 WHERE code = ?", (coupon,))
        self.conn.commit()