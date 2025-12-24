try :
    previousTemp = -1
    for i in range(1,8) :
        userInput = float(input((f"Day {i} : ")))
        if userInput < previousTemp and i != 1 :
            print(f"Temperature dropped on day {i}")
        previousTemp = userInput
except :
    print()
    print("Error Occured")
    print("Programme end")
    print()