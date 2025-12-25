try :
    print ("--- ID Checksum Calculator ---")
    userInput = input("Enter 13-digit ID number: ")
    if not userInput.isdigit() :
        raise Exception("Error")
    sum = 0
    for i in range(len(userInput)-1) :
        # print(f"{userInput[i]} * {13-i}")
        sum += int(userInput[i])*(13-i)
    reminder = sum % 11
    reminderDiff = 11 - reminder
    reminderDiff = str(reminderDiff)
    print(f"Calculated checksum digit {reminderDiff[len(reminderDiff)-1]}")
except :
    print("Error occured")