def get_matrix(n, value):

    matrix = []

    for i in range(n):
        matrix.append([])
        for j in range(2):
            matrix[i].append(value)
    return matrix

print(get_matrix(3,5))
