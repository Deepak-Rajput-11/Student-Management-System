import tkinter as tk  # Import Tkinter
from tkinter import messagebox, ttk
from database import (
    get_all_students_db,
    add_student_db,
    find_student_db,
    update_student_db,
    delete_student_db,
)

from student import Student
from validation import is_valid_phone, is_valid_email, is_valid_age, is_valid_name

root = tk.Tk()  # Create main window

root.title("Student Management System")  # Set window title
root.geometry("1000x600")

title_label = tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 24, "bold"),
)
title_label.pack(pady=20)
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

sidebar_frame = tk.Frame(main_frame, width=200, bg="lightgray")
sidebar_frame.pack(side="left", fill="y")

content_frame = tk.Frame(main_frame, bg="white")
content_frame.pack(side="right", fill="both", expand=True)


def add_student():
    student_id = id_entry.get().strip()
    name = name_entry.get().strip()
    phone_number = phone_entry.get().strip()
    email = email_entry.get().strip()
    course = course_entry.get().strip()
    age = age_entry.get().strip()
    guardian_name = guardian_entry.get().strip()
    address = address_entry.get().strip()

    if (
        student_id == ""
        or name == ""
        or phone_number == ""
        or email == ""
        or course == ""
        or age == ""
        or guardian_name == ""
        or address == ""
    ):
        messagebox.showerror("Error", "Please fill all fields.")
        return

    if not is_valid_name(name):
        messagebox.showerror("Error", "Name must contain only letters.")
        return

    if not is_valid_phone(phone_number):
        messagebox.showerror("Error", "Phone number must contain exactly 10 digits.")
        return

    if not is_valid_email(email):
        messagebox.showerror("Error", "Please enter a valid email address.")
        return

    if not is_valid_age(age):
        messagebox.showerror("Error", "Age must be a valid positive number.")
        return

    if not is_valid_name(guardian_name):
        messagebox.showerror("Error", "Guardian name must contain only letters.")
        return

    existing_student = find_student_db(student_id)

    if existing_student is not None:
        messagebox.showerror("Error", "Student ID already exists.")
        return

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

    add_student_db(student)

    messagebox.showinfo("Success", "Student added successfully!")

    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    guardian_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


def show_add_student():
    view_frame.pack_forget()
    search_frame.pack_forget()
    update_frame.pack_forget()
    delete_frame.pack_forget()
    form_frame.pack(pady=20)


