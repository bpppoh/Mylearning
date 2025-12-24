try :
    numberOfStudent = int(input("Number of Student : "))
    if numberOfStudent < 1 :
        raise ValueError("Number of student can't be below 1")
    totalScore = 0
    for i in range(1,numberOfStudent+1) :
        totalScore += int(input(f"Student {i} : "))
    scoreAverage = totalScore / numberOfStudent
    print(f"Total Scores : {scoreAverage}")
except:
    print()
    print("Error Occured")
    print("Programme end")
    print()