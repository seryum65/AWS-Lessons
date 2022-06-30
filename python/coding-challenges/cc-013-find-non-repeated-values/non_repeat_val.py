
products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]

# with open("products.txt", 'w', encoding="utf-8") as file:
#     for output in products:
#         file.write(output + '\n')  # adds a newline character to each string
# with open("products.txt", 'r', encoding="utf-8") as file:
#     #print(file.readlines())  # reads and displays entire lines in a list

product_list = []

for line in products:
    product_list.append(line)
#print(product_list)

output={}
for i in range(len(product_list)):
    if product_list[i] not in output:
        output[product_list[i]]=0
    output[product_list[i]]+=1

for x in output:
    if (output[x]== 1):
        print(x,end="\n")