def view_students():
    form_frame.pack_forget()
    search_frame.pack_forget()
    update_frame.pack_forget()
    delete_frame.pack_forget()
    view_frame.pack(fill="both", expand=True)

    for row in student_table.get_children():
        student_table.delete(row)

    students = get_all_students_db()

    for student in students:
        student_table.insert(
            "",
            "end",
            values=(
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


def show_search_student():
    form_frame.pack_forget()
    view_frame.pack_forget()
    update_frame.pack_forget()
    delete_frame.pack_forget()

    search_id_entry.delete(0, tk.END)
    search_details_frame.pack_forget()

    search_frame.pack(fill="both", expand=True)


def show_update_student():
    form_frame.pack_forget()
    view_frame.pack_forget()
    search_frame.pack_forget()
    delete_frame.pack_forget()

    update_id_entry.config(state="normal")
    update_id_entry.delete(0, tk.END)
    update_form_frame.pack_forget()

    update_frame.pack(fill="both", expand=True)


current_update_student_id = None


def show_delete_student():
    form_frame.pack_forget()
    view_frame.pack_forget()
    search_frame.pack_forget()
    update_frame.pack_forget()

    delete_id_entry.config(state="normal")
    delete_id_entry.delete(0, tk.END)
    delete_details_frame.pack_forget()
    delete_action_button.pack_forget()

    delete_frame.pack(fill="both", expand=True)


def find_update_student():
    global current_update_student_id

    update_form_frame.pack_forget()

    student_id = update_id_entry.get().strip()

    if student_id == "":
        messagebox.showerror("Error", "Please enter Student ID.")
        return

    student = find_student_db(student_id)

    if student is None:
        messagebox.showerror("Error", "Student not found.")
        return

    current_update_student_id = student_id
    update_id_entry.config(state="disabled")

    update_name_entry.delete(0, tk.END)
    update_name_entry.insert(0, student.name)

    update_phone_entry.delete(0, tk.END)
    update_phone_entry.insert(0, student.phone_number)

    update_email_entry.delete(0, tk.END)
    update_email_entry.insert(0, student.email)

    update_course_entry.delete(0, tk.END)
    update_course_entry.insert(0, student.course)

    update_age_entry.delete(0, tk.END)
    update_age_entry.insert(0, student.age)

    update_guardian_entry.delete(0, tk.END)
    update_guardian_entry.insert(0, student.guardian_name)

    update_address_entry.delete(0, tk.END)
    update_address_entry.insert(0, student.address)

    update_form_frame.pack(pady=10)


def find_delete_student():
    delete_details_frame.pack_forget()
    delete_action_button.pack_forget()

    student_id = delete_id_entry.get().strip()

    if student_id == "":
        messagebox.showerror("Error", "Please enter Student ID.")
        return

    student = find_student_db(student_id)

    if student is None:
        messagebox.showerror("Error", "Student not found.")
        return
    delete_id_entry.config(state="disabled")

    delete_student_id_value.config(text=student.student_id)
    delete_name_value.config(text=student.name)
    delete_phone_value.config(text=student.phone_number)
    delete_email_value.config(text=student.email)
    delete_course_value.config(text=student.course)
    delete_age_value.config(text=student.age)
    delete_guardian_value.config(text=student.guardian_name)
    delete_address_value.config(text=student.address)

    delete_details_frame.pack(pady=20)
    delete_action_button.pack(pady=10)


def delete_student():
    student_id = delete_id_entry.get().strip()

    confirm = messagebox.askyesno(
        "Confirm Delete", "Are you sure you want to delete this student?"
    )

    if confirm == False:
        return

    delete_student_db(student_id)

    messagebox.showinfo("Success", "Student deleted successfully!")

    delete_details_frame.pack_forget()
    delete_action_button.pack_forget()

    delete_id_entry.config(state="normal")
    delete_id_entry.delete(0, tk.END)


def update_student():
    student_id = current_update_student_id

    name = update_name_entry.get().strip()
    phone_number = update_phone_entry.get().strip()
    email = update_email_entry.get().strip()
    course = update_course_entry.get().strip()
    age = update_age_entry.get().strip()
    guardian_name = update_guardian_entry.get().strip()
    address = update_address_entry.get().strip()

    if (
        name == ""
        or phone_number == ""
        or email == ""
        or course == ""
        or age == ""
        or guardian_name == ""
        or address == ""
    ):
        messagebox.showerror("Error", "Please fill all fields.")
        return

    if not is_valid_name(name):
        messagebox.showerror("Error", "Name must contain only letters.")
        return

    if not is_valid_phone(phone_number):
        messagebox.showerror("Error", "Phone number must contain exactly 10 digits.")
        return

    if not is_valid_email(email):
        messagebox.showerror("Error", "Please enter a valid email address.")
        return

    if not is_valid_age(age):
        messagebox.showerror("Error", "Age must be a valid positive number.")
        return

    if not is_valid_name(guardian_name):
        messagebox.showerror("Error", "Guardian name must contain only letters.")
        return

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

    update_student_db(student)

    messagebox.showinfo("Success", "Student updated successfully!")

    update_form_frame.pack_forget()

    update_id_entry.config(state="normal")
    update_id_entry.delete(0, tk.END)


def search_student():

    search_details_frame.pack_forget()

    student_id = search_id_entry.get().strip()

    if student_id == "":
        messagebox.showerror("Error", "Please enter Student ID.")
        return

    student = find_student_db(student_id)

    if student is None:
        messagebox.showerror("Error", "Student not found.")
        return

    search_student_id_value.config(text=student.student_id)
    search_name_value.config(text=student.name)
    search_phone_value.config(text=student.phone_number)
    search_email_value.config(text=student.email)
    search_course_value.config(text=student.course)
    search_age_value.config(text=student.age)
    search_guardian_value.config(text=student.guardian_name)
    search_address_value.config(text=student.address)

    search_details_frame.pack(pady=20)


form_frame = tk.Frame(content_frame)
form_frame.pack(pady=20)

view_frame = tk.Frame(content_frame, bg="white")
search_frame = tk.Frame(content_frame, bg="white")
update_frame = tk.Frame(content_frame, bg="white")
delete_frame = tk.Frame(content_frame, bg="white")


delete_title = tk.Label(
    delete_frame,
    text="Delete Student",
    font=("Arial", 20, "bold"),
    bg="white",
)

delete_title.pack(pady=20)

delete_id_label = tk.Label(
    delete_frame,
    text="Student ID:",
    bg="white",
)

delete_id_label.pack(pady=5)

delete_id_entry = tk.Entry(delete_frame)
delete_id_entry.pack(pady=5)

find_delete_button = tk.Button(
    delete_frame,
    text="Find Student",
    command=find_delete_student,
)

find_delete_button.pack(pady=10)


delete_details_frame = tk.Frame(
    delete_frame,
    bg="white",
)

delete_student_id_label = tk.Label(
    delete_details_frame,
    text="Student ID:",
    bg="white",
    font=("Arial", 10, "bold"),
)
delete_student_id_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

delete_student_id_value = tk.Label(
    delete_details_frame,
    text="",
    bg="white",
)
delete_student_id_value.grid(row=0, column=1, sticky="w", padx=10, pady=5)

delete_name_label = tk.Label(
    delete_details_frame,
    text="Name:",
    bg="white",
    font=("Arial", 10, "bold"),
)
delete_name_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

delete_name_value = tk.Label(
    delete_details_frame,
    text="",
    bg="white",
)
delete_name_value.grid(row=1, column=1, sticky="w", padx=10, pady=5)

delete_phone_label = tk.Label(
    delete_details_frame,
    text="Phone Number:",
    bg="white",
    font=("Arial", 10, "bold"),
)
delete_phone_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

delete_phone_value = tk.Label(
    delete_details_frame,
    text="",
    bg="white",
)
delete_phone_value.grid(row=2, column=1, sticky="w", padx=10, pady=5)

delete_email_label = tk.Label(
    delete_details_frame,
    text="Email:",
    bg="white",
    font=("Arial", 10, "bold"),
)
delete_email_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

delete_email_value = tk.Label(
    delete_details_frame,
    text="",
    bg="white",
)
delete_email_value.grid(row=3, column=1, sticky="w", padx=10, pady=5)

# Course
delete_course_label = tk.Label(
    delete_details_frame,
    text="Course:",
    bg="white",
    font=("Arial", 10, "bold"),
)
delete_course_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)

delete_course_value = tk.Label(
    delete_details_frame,
    text="",
    bg="white",
)
delete_course_value.grid(row=4, column=1, sticky="w", padx=10, pady=5)


delete_age_label = tk.Label(
    delete_details_frame,
    text="Age:",
    bg="white",
    font=("Arial", 10, "bold"),
)
delete_age_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)

