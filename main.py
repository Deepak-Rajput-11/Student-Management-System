from student import Student

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
        student_id = input("Enter Student ID: ")

        duplicate = False

        for student in students:
            if student.student_id == student_id:
                duplicate = True

        if duplicate == False:

            name = input("Enter name: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
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

        else:
            print("Student ID already exist!")

    elif choice == "2":
        print("View Student Selector")
        print()

        if students == []:
            print("No Students Found")
        else:
            for student in students:
                print(f"ID: {student.student_id}")
                print(f"Name: {student.name}")
                print(f"Course: {student.course}")
                print(f"Age: {student.age}")
                print()

    elif choice == "3":
        search_id = input("Enter Student ID: ")
        found = False

        for student in students:
            if student.student_id == search_id:
                found = True
                print(f"ID: {student.student_id}")
                print(f"Name: {student.name}")
                print(f"Course: {student.course}")
                print(f"Age: {student.age}")
                print()
                break

        if found == False:
            print("Student not found.")

    elif choice == "4":
        update_id = input("Enter Student ID: ")
        found = False

        for student in students:
            if student.student_id == update_id:
                found = True

                new_name = input("Enter new name: ")
                student.name = new_name

                new_phone_no = input("Enter new phone number: ")
                student.phone_number = new_phone_no

                new_email = input("Enter new email ID: ")
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
                break

        if found == False:
            print("Student not found")

    elif choice == "5":
        delete_id = input("Enter Student ID: ")
        found = False

        for i in range(len(students)):
            if students[i].student_id == delete_id:
                found = True
                students.pop(i)
                print("Student deleted successfully!")
                break

        if found == False:
            print("Student not found.")

    elif choice == "6":
        print("Thanks for using Student Management System")
        running = False

    else:
        print("Invalid Choice")
