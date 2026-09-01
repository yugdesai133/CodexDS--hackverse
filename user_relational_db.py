
import sqlite3
import uuid
from typing import Dict, Any, Optional, List

class UserRelationalDB:
    def __init__(self, db_path: str = "users_relational.db"):
        self.db_path = db_path
        self._init_db()

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Enables dictionary-like row access
        return conn

    def _init_db(self):
        """Initializes the relational tables for users and their session logs."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    invested_amount REAL NOT NULL,
                    investment_goal TEXT NOT NULL CHECK(investment_goal IN ('SHORT_TERM', 'LONG_TERM')),
                    risk_tolerance TEXT NOT NULL CHECK(risk_tolerance IN ('CONSERVATIVE', 'MODERATE', 'AGGRESSIVE')),
                    market_experience TEXT NOT NULL CHECK(market_experience IN ('BEGINNER', 'INTERMEDIATE', 'ADVANCED')),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()

    def add_user(
        self,
        name: str,
        age: int,
        invested_amount: float,
        investment_goal: str,
        risk_tolerance: str,
        market_experience: str,
        user_id: Optional[str] = None
    ) -> str:
        """
        Takes raw backend/form inputs with explicit validation and saves the record.
        """
        # Validate and normalize parameters
        norm_goal = investment_goal.strip().upper()
        if norm_goal not in ["SHORT_TERM", "LONG_TERM"]:
            raise ValueError(f"Invalid investment_goal: '{investment_goal}'. Must be 'SHORT_TERM' or 'LONG_TERM'.")

        norm_risk = risk_tolerance.strip().upper()
        if norm_risk not in ["CONSERVATIVE", "MODERATE", "AGGRESSIVE"]:
            raise ValueError(f"Invalid risk_tolerance: '{risk_tolerance}'. Must be 'CONSERVATIVE', 'MODERATE', or 'AGGRESSIVE'.")

        norm_exp = market_experience.strip().upper()
        if norm_exp not in ["BEGINNER", "INTERMEDIATE", "ADVANCED"]:
            raise ValueError(f"Invalid market_experience: '{market_experience}'. Must be 'BEGINNER', 'INTERMEDIATE', or 'ADVANCED'.")

        if age <= 0:
            raise ValueError("Age must be a positive integer.")

        if invested_amount < 0:
            raise ValueError("Invested amount cannot be negative.")

        assigned_id = user_id if user_id else f"usr_{uuid.uuid4().hex[:8]}"

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (
                    user_id,
                    name,
                    age,
                    invested_amount,
                    investment_goal,
                    risk_tolerance,
                    market_experience
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                assigned_id,
                name.strip(),
                int(age),
                float(invested_amount),
                norm_goal,
                norm_risk,
                norm_exp
            ))
            conn.commit()

        return assigned_id

    def get_user_by_id(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Retrieves a single user's profile by ID."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            row = cursor.fetchone()
            if row:
                return dict(row)
            return None

    def list_all_users(self) -> List[Dict[str, Any]]:
        """Retrieves all registered user profiles."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users ORDER BY created_at DESC")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]


# =========================================================
# BACKEND INPUT DEMO / TEST
# =========================================================
if __name__ == "__main__":
    db = UserRelationalDB()

    print("--- Dynamic Backend User Creation ---")

    # Example 1: Ingesting a user from backend/API payloads (no defaults)
    user1_id = db.add_user(
        name="Rohit Sharma",
        age=24,
        invested_amount=75000.0,
        investment_goal="SHORT_TERM",
        risk_tolerance="AGGRESSIVE",
        market_experience="BEGINNER"
    )
    print(f"Created User: {user1_id}")

    # Example 2: Ingesting another profile
    user2_id = db.add_user(
        name="Ananya Iyer",
        age=34,
        invested_amount=500000.0,
        investment_goal="LONG_TERM",
        risk_tolerance="CONSERVATIVE",
        market_experience="ADVANCED"
    )
    print(f"Created User: {user2_id}")

    print("\n--- Fetching User 1 Profile ---")
    profile = db.get_user_by_id(user1_id)
    for key, value in profile.items():
        print(f"  {key}: {value}")

    print("\n--- All Registered Users ---")
    for u in db.list_all_users():
        print(f"ID: {u['user_id']} | Name: {u['name']} | Risk: {u['risk_tolerance']} | Goal: {u['investment_goal']}")