# Python program to find vowels in a string
find_vowels=input("Please enter a string:").lower()
vowels_list= []
for i in find_vowels:    
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowels_list.append(i)

# Python program to find consecutive vowels in a string
if len(vowels_list) <= 1:
    print("Negative")
else:
    for k in range(0,len(vowels_list)):
        for j in range(k):
            if ord(vowels_list[j]) < ord(vowels_list[j+1]):
                Consecutive = True
                k = k + 1
            else:
                Consecutive = False

# Python program to find result of consecutive vowels in a string
if Consecutive:
    print("Positive")
else:
    print("Negative")

