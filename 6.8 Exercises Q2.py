import numpy as np

a = np.array([230, 10, 284, 39, 76])
b = [2]

flag = 1

while (flag):
    for num in a:
        if num < 100:
            flag = 1
            a = a*b
            print(a)    
            break
        else:
            flag = 0
