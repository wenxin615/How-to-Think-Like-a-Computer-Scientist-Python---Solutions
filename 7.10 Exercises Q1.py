with open("readme.txt","r") as my_text:
    
    all_lines = my_text.readlines()

    for line in reversed(list(all_lines)):
        print(line.rstrip())
