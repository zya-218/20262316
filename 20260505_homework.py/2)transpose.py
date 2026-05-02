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

def transpose(A, n):
    result=[]
    for i in range(n):
        row=[0] *n
        result.append(row)
    for i in range(n):
        for j in range(n):
            result[j][i]= A[i][j]
    return result

n=int(input())
A=creat_matrix(n)
N= transpose(A,n)
print("orignal matrix=")
pretty_print(A)

print("transposed matrix=")
pretty_print(N)