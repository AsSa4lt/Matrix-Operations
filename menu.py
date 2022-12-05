def menu(isMatrixA, isMatrixB, isResult):
    print("1 to set matrix A")
    print("2 to set matrix B")
    if isMatrixA:
        print("3 to inverze matrix A")
        print("4 to get determinant of matrix A")
    if isMatrixA and isMatrixB:
        print("5 for matrix addition")
        print("6 for matrix multiplication(A*B)")
    if isResult != False:
        print("7 to insert result in A")
    print("-1 to end")
