try :
    userInput = input("Enter username: ")
    attempt = 0
    while userInput != "Lisa" and attempt < 2  :
        attempt += 1
        userInput = input("Incorrect. Enter again: ")
    if attempt < 2 :
        print(f"Hello, {userInput}")
    else :
        print("Not allowed. Incorrect name.")
except :
    print()
    print("Error Occured")
    print("Programme end")
    print()