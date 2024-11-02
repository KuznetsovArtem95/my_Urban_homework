def get_matrix(n,m,value):
    matrix=[]
    if n<=0 or m<=0:
        return []
    for a in range(n):
        batrix=[]
        matrix.append(batrix)
        for b in range(m):
            batrix.append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)


