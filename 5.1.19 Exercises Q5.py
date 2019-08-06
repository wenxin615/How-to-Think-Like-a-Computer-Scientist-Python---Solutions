import string
text = '''Hello, this is me! Im Lee Wen Xin! Nice to meet you.'''

def remove_punctuation(text):
    new_text=""
    for letter in text:
        if letter not in string.punctuation:
            new_text += letter
    return new_text
    
def count_word(text):
    counter = 0
    e_counter = 0
    for letter in text:
        letter.lower()
        counter += 1
        if letter == "e":
            e_counter +=1
    return counter,e_counter

new_text = remove_punctuation(text)
new_count = count_word(new_text)
print(new_count)

print('Your text contains {0} words, of which {1} ({2:.2f}%) contain an "e"'.format(new_count[0],new_count[1],(new_count[1]/new_count[0])*100))

