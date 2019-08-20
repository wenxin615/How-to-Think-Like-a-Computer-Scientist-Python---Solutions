def dot_product(vec1,vec2):
    sum = 0
    for num in range(len(vec1)):
        sum += vec1[num] * vec2[num]
    return sum
    
print(dot_product([1,1],[1,1]))    
print(dot_product([1, 2], [1, 4]))
print(dot_product([1, 2, 1], [1, 4, 3]))
