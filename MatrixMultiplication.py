from Matrix import Matrix


def multiply(matrixA, matrixB):
    if matrixA.getColumns() == matrixB.getRows():
        dataA = matrixA.getData()
        dataB = matrixB.getData()
        dataResult = []
        stepByStep = []
        print("RESULT")
        for i in range(0, matrixA.getRows()):
            rowRes = ""
            row = []

            for j in range(0, matrixB.getColumns()):
                buffer = 0
                oneStep = "a" + str(i + 1) + str(j + 1)+"="
                for k in range(0, matrixA.getColumns()):
                    buffer = buffer + dataA[i][k] * dataB[k][j]
                    if k == 0:
                        oneStep += str(dataA[i][k]) + "*" + str(dataB[k][j])
                    else:
                        oneStep +="+" + str(dataA[i][k]) + "*" + str(dataB[k][j])
                row.append(buffer)
                rowRes += str(buffer) + " "
                stepByStep.append(oneStep)
            dataResult.append(row)
            print(rowRes)
        print()
        print("STEP-BY-STEP")
        for i in range (0, len(stepByStep)):
            print(stepByStep[i])
        return Matrix(matrixA.getRows(), matrixB.getColumns(), dataResult)
    else:
        print("Count of columns of matrix A must be the same as count of rows matrix B")
        return False
