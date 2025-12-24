# Each employee is a list with mixed data types: [name, age, salary, employed]
employees = [
    ["Alice", 30, 55000.75, True],
    ["Bob", 25, 48000.00, False]
]

def increaseSalary(employee) :
    employee[2] = employee[2]*110/100
    
# Access and print each employee's data
# for i, emp in enumerate(employees):
#     print(f"Employee {i+1}:")
#     print(f"  Name: {emp[0]} ,Type: {type(emp[0])}")
#     print(f"  Age: {emp[1]},Type: {type(emp[0])}")
#     print(f"  Salary: {emp[2]},Type: {type(emp[0])}")
#     print(f"  Employed: {emp[3]},Type: {type(emp[0])}")
#     print()
print(employees[1][2])
increaseSalary(employees[1])
print(employees[1][2])