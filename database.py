import sqlite3
from student import Student

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


def add_student_db(student):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO students
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            student.student_id,
            student.name,
            student.phone_number,
            student.email,
            student.course,
            student.age,
            student.guardian_name,
            student.address,
        ),
    )

    connection.commit()
    connection.close()


def get_all_students_db():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    students = []

    for row in rows:
        student = Student(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
        )

        students.append(student)

    connection.close()

    return students


def find_student_db(student_id):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,),
    )

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return None

    student = Student(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4],
        row[5],
        row[6],
        row[7],
    )

    return student


def update_student_db(student):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE students
        SET name = ?,
            phone_number = ?,
            email = ?,
            course = ?,
            age = ?,
            guardian_name = ?,
            address = ?
        WHERE student_id = ?
        """,
        (
            student.name,
            student.phone_number,
            student.email,
            student.course,
            student.age,
            student.guardian_name,
            student.address,
            student.student_id,
        ),
    )

    connection.commit()
    connection.close()


connection.close()
