solutionFile = input("Choose your solution file: ")
examFile = input("Choose your exam file: ")
# solutionFile = 'sol2.txt'
# examFile = 'exam2.txt'


with open(solutionFile,'r') as sol :
    solLine = sol.readline()
    sol = solLine.split()
    with open(examFile,'r') as exam :
        studentScoreList = []
        examLines = exam.readlines()
        for line in examLines :
            score = 0
            answer = line.strip().split()
            for i in range(len(sol)) :
                if answer[i] == sol[i]:
                    score = score + 1
            studentScoreList.append(score)
        print(studentScoreList)