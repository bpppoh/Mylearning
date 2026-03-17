userInput = input("FirstName lastName : ")
nameList = userInput.split()
firstName = nameList[0]
lastName = nameList[1]
print(f"Hello! {firstName} {lastName}")
print(f"{lastName}, {firstName}")