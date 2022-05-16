def convert_milliseconds(num):
  
 
    # Converting to milliseconds
    hours = num // 3600000
    minutes = (num % 3600000) // 60000
    seconds = (num % 60000) // 1000
    milliseconds = num % 1000

    if hours > 0:
        if seconds > 0:
            result = print(f'\n{num} milliseconds = {hours} Hours/s  {minutes} Minutes/s  {seconds} Seconds/s ')
        else :
            result = print(f'\n{num} milliseconds = {hours} Hours/s')
        
    elif minutes > 0 :
        if seconds > 0:
            result = print(f'\n{num} milliseconds = {minutes} Minutes/s  {seconds} Seconds/s ')
        else :
            result = print(f'\n{num} milliseconds = {minutes} Minutes/s ')
 
    elif seconds > 0 :
        result = print(f'\n{num} milliseconds = {seconds} Seconds/s ')
    
    else :
        result = print(f'\njust {milliseconds} Milliseconds/s ')


    return result

while True:
    
    print("\nThis program converts milliseconds into hours, minutes, and seconds (To exit the program, please type 'exit')")
    num = (input("Please enter the milliseconds (should be greater than zero) :"))
    
    if num.isdecimal() == False:
        if num.lower() == "exit":
            print("\nExiting the program... Good Bye!!!\n")
            break
        
        else:
            print("\nNot Valid Input !!!")
            continue
    num = int(num)
    
    if num < 0 :
            print("\nNot Valid Input !!!")
            
           
    
    convert_milliseconds(num)
    

