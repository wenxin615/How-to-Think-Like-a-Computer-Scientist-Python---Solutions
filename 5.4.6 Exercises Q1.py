def read(strings):
    strings = strings.lower()
    letter_count = {}
    
    for letter in strings:
        letter_count[letter] = letter_count.get(letter,0) + 1
 
    letter_items = list(letter_count.items())
    letter_items.sort()
    
    for (key,value) in letter_items :
        if key != " ":
            print(key, " ", value)
    return letter_count
    
read("ThiS is String with Upper and lower case Letters")
    
    
