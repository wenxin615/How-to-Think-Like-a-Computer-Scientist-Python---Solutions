print("Hello World")

def add_vectors(vec1,vec2):
    sum = []
    for num in range(len(vec1)):
       sum.append(vec1[num]+vec2[num])
       
    return sum

print(add_vectors([1, 1], [1, 1])==[2,2])
print(add_vectors([1, 2], [1, 4]) == [2, 6])
print(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
