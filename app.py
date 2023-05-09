import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'numbers'))
sys.path.append(path)

from mysimp import addNumbers, subtractNumbers
from comp import sumDigits, Palindrome

# call functions from simp module
result = addNumbers(10, 5)
print(result)

# prompt user to enter a number
num = input("Enter a number: ")

# check if number is a palindrome
if Palindrome(int(num)):
    print(num, "is a palindrome")

    # get the sum of digits of the number
    sum_of_digits = sumDigits(int(num))

    # check if sum is a palindrome
    if Palindrome(sum_of_digits):
        print("The sum of the digits of", num, "is a palindrome")
    else:
        print("The sum of the digits of", num, "is not a palindrome. Sum is", sum_of_digits)

else:
    print(num, "is not a palindrome")
