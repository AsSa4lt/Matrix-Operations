class Matrix:
    def __init__(self, rows, columns, data):
        self.rows = rows
        self.columns = columns
        self.data = data

    def getRows(self):
        return self.rows

    def getColumns(self):
        return self.columns

    def getData(self):
        return self.data

    def printMatrix(self):
        for i in range(0, self.rows):
            row = ""
            for j in range(0, self.columns):
                row += str(self.data[i][j]) + " "
            print(row)
