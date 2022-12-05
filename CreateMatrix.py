from Matrix import Matrix


def setMatrix():
    print("Enter count of rows")
    rows = int(input())
    print("Enter count of columns")
    columns = int(input())
    data = []
    for i in range(0, rows):
        print("Enter row " + str(i+1) + ":")
        a = [int(x) for x in input().split()]
        data.append(a)
    matrix = Matrix(rows, columns, data)
    print()
    matrix.printMatrix()
    print()
    return matrix