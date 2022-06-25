# Python program to find vowels in a string

word=input("\nPlease enter a string:")
vowels_list= []
for i in word.lower():    
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowels_list.append(i)

# Function to find consecutive vowels in a string
def isConcecutive(vowels_list):
    Concecutive = True
    if len(vowels_list) <= 1:
        Concecutive = False

    elif len(vowels_list) > 1:
        for k in range(0,len(vowels_list)-1):
                if ord(vowels_list[k]) == ord(vowels_list[k+1]):
                    Concecutive = False
                elif ord(vowels_list[k]) < ord(vowels_list[k+1]):
                    Concecutive = True
                else:
                    Concecutive = False
    return Concecutive

# Python program to find result of consecutive vowels in a string
if isConcecutive(word):
        print(f"'{word}' contains consequtive letters, Positive")
else:
        print(f"'{word}' contains does not consequtive letters, Negative")