delete_age_value = tk.Label(
    delete_details_frame,
    text="",
    bg="white",
)
delete_age_value.grid(row=5, column=1, sticky="w", padx=10, pady=5)


delete_guardian_label = tk.Label(
    delete_details_frame,
    text="Guardian Name:",
    bg="white",
    font=("Arial", 10, "bold"),
)
delete_guardian_label.grid(row=6, column=0, sticky="w", padx=10, pady=5)

delete_guardian_value = tk.Label(
    delete_details_frame,
    text="",
    bg="white",
)
delete_guardian_value.grid(row=6, column=1, sticky="w", padx=10, pady=5)


delete_address_label = tk.Label(
    delete_details_frame,
    text="Address:",
    bg="white",
    font=("Arial", 10, "bold"),
)
delete_address_label.grid(row=7, column=0, sticky="w", padx=10, pady=5)

delete_address_value = tk.Label(
    delete_details_frame,
    text="",
    bg="white",
)
delete_address_value.grid(row=7, column=1, sticky="w", padx=10, pady=5)


delete_action_button = tk.Button(
    delete_frame,
    text="Delete Student",
    command=delete_student,
)


update_title = tk.Label(
    update_frame,
    text="Update Student",
    font=("Arial", 20, "bold"),
    bg="white",
)
update_title.pack(pady=20)

update_id_label = tk.Label(
    update_frame,
    text="Student ID:",
    bg="white",
)
update_id_label.pack(pady=5)

update_id_entry = tk.Entry(update_frame)
update_id_entry.pack(pady=5)

find_update_button = tk.Button(
    update_frame,
    text="Find Student",
    command=find_update_student,
)

find_update_button.pack(pady=10)

update_form_frame = tk.Frame(
    update_frame,
    bg="white",
)


update_name_label = tk.Label(
    update_form_frame,
    text="Name:",
    bg="white",
)
update_name_label.grid(row=0, column=0, padx=10, pady=5)

update_name_entry = tk.Entry(update_form_frame)
update_name_entry.grid(row=0, column=1, padx=10, pady=5)


update_phone_label = tk.Label(
    update_form_frame,
    text="Phone Number:",
    bg="white",
)
update_phone_label.grid(row=1, column=0, padx=10, pady=5)

update_phone_entry = tk.Entry(update_form_frame)
update_phone_entry.grid(row=1, column=1, padx=10, pady=5)

update_email_label = tk.Label(
    update_form_frame,
    text="Email:",
    bg="white",
)
update_email_label.grid(row=2, column=0, padx=10, pady=5)

