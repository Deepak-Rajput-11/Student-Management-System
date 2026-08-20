import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id TEXT PRIMARY KEY,
        name TEXT,
        phone_number TEXT,
        email TEXT,
        course TEXT,
        age INTEGER,
        guardian_name TEXT,
        address TEXT
    )
""")

cursor.execute("SELECT * FROM students")

student = cursor.fetchone()
print(student)


connection.close()
