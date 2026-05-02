import random
def creat_matrix(n):
    matrix=[]
    for i in range(n):
        row =[]
        for j in range(n):
            row.append(random.randint(1, n*n*10-1))
        matrix.append(row)
    return matrix


def pretty_print(matrix):
    for row in matrix:
        for utga in row:
            print(f"{utga:4}", end=" ")
        print()
    print()

def plus(A, B, n):
    result =[] 
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

def multiply(A, B, n):
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            t=0
            for m in range(n):
                t+= A[i][m] * B[m][j]
            row.append(t)
        result.append(row)
    return result

n = int(input())
A=creat_matrix(n)
B=creat_matrix(n)
C=creat_matrix(n)

#A*B
D= multiply(A, B, n)

#A*B+C
result= plus(D, C, n)
print("A=")
pretty_print(A)

print("B=")
pretty_print(B)

print("C=")
pretty_print(C)

print("A*B=")
pretty_print(D)

print("A*B+C=")
pretty_print(result)
