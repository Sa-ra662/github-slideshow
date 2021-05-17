N = str(input("Insert name: "))
gender = int(input("Insert gender (1 = male), (2 = female): "))
grades = []
lengthList = 6
total = 0
for i in range(6):
    score = int(input("Insert every score followed by the enter key: "))
    grades.append(score)
suma = grades[0] + grades[1] + grades[2] + grades[3] + grades[4] + grades[5]
subtraction = grades[0] - grades[1] - grades[2] - grades[3] - grades[4] - grades[5]
average = suma / 6

print(average)
print("The addition of all your grades is: ", suma)
print("the subtraction of all your grades is: ", subtraction)
if gender == 0:
    print("Hi Mr ", name)
else:
    print("Hi Mrs ", name)
if average > 1:
    print(
        "congratulations! you have passed"
    )
else:
    print("Unfortunately You have failed ")