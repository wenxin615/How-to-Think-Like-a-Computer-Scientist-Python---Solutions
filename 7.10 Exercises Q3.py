with open('readme.txt','r') as f, open('readmecopy.txt','w') as copy:
    counter = 0
    for line in f:
        counter += 1
        #counters = str(counter)
        copy.write("{0:04d}".format(counter)+" "+line+"\n")
         
            
