try :
    numberOfStudent = int(input("Number of Student : "))
    if numberOfStudent < 1 :
        raise ValueError("Number of student can't be below 1")
    totalScore = 0
    totalPassScore = 0
    totalFailScore = 0
    topScore = -1
    for i in range(1,numberOfStudent+1) :
        userInput = float(input(f"Student {i} : "))
        if userInput > topScore :
            topScore = userInput
        totalScore += userInput
        if userInput >= 5 :
            totalPassScore += userInput
        else :
            totalFailScore += userInput
    
    allAverage = totalScore / numberOfStudent
    passAverage = totalPassScore / numberOfStudent
    failAverage = totalFailScore / numberOfStudent
    
    print(f"Average score : {allAverage}")
    print(f"Average passing score : {passAverage}")
    print(f"Average failing score : {failAverage}")
    print(f"Highest score : {topScore}")
except:
    print()
    print("Error Occured")
    print("Programme end")
    print()