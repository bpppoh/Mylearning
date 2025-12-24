try :
    balance = 50000
    while balance > 0 :
        print(f"Balance : {balance}")
        userInput = int(input("withdraw : "))
        if userInput <= balance :
            balance -= userInput
        else :
            print("Insufficient fund.")
        # print("==============")
    print(f"Balance is {balance}")
except :
    print()
    print("Error Occured")
    print("Programme end")
    print()