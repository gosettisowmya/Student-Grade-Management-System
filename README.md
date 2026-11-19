                                                   🎓 Student Grade Management System
A simple Student Grade Management System built using Python to
manage student records, subject marks, and academic performance. The
application supports adding, viewing, searching, updating, and deleting
student records, while automatically calculating totals, percentages,
and grades. Student information is stored locally using JSON file
storage.
📌 Project Overview
Managing student marks manually can be time-consuming and error-prone.
This project provides a menu-driven Python application that helps
organize student information and automate basic grade calculations.

Users can enter student details and marks for multiple subjects, view
academic results, search student records, update marks, and delete
records.
✨ Features
- Add student records
- View all student records
- Search students using Student ID
- Update subject marks
- Delete student records
- Calculate total marks
- Calculate percentage
- Assign grades automatically
- Validate marks between 0 and 100
- Store records persistently in a JSON file
🛠️ Technologies Used
- Language: Python 3
- Storage: JSON
- Libraries: json, os (Python standard library)
## 🏗️ System Architecture

```text
                 +------------------+
                 |      User        |
                 +--------+---------+
                          |
                          v
                 +------------------+
                 |    Main Menu     |
                 +--------+---------+
                          |
       +------------------+------------------+
       |         |         |        |        |
       v         v         v        v        v
   Add Student  View    Search   Update   Delete
       |         |         |        |        |
       +---------+---------+--------+--------+
                          |
                          v
                 +------------------+
                 | Student Records  |
                 |   Dictionary      |
                 +--------+---------+
                          |
                          v
                 +------------------+
                 | Grade Calculation|
                 | Total & Average  |
                 +--------+---------+
                          |
                          v
                 +------------------+
                 | Grade Assignment|
                 +--------+---------+
                          |
                          v
                 +------------------+
                 | JSON File Storage|
                 |  students.json  |
                 +------------------+
```
## 📂 Project Structure

```text
Student-Grade-Management-System/
│
├── student_grade_management.py
├── students.json
└── README.md
```                    # Project documentation
## 🛠️ Technologies Used

- Python 3
- JSON
- Functions
- Dictionaries
- File Handling
- Conditional Statements
- Loops
- `json` and `os` libraries
🚀 Installation and Execution
1. Clone the repository
git clone https://github.com/gosettisowmya/Student-Grade-Management-System.git
2. Navigate into the project folder
cd Student-Grade-Management-System
3. Run the program
python student_grade_management.py
🖥️ Menu Options
When you run the program, the following menu is displayed:
===== Student Grade Management System =====

1. Add Student
2. View All Students
3. Search Student
4. Update Student Marks
5. Delete Student
6. Exit
  Option                 Description
  Add Student            Enter a student ID, name, subjects, and marks
View All Students      Display all stored student records
Search Student         Find a student using their ID
Update Student Marks   Modify marks for an existing subject
Delete Student         Remove a student record
Exit                   Close the application
📊 Grade Calculation
The system calculates total marks and average percentage across the
entered subjects.

  Percentage   Grade
  90--100      A+
80--89.99    A
70--79.99    B
60--69.99    C
50--59.99    D
Below 50     F
💾 Data Storage
Student records are saved in a local JSON file named students.json.
The file is automatically created when student data is saved, and
records can be loaded again when the program is restarted.
📚 Python Concepts Demonstrated
- Functions and modular programming
- Dictionaries and data structures
- Loops and conditional statements
- User input handling
- File handling
- JSON serialization and deserialization
- CRUD operations (Create, Read, Update, Delete)
- Basic validation and exception handling
🔮 Future Enhancements
- Graphical user interface (GUI)
- Student ranking and class toppers
- Export student reports to CSV or Excel
- Subject-wise performance analysis
- Database integration using MySQL or SQLite
👩‍💻 Author
Gosetti Sowmya

GitHub: @gosettisowmya
