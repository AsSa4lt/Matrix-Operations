def det2(data):
    return data[0][0] * data[1][1] - data[0][1] * data[1][0]


def minor(data, i, j):  # getting minor of matrix
    tmp = [row for k, row in enumerate(data) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp


def determinant(data):  # Recursive function
    size = len(data)
    if size == 2:   # if size is 2, we can just count determinant
        return det2(data)

    return sum((-1) ** j * data[0][j] * determinant(minor(data, 0, j))  # if size is bigger than 2, we need to continue
               for j in range(size))


def matrixDet(matrix):
    data = matrix.getData()
    if matrix.getRows() == matrix.getColumns():
        print("Result is: " + str(determinant(data)))
    else:
        print("Matrix need to have the same count of columns and rows")
