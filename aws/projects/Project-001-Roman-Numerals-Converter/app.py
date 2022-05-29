
def intToRoman(num):
  
    # Storing roman values of digits from 0-9
    # when placed at different places
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
  
    # Converting to roman
    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]
  
    ans = (thousands + hundreds +
           tens + ones)
  
    return ans
  
# Driver code
#  if __name__ == "__main__":
#     print("This program converts decimal numbers to Roman Numerals (To exit the program, please type 'exit')")
while True:
    
    print("\nThis program converts decimal numbers to Roman Numerals (To exit the program, please type 'exit')")
    number = (input("Please enter a number between 1 and 3999, inclusively :"))
    if number.isdecimal() == False:
        if number.lower() == "exit":
            print("\nExiting the program... Good Bye")
            break
        
        else:
            print("\nNot Valid Input !!!")
            isdigit = True
            continue
    number = int(number)
    try:

        if number<1 or number>3999:
            print("\nNot Valid Input !!!")
            isdigit = False
        else:
            isdigit = True

       
        print(f'\nRoman numerals representation of decimal number {number} = {intToRoman(number)}')
    except IndexError:
        print("")
