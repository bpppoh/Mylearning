try :
    userInput = int(input("Enter an integer : "))
    if userInput > 0 :
        for i in range(1,userInput+1) :
            if userInput % i == 0 :
                print(i)
    else :
        print("Input number is below 0")
except :
    print()
    print("Error Occured")
    print("Programme end")
    print()