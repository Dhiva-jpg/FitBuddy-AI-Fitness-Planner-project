import sqlite3
from pathlib import Path

DB_PATH = Path("data/fitbuddy.db")

def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def initialize_database():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                height REAL,
                weight REAL,
                goal TEXT
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS plans (
                plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                generated_plan TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(user_id)
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS progress (
                progress_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                weight REAL,
                workout_completed INTEGER,
                recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

def save_user(name, age, height, weight, goal):
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO users (name, age, height, weight, goal) VALUES (?, ?, ?, ?, ?)",
            (name, age, height, weight, goal)
        )
        return cursor.lastrowid

def save_plan(user_id, plan):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO plans (user_id, generated_plan) VALUES (?, ?)",
            (user_id, plan)
        )

def save_progress(user_id, weight, completed):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO progress (user_id, weight, workout_completed) VALUES (?, ?, ?)",
            (user_id, weight, completed)
        )

def get_progress(user_id):
    with get_connection() as conn:
        return conn.execute(
            """SELECT weight, workout_completed, recorded_at
               FROM progress WHERE user_id = ? ORDER BY recorded_at""",
            (user_id,)
        ).fetchall()
