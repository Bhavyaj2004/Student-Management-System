import sqlite3
from tabulate import tabulate

# Database setup
def create_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            roll_no INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            grade TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Add student
def add_student():
    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    grade = input("Enter Grade: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (roll_no, name, course, grade))
    conn.commit()
    conn.close()
    print("Student added successfully!")

# View all students
def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()

    if not students:
        print("No records found!")
    else:
        headers = ["Roll No", "Name", "Course", "Grade"]
        print(tabulate(students, headers=headers, tablefmt="grid"))

# Update student
def update_student():
    roll_no = int(input("Enter Roll No to update: "))
    name = input("Enter New Name: ")
    course = input("Enter New Course: ")
    grade = input("Enter New Grade: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=?, course=?, grade=? WHERE roll_no=?", (name, course, grade, roll_no))
    conn.commit()
    conn.close()
    print("Student updated successfully!")

# Delete student
def delete_student():
    roll_no = int(input("Enter Roll No to delete: "))
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
    conn.commit()
    conn.close()
    print("Student deleted successfully!")

# Search student
def search_student():
    roll_no = int(input("Enter Roll No to search: "))
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,))
    student = cursor.fetchone()
    conn.close()

    if student:
        headers = ["Roll No", "Name", "Course", "Grade"]
        print(tabulate([student], headers=headers, tablefmt="grid"))
    else:
        print("Student not found!")

# Main menu
def main():
    create_table()
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            search_student()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()