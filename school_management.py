import os

class Student:
    def __init__(self, student_id, name, grade, age):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.age = age

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}, Age: {self.age}")

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    grade = input("Enter Grade: ")
    age = input("Enter Age: ")
    
    student = Student(student_id, name, grade, age)
    with open("students.txt", "a") as f:
        f.write(f"{student_id},{name},{grade},{age}\n")
    print("Student added successfully!\n")

def view_students():
    if not os.path.exists("students.txt"):
        print("No student data found.\n")
        return
    with open("students.txt", "r") as f:
        print("\nStudent Records:")
        for line in f:
            student_id, name, grade, age = line.strip().split(",")
            student = Student(student_id, name, grade, age)
            student.display()
        print()

def search_student():
    search_id = input("Enter Student ID to search: ")
    found = False
    with open("students.txt", "r") as f:
        for line in f:
            student_id, name, grade, age = line.strip().split(",")
            if student_id == search_id:
                student = Student(student_id, name, grade, age)
                student.display()
                found = True
                break
    if not found:
        print("Student not found.\n")

def delete_student():
    delete_id = input("Enter Student ID to delete: ")
    lines = []
    found = False
    with open("students.txt", "r") as f:
        lines = f.readlines()
    with open("students.txt", "w") as f:
        for line in lines:
            student_id, *_ = line.strip().split(",")
            if student_id != delete_id:
                f.write(line)
            else:
                found = True
    if found:
        print("Student deleted successfully.\n")
    else:
        print("Student ID not found.\n")

def update_student():
    update_id = input("Enter Student ID to update: ")
    updated_lines = []
    found = False
    with open("students.txt", "r") as f:
        for line in f:
            student_id, name, grade, age = line.strip().split(",")
            if student_id == update_id:
                print("Enter new details:")
                name = input("New Name: ")
                grade = input("New Grade: ")
                age = input("New Age: ")
                updated_lines.append(f"{student_id},{name},{grade},{age}\n")
                found = True
            else:
                updated_lines.append(line)
    with open("students.txt", "w") as f:
        f.writelines(updated_lines)
    if found:
        print("Student updated successfully.\n")
    else:
        print("Student not found.\n")

# Menu
def menu():
    while True:
        print("===== School Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
menu()
