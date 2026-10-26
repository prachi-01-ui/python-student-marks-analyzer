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
        
        print("\nStudent Details")
        print("Student Name:",name)
        print("AI and its Applications:",ai_marks,"/ 40.0")
        print("OOPS in Java:",oops_marks,"/ 40.0")
        print("DBMS:",dbms_marks,"/ 30.0")
        print("Operating System:",os_marks,"/ 30.0")
        print("Engineering Maths:",maths_marks,"/ 30.0")
        print("Advanced Data Structures:",ads_marks,"/ 40.0")
        
        total_marks=(ai_marks+oops_marks+dbms_marks+os_marks+maths_marks+ads_marks)
        
        percentage=(total_marks/210) * 100
        print("-"*38)
        print("Total Marks obtained by the student:",total_marks)
        print("Percentage:",round(percentage,2),"%")
        
        
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

        
    elif choice=='2':
        print("Option 2 selected")
    elif choice=='3':
        print("Option 3 selected")
    elif choice=='4':
        print("Option 4 selected")
    elif choice=='5':
        print("Option 5 selected")
    elif choice=='6':
        print("Option 6 selected")
    elif choice=='7':
        print("Exiting STUDENT MARKS ANALYSER.....")
        break
    else:
        print("Invalid choice entered. Kindly choose from numbers 1-7.")   
    
    