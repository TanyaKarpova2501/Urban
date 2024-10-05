from pydoc import apropos


def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return(0 >= 1)
result_1 = get_matrix( 5, 7, 15)
result_2 = get_matrix( 8, 3, 10)
result_3 = get_matrix( 2, 5, 20)
print(result_1)
print(result_2)
print(result_3)