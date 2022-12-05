from Matrix import Matrix


def inversion(matrix):
    if matrix.getColumns() == matrix.getRows():
        step = matrix.getColumns()
        data = matrix.getData()
        for i in range(0, step):  # appending a unit matrix to our matrix
            for j in range(0, step):
                if i == j:
                    data[i].append(1)
                else:
                    data[i].append(0)

        printStep(data, step)
        for i in range(0, step):
            k = -1
            if data[i][i] == 0:  # if diagonal element is 0, we need to change rows
                for j in range(0, step):
                    if data[j][i] != 0:
                        k = j
                        break
                if k == -1:  # if every element is 0 in column, that means, that inverse matrix does not exist
                    print("Impossible to solve")
                    return False
                else:
                    for j in range(0, 2 * step):  # replacing rows
                        buffer = data[i][j]
                        data[i][j] = data[k][j]
                        data[k][j] = buffer
                    printStep(data, step)

            a = data[i][i]
            for j in range(0, step):    # just Gauss elimination
                koef = data[j][i] / a
                if i != j:
                    for k in range(0, 2 * step):
                        data[j][k] = data[j][k] - data[i][k] * koef
                    printStep(data, step)

        for i in range(0, step):    # if elements on diagonal is not 1, we need to solve this problem
            if data[i][i] != 1:
                lomeno = data[i][i]
                for j in range(0, 2 * step):
                    data[i][j] = data[i][j] / lomeno

        printStep(data, step)
        print("RESULT")
        dataResult = []
        for i in range(0, step):
            buf = ""
            resRow=[]
            for j in range(step, 2 * step):
                resRow.append(data[i][j])
                buf += str(data[i][j]) + " "
            print(buf)
            dataResult.append(resRow)
        resultMatrix = Matrix(step, step, dataResult)
        return resultMatrix
    else:
        print("Matrix need to have the same count of columns and rows")
        return False


def printStep(data, step):
    print("New Step")
    for i in range(0, step):
        buf = ""
        for j in range(0, 2 * step):
            buf = buf + str(data[i][j]) + " "
        print(buf)
    print()