import sqlite3
import json

def init():
    connection = sqlite3.connect("database.db")

    with open("schema.sql") as f:
        connection.executescript(f.read())

    connection.commit()
    connection.close()

def _get_db_connection():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection

def get_voucher(voucher_id):
    with _get_db_connection() as conn:
        voucher = conn.execute(f"""
            SELECT * FROM voucher
            WHERE voucher_id="{voucher_id}"
        """).fetchone()

        return {
            "created": voucher[1],
            "voucher_id": voucher[2],
            "person_id": voucher[3],
            "credits": voucher[4],
            "redeemed": voucher[5]
        }

def get_vouchers(person_id):
    with _get_db_connection() as conn: 
        vouchers = conn.execute(f"""
            SELECT * FROM voucher
            WHERE person_id="{person_id}"
        """).fetchall()
     
        response = []

        for voucher in vouchers:
            response.append({
                "created": voucher[1],
                "voucher_id": voucher[2],
                "person_id": voucher[3],
                "credits": voucher[4],
                "redeemed": voucher[5]
            })
       
        return response

def update_credits(voucher_id, count):
    with _get_db_connection() as conn:
        conn.execute(f"""
            UPDATE voucher
            SET credits = credits + {count}
            WHERE voucher_id=="{voucher_id}"
        """)

def create_voucher(voucher_id, credits):
    with _get_db_connection() as conn:
        conn.execute(f"""
            INSERT INTO voucher (voucher_id, credits, redeemed)
            VALUES (?, ?, ?)""", (voucher_id, credits, False)
        )

def redeem_voucher(voucher_id, person_id):
    with _get_db_connection() as conn:
        conn.execute(f"""
            UPDATE voucher
            SET redeemed=1, person_id="{person_id}"
            WHERE voucher_id="{voucher_id}"
        """)

