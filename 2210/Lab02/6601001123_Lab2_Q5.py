try :
    word = ""
    while True :
        userInput = input("Next word : ")
        if userInput != "." :
            word += " " + userInput
        else :
            break
    print(f"Sentence :{word}")
except :
    print()
    print("Error Occured")
    print("Programme end")
    print()