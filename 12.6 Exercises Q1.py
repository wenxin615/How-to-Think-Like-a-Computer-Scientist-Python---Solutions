
def readposint():
    flag = 1
    while flag is 1:
        
        try: 
            num = int(input("Please enter a positive number:"))
            if num > 0:
                flag = 0
                print("Correct Number!")
            else:
                print("Invalid Number!")
        except ValueError:
            print("That's not an integer. Try again")
        
readposint()
    
    
