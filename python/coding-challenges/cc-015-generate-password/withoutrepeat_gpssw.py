import random
import string


def generate_password_withoutRepeat():

    numbers = string.digits
    yourName = input(" Please enter your name (without any spaces): ").lower().replace(" ", "")

    create_three_letters = ''.join((random.sample(yourName,3)))  
    create_four_digit = ''.join((random.sample(numbers,4)))
   

    print (create_three_letters + create_four_digit)

generate_password_withoutRepeat()




