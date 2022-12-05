from Matrix import Matrix


def addMatrices(matrixA, matrixB):
    if matrixA.getRows() == matrixB.getRows() and matrixA.getColumns() == matrixB.getColumns():
        dataA = matrixA.getData()
        dataB = matrixB.getData()
        dataRes = []
        print("RESULT")
        for i in range(0, matrixA.getRows()):
            rowRes = ""
            row = []
            for j in range(0, matrixA.getColumns()):
                row.append(dataA[i][j] + dataB[i][j])
                rowRes += str(dataA[i][j] + dataB[i][j]) + " "
            print(rowRes)
            dataRes.append(row)

        return Matrix(matrixA.getRows(), matrixB.getColumns(), dataRes)
    else:
        print("Count of columns and rows of both matrices must be the same")
        return False
