def remove_letter(letter,words):

    for word in range(len(words)):
        if words[word]==letter:
            continue
        else:
            print(words[word],end="")
    print("\n")
    
    
remove_letter("a","apple")
remove_letter("a","banana")
remove_letter("z","banana")
remove_letter("i","Mississippi")
remove_letter("b","")
remove_letter("b","c")
    
