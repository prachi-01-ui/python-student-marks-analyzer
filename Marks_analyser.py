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
        print("Option 1 selected")
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
    
    