def get_matrix(n=0, m=0, value=0):
    matrix = list()

    for i in range(n):
        matrix.append(list())

        for j in range(m):
            matrix[i].append(value)

    return matrix


# print(get_matrix())
# print(get_matrix(3, 3))
# print(get_matrix(2, 5, 8))

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)
