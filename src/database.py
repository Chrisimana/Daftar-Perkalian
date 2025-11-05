import sqlite3
import datetime
import json

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('history_perkalian.db', check_same_thread=False)
        self.create_table()
    
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS history_perkalian (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bilangan INTEGER NOT NULL,
            hasil TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
        try:
            self.conn.execute(query)
            self.conn.commit()
        except Exception as e:
            print(f"Error creating table: {e}")
    
    def simpan_history(self, bilangan, hasil_perkalian):
        """Menyimpan hasil perkalian ke database"""
        try:
            query = "INSERT INTO history_perkalian (bilangan, hasil) VALUES (?, ?)"
            self.conn.execute(query, (bilangan, json.dumps(hasil_perkalian)))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error saving history: {e}")
            return False
    
    def ambil_history(self, limit=10):
        """Mengambil history perkalian"""
        try:
            query = "SELECT * FROM history_perkalian ORDER BY timestamp DESC LIMIT ?"
            cursor = self.conn.execute(query, (limit,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching history: {e}")
            return []
    
    def hapus_history(self):
        """Menghapus semua history"""
        try:
            self.conn.execute("DELETE FROM history_perkalian")
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error clearing history: {e}")
            return False
    
    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()