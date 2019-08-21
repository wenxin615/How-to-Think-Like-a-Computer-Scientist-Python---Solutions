with open('readmecopy.txt','r') as f, open('readmecopy2.txt','w') as copy:
    for line in f:
        print(line,end="")
        counter = 0
        for word in line:
            print(word,end=" ")
            counter += 1
            if counter>4:
                copy.write(word)
        copy.write("\n")