update_email_entry = tk.Entry(update_form_frame)
update_email_entry.grid(row=2, column=1, padx=10, pady=5)


update_course_label = tk.Label(
    update_form_frame,
    text="Course:",
    bg="white",
)
update_course_label.grid(row=3, column=0, padx=10, pady=5)

update_course_entry = tk.Entry(update_form_frame)
update_course_entry.grid(row=3, column=1, padx=10, pady=5)


update_age_label = tk.Label(
    update_form_frame,
    text="Age:",
    bg="white",
)
update_age_label.grid(row=4, column=0, padx=10, pady=5)

update_age_entry = tk.Entry(update_form_frame)
update_age_entry.grid(row=4, column=1, padx=10, pady=5)


update_guardian_label = tk.Label(
    update_form_frame,
    text="Guardian Name:",
    bg="white",
)
update_guardian_label.grid(row=5, column=0, padx=10, pady=5)

update_guardian_entry = tk.Entry(update_form_frame)
update_guardian_entry.grid(row=5, column=1, padx=10, pady=5)


update_address_label = tk.Label(
    update_form_frame,
    text="Address:",
    bg="white",
)
update_address_label.grid(row=6, column=0, padx=10, pady=5)

update_address_entry = tk.Entry(update_form_frame)
update_address_entry.grid(row=6, column=1, padx=10, pady=5)

update_action_button = tk.Button(
    update_form_frame,
    text="Update Student",
    command=update_student,
)

update_action_button.grid(
    row=7,
    column=0,
    columnspan=2,
    pady=15,
)


search_title = tk.Label(
    search_frame,
    text="Search Student",
    font=("Arial", 20, "bold"),
    bg="white",
)

search_title.pack(pady=20)

search_id_label = tk.Label(
    search_frame,
    text="Student ID:",
    bg="white",
)

search_id_label.pack(pady=5)

search_id_entry = tk.Entry(search_frame)
search_id_entry.pack(pady=5)

search_action_button = tk.Button(
    search_frame,
    text="Search",
    command=search_student,
)

search_action_button.pack(pady=10)

search_details_frame = tk.Frame(
    search_frame,
    bg="white",
)

search_student_id_label = tk.Label(
    search_details_frame,
    text="Student ID:",
    bg="white",
    font=("Arial", 10, "bold"),
)
search_student_id_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

search_student_id_value = tk.Label(
    search_details_frame,
    text="",
    bg="white",
)
search_student_id_value.grid(row=0, column=1, sticky="w", padx=10, pady=5)


search_name_label = tk.Label(
    search_details_frame,
    text="Name:",
    bg="white",
    font=("Arial", 10, "bold"),
)
search_name_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

search_name_value = tk.Label(
    search_details_frame,
    text="",
    bg="white",
)
search_name_value.grid(row=1, column=1, sticky="w", padx=10, pady=5)


search_phone_label = tk.Label(
    search_details_frame,
    text="Phone Number:",
    bg="white",
    font=("Arial", 10, "bold"),
)
search_phone_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

search_phone_value = tk.Label(
    search_details_frame,
    text="",
    bg="white",
)
search_phone_value.grid(row=2, column=1, sticky="w", padx=10, pady=5)


search_email_label = tk.Label(
    search_details_frame,
    text="Email:",
    bg="white",
    font=("Arial", 10, "bold"),
)
search_email_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

search_email_value = tk.Label(
    search_details_frame,
    text="",
    bg="white",
)
search_email_value.grid(row=3, column=1, sticky="w", padx=10, pady=5)


search_course_label = tk.Label(
    search_details_frame,
    text="Course:",
    bg="white",
    font=("Arial", 10, "bold"),
)
search_course_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)

search_course_value = tk.Label(
    search_details_frame,
    text="",
    bg="white",
)
search_course_value.grid(row=4, column=1, sticky="w", padx=10, pady=5)


search_age_label = tk.Label(
    search_details_frame,
    text="Age:",
    bg="white",
    font=("Arial", 10, "bold"),
)
search_age_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)

search_age_value = tk.Label(
    search_details_frame,
    text="",
    bg="white",
)
search_age_value.grid(row=5, column=1, sticky="w", padx=10, pady=5)


search_guardian_label = tk.Label(
    search_details_frame,
    text="Guardian Name:",
    bg="white",
    font=("Arial", 10, "bold"),
)
search_guardian_label.grid(row=6, column=0, sticky="w", padx=10, pady=5)

search_guardian_value = tk.Label(
    search_details_frame,
    text="",
    bg="white",
)
search_guardian_value.grid(row=6, column=1, sticky="w", padx=10, pady=5)


