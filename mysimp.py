# module of adding and subtracting
used_simp = False


def addNumbers(num1, num2):
    global used_simp
    used_simp = True
    return num1 + num2


def subtractNumbers(num1, num2):
    global used_simp
    used_simp = True
    return num1 - num2
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

sum = addNumbers(num1, num2)
subtract = subtractNumbers(num1, num2)

print('Summing:', sum)
print('subtract:', subtract)






