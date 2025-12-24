def checkAnswer(correctAnswer,studentAnswer) :
    correctCount = 0
    if len(correctAnswer) != len(studentAnswer) :
        print("Incomplete answer")
    else :
        for i in range(len(studentAnswer)) :
            if studentAnswer[i] == correctAnswer[i] :
                correctCount += 1
        print(f"Number of correct answers: {correctCount}")

try : 
    print("--- Multiple Choice Answer Checker ---")
    correctAnswer = input("Enter the string of correct answers: ").lower()
    studentAnswer = input("Enter the string of student's answers: ").lower()
    checkAnswer(correctAnswer,studentAnswer) 
    while True :
        correctAnswer = input("Enter the correct answers (type 'exit' to quit): ").lower()
        if correctAnswer == "exit" :
            break 
        studentAnswer = input("Enter the student's answers: ")
        checkAnswer(correctAnswer,studentAnswer) 
    print("Exiting program. Goodbye!")
except:
    print("Error")