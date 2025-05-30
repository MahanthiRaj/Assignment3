import sqlite3

school = {
    1: {"roll_no": 1, "name": "Alice", "address": "NY", "section": "A"},
    2: {"roll_no": 2, "name": "Bob", "address": "LA", "section": "B"},
    
}

with sqlite3.connect("school.db", timeout=30) as conn:
    cursor = conn.cursor()
    for value in school.values():
        cursor.execute('''
            INSERT INTO students (roll_no, name, address, section)
            VALUES (:roll_no, :name, :address, :section)
        ''', value)
    conn.commit()
