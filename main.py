from student import Student


def get_valid_phone():
    while True:
        phone_number = input("Enter Phone Number: ")

        if phone_number.isdigit() and len(phone_number) == 10:
            return phone_number
        else:
            print("Invalid phone number. Please enter 10 digits.")


def get_valid_email():
    while True:
        email = input("Enter Email: ")

        if "@" in email and "." in email:
            return email
        else:
            print("Invalid Email.")


def find_student(student_id):
    for student in students:
        if student.student_id == student_id:
            return student

    return None


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

        while True:
            student_id = input("Enter Student ID: ")

            if student_id == "":
                print("Student ID cannot be empty.")
                continue

            duplicate = False

            for student in students:
                if student.student_id == student_id:
                    duplicate = True

            if duplicate == True:
                print("Student ID already exist.")
                continue
            break
        name = input("Enter name: ")

        phone_number = get_valid_phone()
        email = get_valid_email()

        course = input("Enter Course Name: ")

        while True:
            try:
                age = int(input("Enter age: "))
                break
            except ValueError:
                print("Please enter a valid age.")

        guardian_name = input("Enter Guardian Name: ")
        address = input("Enter Address: ")

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

    elif choice == "2":
        print("View Student Selector")
        print()

        if students == []:
            print("No Students Found")
        else:
            for index, student in enumerate(students, start=1):
                print("============================")
                print(f"Student {index}")
                print("============================")
                print(f"ID:            {student.student_id}")
                print(f"Name:          {student.name}")
                print(f"Phone_Number:  {student.phone_number}")
                print(f"Email ID:      {student.email}")
                print(f"Course:        {student.course}")
                print(f"Age:           {student.age}")
                print(f"Gaurdian_name: {student.gaurdian_name}")
                print(f"Address:       {student.address}")
                print()

    elif choice == "3":
        search_id = input("Enter Student ID: ")

        student = find_student(search_id)

        if student is not None:
            print(f"ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Course: {student.course}")
            print(f"Age: {student.age}")
            print()
        else:
            print("Student not found.")

    elif choice == "4":
        update_id = input("Enter Student ID: ")
        student = find_student(update_id)

        if student is not None:
            new_name = input("Enter new name: ")
            student.name = new_name

            new_phone_no = get_valid_phone()
            student.phone_number = new_phone_no

            new_email = get_valid_email()
            student.email = new_email

            new_course = input("Enter new course name: ")
            student.course = new_course

            while True:
                try:
                    new_age = int(input("Enter new age: "))
                    break
                except ValueError:
                    print("Please enter a valid age.")

            student.age = new_age

            new_gaurdian_name = input("Enter new gaurdian name: ")
            student.gaurdian_name = new_gaurdian_name

            new_address = input("Enter new address: ")
            student.address = new_address

            print("Student updated successfully!!!")

        else:
            print("Student not found")

    elif choice == "5":
        while True:
            delete_id = input("Enter Student ID: ")

            student = find_student(delete_id)

            if student is not None:
                students.remove(student)
                print("Student deleted successfully!")
                break

            else:
                print("Student not found. Please enter a valid Student ID.")

    elif choice == "6":
        print("Thanks for using Student Management System")
        running = False

    else:
        print("Invalid Choice")
