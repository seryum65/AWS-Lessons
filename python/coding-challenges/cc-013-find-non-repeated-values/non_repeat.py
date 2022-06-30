products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]

def NonRepeating(input):
    output={}
    for i in range(len(input)):
        if input[i] not in output:
            output[input[i]]=0
        output[input[i]] = output[input[i]]+1
    print(output)

    for x in output:
        if (output[x] == 1):
            print(x,end="\n")

NonRepeating(products)