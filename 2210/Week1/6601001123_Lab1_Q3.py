import datetime

userInput = input("Name,age: ").split()
name = userInput[0]
age = int(userInput[1])
yearOfBirth = datetime.datetime.now().year - age
print(f"{name}'s year of birth is {yearOfBirth}.")