search_address_label = tk.Label(
    search_details_frame,
    text="Address:",
    bg="white",
    font=("Arial", 10, "bold"),
)
search_address_label.grid(row=7, column=0, sticky="w", padx=10, pady=5)

search_address_value = tk.Label(
    search_details_frame,
    text="",
    bg="white",
)
search_address_value.grid(row=7, column=1, sticky="w", padx=10, pady=5)

view_title = tk.Label(
    view_frame,
    text="Student Records",
    font=("Arial", 20, "bold"),
    bg="white",
)

view_title.pack(pady=20)
table_frame = tk.Frame(view_frame)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

student_table = ttk.Treeview(
    table_frame,
    columns=("ID", "Name", "Phone", "Email", "Course", "Age", "Guardian", "Address"),
    show="headings",
)

student_table.heading("ID", text="Student ID")
student_table.heading("Name", text="Name")
student_table.heading("Phone", text="Phone Number")
student_table.heading("Email", text="Email")
student_table.heading("Course", text="Course")
student_table.heading("Age", text="Age")
student_table.heading("Guardian", text="Guardian Name")
student_table.heading("Address", text="Address")

student_table.column("ID", width=80)
student_table.column("Name", width=120)
student_table.column("Phone", width=120)
student_table.column("Email", width=160)
student_table.column("Course", width=100)
student_table.column("Age", width=60)
student_table.column("Guardian", width=130)
student_table.column("Address", width=180)

student_table.pack(side="top", fill="both", expand=True)

horizontal_scrollbar = ttk.Scrollbar(
    table_frame,
    orient="horizontal",
    command=student_table.xview,
)

horizontal_scrollbar.pack(side="bottom", fill="x")

student_table.configure(xscrollcommand=horizontal_scrollbar.set)


id_label = tk.Label(form_frame, text="Student ID:")
id_label.grid(row=0, column=0, padx=10, pady=5)

id_entry = tk.Entry(form_frame)
id_entry.grid(row=0, column=1, padx=10, pady=5)

name_label = tk.Label(form_frame, text="Name:")
name_label.grid(row=1, column=0, padx=10, pady=5)

name_entry = tk.Entry(form_frame)
name_entry.grid(row=1, column=1, padx=10, pady=5)

phone_label = tk.Label(form_frame, text="Phone Number:")
phone_label.grid(row=2, column=0, padx=10, pady=5)

phone_entry = tk.Entry(form_frame)
phone_entry.grid(row=2, column=1, padx=10, pady=5)

email_label = tk.Label(form_frame, text="Email:")
email_label.grid(row=3, column=0, padx=10, pady=5)

email_entry = tk.Entry(form_frame)
email_entry.grid(row=3, column=1, padx=10, pady=5)


course_label = tk.Label(form_frame, text="Course:")
course_label.grid(row=4, column=0, padx=10, pady=5)

course_entry = tk.Entry(form_frame)
course_entry.grid(row=4, column=1, padx=10, pady=5)


age_label = tk.Label(form_frame, text="Age:")
age_label.grid(row=5, column=0, padx=10, pady=5)

age_entry = tk.Entry(form_frame)
age_entry.grid(row=5, column=1, padx=10, pady=5)


guardian_label = tk.Label(form_frame, text="Guardian Name:")
guardian_label.grid(row=6, column=0, padx=10, pady=5)

guardian_entry = tk.Entry(form_frame)
guardian_entry.grid(row=6, column=1, padx=10, pady=5)


address_label = tk.Label(form_frame, text="Address:")
address_label.grid(row=7, column=0, padx=10, pady=5)

address_entry = tk.Entry(form_frame)
address_entry.grid(row=7, column=1, padx=10, pady=5)

save_button = tk.Button(
    form_frame,
    text="Save Student",
    command=add_student,
)

save_button.grid(row=8, column=0, columnspan=2, pady=15)

add_button = tk.Button(
    sidebar_frame,
    text="Add Student",
    command=show_add_student,
)

add_button.pack(pady=10)


view_button = tk.Button(
    sidebar_frame,
    text="View Students",
    command=view_students,
)

view_button.pack(pady=10)

search_button = tk.Button(
    sidebar_frame,
    text="Search Student",
    command=show_search_student,
)

search_button.pack(pady=10)

update_button = tk.Button(
    sidebar_frame,
    text="Update Student",
    command=show_update_student,
)
update_button.pack(pady=10)

delete_button = tk.Button(
    sidebar_frame,
    text="Delete Student",
    command=show_delete_student,
)

delete_button.pack(pady=10)

root.mainloop()
