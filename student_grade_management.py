
import json
import os

FILE_NAME = "students.json"


# Load student data from file
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


# Save student data to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Calculate total, percentage, and grade
def calculate_grade(marks):
    total = sum(marks.values())
    percentage = total / len(marks) if marks else 0

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade


# Add a student
def add_student(students):
    student_id = input("Enter Student ID: ").strip()

    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    marks = {}

    number_of_subjects = int(input("Enter number of subjects: "))

    if number_of_subjects <= 0:
        print("Number of subjects must be greater than zero.")
        return

    for i in range(number_of_subjects):
        subject = input(f"Enter subject {i + 1} name: ").strip()

        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= mark <= 100:
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

        marks[subject] = mark

    students[student_id] = {
        "name": name,
        "marks": marks
    }

    save_students(students)
    print("Student added successfully!")


# Display one student's details
def display_student(student_id, student):
    total, percentage, grade = calculate_grade(student["marks"])

    print("\n---------- Student Details ----------")
    print("Student ID :", student_id)
    print("Name       :", student["name"])

    print("Marks:")
    for subject, mark in student["marks"].items():
        print(f"  {subject}: {mark}")

    print("Total      :", total)
    print("Percentage :", round(percentage, 2), "%")
    print("Grade      :", grade)
    print("----------------------------------")


# View all students
def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n======= Student Records =======")

    for student_id, student in students.items():
        display_student(student_id, student)


# Search student
def search_student(students):
    student_id = input("Enter Student ID to search: ").strip()

    if student_id in students:
        display_student(student_id, students[student_id])
    else:
        print("Student not found!")


# Update student marks
def update_student(students):
    student_id = input("Enter Student ID to update: ").strip()

    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]

    print("Student Name:", student["name"])
    print("Current Marks:", student["marks"])

    subject = input("Enter subject to update: ").strip()

    if subject not in student["marks"]:
        print("Subject not found!")
        return

    while True:
        try:
            new_mark = float(input("Enter new marks (0-100): "))
            if 0 <= new_mark <= 100:
                break
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    student["marks"][subject] = new_mark

    save_students(students)
    print("Marks updated successfully!")


# Delete student
def delete_student(students):
    student_id = input("Enter Student ID to delete: ").strip()

    if student_id in students:
        del students[student_id]
        save_students(students)
        print("Student record deleted successfully!")
    else:
        print("Student not found!")


# Main menu
def main():
    students = load_students()

    while True:
        print("\n===== Student Grade Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("Thank you for using Student Grade Management System!")
            break

        else:
            print("Invalid choice! Please select 1-6.")


# Start the program
if __name__ == "__main__":
    main()
