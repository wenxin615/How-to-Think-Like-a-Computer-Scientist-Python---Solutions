

def remove(letter,words):
    new_words=words
    for a in range(len(words)):
        if words[a:a+len(letter)] == letter:
            new_words = words[:a] + words[a+len(letter):]
            break      
    print(new_words)

remove("an","banana")
remove("cyc","bicycle")
remove("iss","Mississippi")
remove("eggs","bicycle")
