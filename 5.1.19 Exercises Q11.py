print("Hello World")

def count(letter,words):
    counter = 0
    for a in range(len(words)):
        if words[a] == letter[0]:
                if words[a:a+len(letter)] == letter:
                    counter += 1
                    
    print(counter)
    
    

count("is","Mississippi")
count("an","banana")
count("ana","banana")
count("nana","banana")
count("nanan","banana")
count("aaa","aaaaaa")
