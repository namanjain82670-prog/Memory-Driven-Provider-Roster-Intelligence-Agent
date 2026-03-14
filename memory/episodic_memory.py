import sqlite3
from datetime import datetime


class EpisodicMemory:

    def __init__(self):

        self.conn = sqlite3.connect("episodic_memory.db")

        self.create_table()

    def create_table(self):

        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
        time TEXT,
        query TEXT,
        result TEXT
        )
        """)

        self.conn.commit()

    def store(self, query, result):

        cursor = self.conn.cursor()

        cursor.execute(
            "INSERT INTO history VALUES (?, ?, ?)",
            (datetime.now().isoformat(), query, result)
        )

        self.conn.commit()

    def search(self, keyword):
        """
        Search past investigations
        """

        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT * FROM history WHERE query LIKE ?",
            ('%' + keyword + '%',)
        )

        results = cursor.fetchall()

        return results