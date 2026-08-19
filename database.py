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

cursor.execute(
    """
    INSERT INTO students
    (student_id, name, phone_number, email, course, age, guardian_name, address)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""",
    ("S001", "Rahul", "9876543210", "rahul@gmail.com", "BCA", 20, "Rajesh", "Delhi"),
)

connection.commit()

print("Student inserted successfully!")

connection.close()
