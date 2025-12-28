studentLibrary = {}

while True :
    print("--- Student Profile Management ---")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. View All Students")
    print("6. Exit")
    print("----------------------------------")
    userChoice = input("Please choose an option : ")
    match int(userChoice) :
        case 1 :
            studentID = int(input("Enter Student ID : "))
            if studentID in studentLibrary :
                print("Student ID already exists.")
            else :
                studentLibrary[studentID] = input("Enter Full Name : ")
                print("Student added successfully.")
        case 2 :
            studentID = int(input("Enter Student ID to view : "))
            if studentID not in studentLibrary :
                print("Student ID not found.")
            else :
                print(f"Result : {studentLibrary[studentID]}")
        case 3 :
            studentID = int(input("Enter Student ID to update : "))
            if studentID not in studentLibrary :
                print("Error: Student ID not found.")
            else :
                studentLibrary[studentID] = input("Enter new Full name : ")
                print("Student data updated successfully.")
        case 4 :
            studentID = int(input("Enter Student ID to delete : "))
            if studentID not in studentLibrary :
                print("Error : Student ID not found.")
            else :
                del studentLibrary[studentID]
                print("Student data deleted successfully.")
        case 5 :
            print("\n--- All Students ---")
            for std_id , name in studentLibrary.items() :
                print(f"ID : {std_id}, Name: {name}")
            print("---------------------")
        case 6 :
            print("Exiting program. Goodbye!")
            break
        case _:
            print("Invalid option. Please try again")
    print()