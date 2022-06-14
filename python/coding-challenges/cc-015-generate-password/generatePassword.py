import random  
import string

def generate_password():
    length = 3
    num = 4
    numbers = string.digits
    yourName = input("Please enter your name (without any spaces): ").lower().replace(" ", "")

    create_three_letters = ''.join(random.choice(yourName) for x in range(length))  
    create_four_digit = ''.join(random.choice(numbers) for x in range(num))


    print (create_three_letters + create_four_digit)


generate_password()

