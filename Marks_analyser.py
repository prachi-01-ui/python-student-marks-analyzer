#function for inputting marks in Choice 1
def get_valid_marks(subject,maximum):
    while True:
        try:
            marks=float(input(f"Enter marks in {subject} (out of {maximum}): "))
            
            if 0<=marks<=maximum:
                return marks
            else:
                print(f"Invalid marks!! Enter marks in between the range 0 and {maximum}.")
        
        except ValueError:
            print("Enter a numeric value.The current input is invalid.")

students=[]

#menu or choices to select which action to perform
while True:     
    print("=" * 40)
    print("       STUDENT MARKS ANALYSER")
    print("=" * 40)
    
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Show Class Topper")
    print("5. Show Class Average")
    print("6. Show Subject-wise Highest")
    print("7. Exit")
    
    print("="*40)
    choice=input("Choose your desired task: ")
    
    if choice=='1':
        name=input("Enter student's name: ")
        
        ai_marks=get_valid_marks("AI and its Applications", 40)
        oops_marks=get_valid_marks("OOPS in Java", 40)
        dbms_marks=get_valid_marks("DBMS", 30)
        os_marks=get_valid_marks("Operating System", 30)
        maths_marks=get_valid_marks("Engineering Maths", 30)
        ads_marks=get_valid_marks("Advanced Data Structures", 40)
        
        total_marks=(ai_marks+oops_marks+dbms_marks+os_marks+maths_marks+ads_marks)
        
        percentage=(total_marks/210) * 100
        
        if percentage>=90:
            grade="A"
        elif percentage>=80:
            grade="B"
        elif percentage>=70:
            grade="C"
        elif percentage>=60:
            grade="D"
        else:
            grade="F"
        
        if (
            ai_marks >= 40 * 0.40
            and oops_marks >= 40 * 0.40
            and dbms_marks >= 30 * 0.40
            and os_marks >= 30 * 0.40
            and maths_marks >= 30 * 0.40
            and ads_marks >= 40 * 0.40
        ):
            result = "PASS"
        else:
            result = "FAIL"
            
        student={
            "name": name,
            "AI and its Applications":ai_marks,
            "OOPS in Java":oops_marks,
            "DBMS":dbms_marks,
            "Operating System":os_marks,
            "Engineering Maths":maths_marks,
            "Advanced Data Structures":ads_marks,
            "total":total_marks,
            "percentage":percentage,
            "grade":grade,
            "result":result
            
        }
        students.append(student)
        print(f"Student {name} added successfully!!")

        
    elif choice=='2':
        if len(students)==0:
            print("No student found in records.Kindly add a student first.")
        else:
            for student in students:
                print("\n========== STUDENT DETAILS ==========")
                print("Student Name:",student["name"])
                print("AI and its Applications:",student["AI and its Applications"],"/ 40.0")
                print("OOPS in Java:",student["OOPS in Java"],"/ 40.0")
                print("DBMS:",student["DBMS"],"/ 30.0")
                print("Operating System:",student["Operating System"],"/ 30.0")
                print("Engineering Maths:",student["Engineering Maths"],"/ 30.0")
                print("Advanced Data Structures:",student["Advanced Data Structures"],"/ 40.0")
                print("-"*38)
                print("Total Marks:",student["total"],"/ 210")
                print("Percentage:",round(student["percentage"],2),"%")
                print("Grade:",student["grade"])
                print("Result:",student["result"])
                print("="*38)
    elif choice=='3':
        search_name=input("Enter student's name to search: ").strip()
        
        found=False
        
        for student in students:
            if student["name"].lower()==search_name.lower():
                found=True
                
                print("\n========== Student Details ==========")
                print("Student Name:",student["name"])
                print("AI and its Applications:",student["AI and its Applications"],"/ 40.0")
                print("OOPS in Java:",student["OOPS in Java"],"/ 40.0")
                print("DBMS:",student["DBMS"],"/ 30.0")
                print("Operating System:",student["Operating System"],"/ 30.0")
                print("Engineering Maths:",student["Engineering Maths"],"/ 30.0")
                print("Advanced Data Structures:",student["Advanced Data Structures"],"/ 40.0")
                print("-"*38)
                print("Total Marks:",student["total"],"/ 210.0")
                print("Percentage:",round(student["percentage"],2),"%")
                print("Grade:",student["grade"])
                print("Result:",student["result"])
                print("="*38)
                break
        if not found:
            print("Student not found....")
    elif choice=='4':
        if len(students)==0:
            print("No student found in records.Kindly add a student first.")
            
        else:
            topper=students[0]
            
            for student in students:
                if student["total"]>topper['total']:
                    topper=student
                    
            print("\n========== CLASS TOPPER ==========")
            print("Student Name:",topper["name"])
            print("Total Marks:",topper["total"])
            print("Percentage:",round(topper["percentage"],2),"%")
            print("Grade:",topper["grade"])
            print("Result:",topper["result"])
            print("="*34)
    elif choice=='5':
        if len(students)==0:
            print("No record found")
        else:
            total_percentage=0
            
            for student in students:
                total_percentage+=student["percentage"]
                
            class_average=total_percentage/len(students)
            
            print("\n========== CLASS AVERAGE ==========")
            print("Number of students in record:",len(students))
            print("Class Average:",round(class_average,2),"%")
            print("="*34)
    elif choice=='6':
        print("Option 6 selected")
    elif choice=='7':
        print("Exiting STUDENT MARKS ANALYSER.....")
        break
    else:
        print("Invalid choice entered. Kindly choose from numbers 1-7.")   
    
    