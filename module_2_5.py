def get_matrixn(n, m, value):
    matrix = []
    if n  < 0:
        return
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

result1 = get_matrixn(2, 2, 10)
result2 = get_matrixn(3, 5, 42)
result3 = get_matrixn(4, 2, 13)

print(result1)
print(result2)
print(result3)