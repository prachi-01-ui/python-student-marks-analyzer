# Student Marks Analyzer

A Python-based command-line application to manage student marks, calculate academic results, and analyze class performance. The project uses Python fundamentals, data structures, and JSON file handling to store and retrieve student records.

## Features

- **Add Student:** Enter a student's name and marks for six subjects.
- **Marks Validation:** Rejects non-numeric marks and marks outside the allowed range.
- **Result Calculation:** Calculates total marks, overall percentage, grade, and pass/fail status.
- **View All Students:** Displays all saved student records.
- **Search Student:** Search for a student by name.
- **Class Topper:** Identifies all students tied for the highest total marks.
- **Class Average:** Calculates the average of students' overall percentages.
- **Subject-wise Highest:** Identifies the highest marks in each subject, including ties.
- **Persistent Storage:** Saves student records in a local JSON file so they can be loaded after restarting the program.

## Subjects and Maximum Marks

| Subject | Maximum Marks |
|---|---:|
| AI and its Applications | 40 |
| OOPS in Java | 40 |
| DBMS | 30 |
| Operating System | 30 |
| Engineering Maths | 30 |
| Advanced Data Structures | 40 |
| **Total** | **210** |

## Grading Rules

Grades are based on the overall percentage:

| Percentage | Grade |
|---|---|
| 90% and above | A |
| 80% to below 90% | B |
| 70% to below 80% | C |
| 60% to below 70% | D |
| Below 60% | F |

A student passes only if they score at least **40% in every subject**.

## Requirements

- Python 3
- No external Python packages required

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code or a terminal.
3. Ensure `students.json` exists in the project folder. If it doesn't, create it with the contents `[]`.
4. Run the application:

   ```bash
   python Marks_analyser.py
   ```

5. Follow the menu displayed in the terminal.

## Data Storage

Student records are stored locally in `students.json`. This file is listed in `.gitignore` to help prevent personal or test student data from being uploaded to a public repository.

The application creates or updates the JSON file when student records are added.

## Technologies Used

- Python
- Lists and dictionaries
- Functions and loops
- Conditional statements
- Exception handling
- JSON file handling
- Git and GitHub

## Future Improvements

- Search using a unique student ID
- Export student reports
- Add a graphical user interface
- Generate class performance charts
- Add automated tests

## Author

Developed as a Python learning project to practise programming fundamentals, data handling, and GitHub workflows.