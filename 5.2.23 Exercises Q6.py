def scalar_mult(scalar,vector):
    sum = []
    for num in vector:
        sum.append(scalar*num)
    return sum

print(scalar_mult(5, [1, 2]) == [5, 10])
print(scalar_mult(3, [1, 0, -1]))
print(scalar_mult(7, [3, 0, 5, 11, 2]))
