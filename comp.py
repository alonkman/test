import mysimp

if not mysimp.used_simp:
    print("Please use the simp module functions first.")
else:
    # sum of digits:
    def sumDigits(number): 

        sum = 0
        for digit in str(number):
            sum += int(digit)
        return sum

    number = int(input("Enter a number to sum: "))
    digit_sum = sumDigits(number)

    print("The sum of the digits of", number, "is", digit_sum)

    # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| #

    # palindrome
    def Palindrome(number):
        number_str = str(number)
        if number_str == number_str[::-1]:
            return True
        else:
            return False

    number = int(input("Enter a palindrome number: "))
    if Palindrome(number):
        print(number, "is a palindrome")
    else:
        print(number, "is not a palindrome")
