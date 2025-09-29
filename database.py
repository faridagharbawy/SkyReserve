import sqlite3

DB_NAME = "flights.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS reservations(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, flight_number TEXT, departure TEXT,
            destination TEXT, date TEXT, seat_number TEXT
        )
    """)
    conn.commit()
    conn.close()

def create_reservation(data):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO reservations(name, flight_number, departure, destination, date, seat_number)
        VALUES(?,?,?,?,?,?)
    """, (data['name'], data['flight_number'], data['departure'], data['destination'], data['date'], data['seat_number']))
    conn.commit()
    conn.close()

def get_reservations():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM reservations")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_reservation(res_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM reservations WHERE id=?", (res_id,))
    row = cur.fetchone()
    conn.close()
    return row

def update_reservation(res_id, data):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        UPDATE reservations
        SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
        WHERE id=?
    """, (data['name'], data['flight_number'], data['departure'], data['destination'], data['date'], data['seat_number'], res_id))
    conn.commit()
    conn.close()

def delete_reservation(res_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM reservations WHERE id=?", (res_id,))
    conn.commit()
    conn.close()
