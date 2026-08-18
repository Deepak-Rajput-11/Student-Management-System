from student import Student


def get_valid_name(prompt):
    while True:
        name = input(prompt)

        if name.strip() == "":
            print("Name cannot be empty.")
        else:
            return name


def get_valid_phone(prompt):
    while True:
        phone_number = input(prompt)

        if phone_number.isdigit() and len(phone_number) == 10:
            return phone_number
        else:
            print("Invalid phone number. Please enter 10 digits.")


def get_valid_email(prompt):
    while True:
        email = input(prompt)

        if "@" not in email:
            print("Email must contain @.")
            continue

        if "." not in email:
            print("Email must contain .")
            continue

        if email.startswith("@") or email.endswith("@"):
            print("Invalid Email.")
            continue

        if email.startswith(".") or email.endswith("."):
            print("Invalid Email.")
            continue

        return email


def get_valid_age(prompt):
    while True:
        try:
            age = int(input(prompt))

            if 5 <= age <= 100:
                return age
            else:
                print("Age must be between 5 and 100.")

        except ValueError:
            print("Please enter a valid age.")


def get_valid_course(prompt):
    while True:
        course = input(prompt)

        if course.strip() == "":
            print("Course name cannot be empty.")
        else:
            return course


def get_valid_text(prompt):
    while True:
        value = input(prompt)

        if value.strip() == "":
            print("This field cannot be empty.")
        else:
            return value


def find_student(student_id):
    for student in students:
        if student.student_id == student_id:
            return student

    return None


def display_student(student):
    print(f"ID:            {student.student_id}")
    print(f"Name:          {student.name}")
    print(f"Phone_Number:  {student.phone_number}")
    print(f"Email ID:      {student.email}")
    print(f"Course:        {student.course}")
    print(f"Age:           {student.age}")
    print(f"Guardian_name: {student.guardian_name}")
    print(f"Address:       {student.address}")
    print()


def add_student():
    while True:
        student_id = input("Enter Student ID: ")

        if student_id.strip() == "":
            print("Student ID cannot be empty.")
            continue

        if find_student(student_id) is not None:
            print("Student ID already exists.")
            continue

        break

    name = get_valid_name("Enter name: ")

    phone_number = get_valid_phone("Enter Phone Number: ")
    email = get_valid_email("Enter Email: ")

    course = get_valid_course("Enter Course Name: ")

    age = get_valid_age("Enter age: ")

    guardian_name = get_valid_text("Enter Guardian Name: ")
    address = get_valid_text("Enter Address: ")

    student = Student(
        student_id,
        name,
        phone_number,
        email,
        course,
        age,
        guardian_name,
        address,
    )

    students.append(student)
    print("Student added successfully!")


def update_student():

    if students == []:
        print("No Students Found")
        return

    while True:
        update_id = input("Enter Student ID: ")

        student = find_student(update_id)

        if student is not None:
            break
        else:
            print("Student not found. Please enter a valid Student ID.")

    new_name = get_valid_name("Enter new name: ")
    student.name = new_name

    new_phone_no = get_valid_phone("Enter new phone number: ")
    student.phone_number = new_phone_no

    new_email = get_valid_email("Enter new email: ")
    student.email = new_email

    new_course = get_valid_course("Enter new course name: ")
    student.course = new_course

    new_age = get_valid_age("Enter new age: ")
    student.age = new_age

    new_guardian_name = get_valid_text("Enter new guardian name: ")
    student.guardian_name = new_guardian_name

    new_address = get_valid_text("Enter new address: ")
    student.address = new_address

    print("Student updated successfully!!!")


def delete_student():

    if students == []:
        print("No Students Found")
        return

    while True:
        delete_id = input("Enter Student ID: ")

        student = find_student(delete_id)

        if student is not None:
            break
        else:
            print("Student not found. Please enter a valid Student ID.")

    students.remove(student)
    print("Student deleted successfully!")


def view_students():
    if students == []:
        print("No Students Found")
        return

    for index, student in enumerate(students, start=1):
        print("============================")
        print(f"Student {index}")
        print("============================")
        display_student(student)


def search_student():

    if students == []:
        print("No Students Found")
        return

    while True:
        search_id = input("Enter Student ID: ")

        student = find_student(search_id)

        if student is not None:
            print("============================")
            print("Student Details")
            print("============================")
            display_student(student)
            break

        else:
            print("Student not found. Please enter a valid Student ID.")


students = []

running = True

while running:
    print("============================")
    print(" Student Management System  ")
    print("============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        print("Add Student Selector")
        add_student()

    elif choice == "2":
        print("View Student Selector")
        print()
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thanks for using Student Management System")
        running = False

    else:
        print("Invalid Choice")
