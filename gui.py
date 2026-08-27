import tkinter as tk  # Import Tkinter
from tkinter import messagebox

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
    student_id = id_entry.get()
    name = name_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    course = course_entry.get()
    age = age_entry.get()
    guardian_name = guardian_entry.get()
    address = address_entry.get()

    if (
        student_id.strip() == ""
        or name.strip() == ""
        or phone_number.strip() == ""
        or email.strip() == ""
        or course.strip() == ""
        or age.strip() == ""
        or guardian_name.strip() == ""
        or address.strip() == ""
    ):
        messagebox.showerror("Error", "Please fill all fields.")
        return

    print(student_id)
    print(name)
    print(phone_number)
    print(email)
    print(course)
    print(age)
    print(guardian_name)
    print(address)

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
    form_frame.pack(pady=20)


def view_students():
    view_window = tk.Toplevel(root)

    view_window.title("View Students")
    view_window.geometry("700x400")

    view_title = tk.Label(
        view_window,
        text="Student Records",
        font=("Arial", 20, "bold"),
    )

    view_title.pack(pady=20)


form_frame = tk.Frame(content_frame)
form_frame.pack(pady=20)

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

root.mainloop()
