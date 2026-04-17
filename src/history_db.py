import sqlite3
from datetime import datetime

DB_NAME = "history.sqlite"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            summary TEXT,
            actions TEXT
        )
        """
    )

    conn.commit()
    conn.close()


def save_record(summary: str, actions: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history (timestamp, summary, actions) VALUES (?, ?, ?)",
        (datetime.utcnow().isoformat(), summary, actions),
    )

    conn.commit()
    conn.close()
