import PySimpleGUI as sg

import DeterminantofaMatrix
import MatrixAddition
import MatrixInverse
import MatrixMultiplication
import menu
import CreateMatrix

isMatrixA = False
isMatrixB = False
isResult = False

while True:
    menu.menu(isMatrixA, isMatrixB, isResult)
    action = 0
    try:
        action = int(input())
    except:
        print("It is not a number")
        print()

    match action:
        case 1:
            try:
                matrixA = CreateMatrix.setMatrix()
                print("Matrix A created successfully")
                print()
                isMatrixA = True
            except:
                print("You have made a mistake, try again")
                print()
        case 2:
            try:
                matrixB = CreateMatrix.setMatrix()
                print("Matrix B created successfully")
                print()
                isMatrixB = True
            except:
                print("You have made a mistake, try again")
        case 3:
            if isMatrixA:
                isResult = MatrixInverse.inversion(matrixA)
                print()
            else:
                print("You need to set matrix A")
                print()
        case 4:
            if isMatrixA:
                DeterminantofaMatrix.matrixDet(matrixA)
            else:
                print("You need to set matrix A")
                print()
        case 5:
            if isMatrixA and isMatrixB:
                isResult = MatrixAddition.addMatrices(matrixA, matrixB)
                print()
            else:
                print("You need to create both matrices")
        case 6:
            if isMatrixA and isMatrixB:
                isResult = MatrixMultiplication.multiply(matrixA, matrixB)
                print()
            else:
                print("You need to create both matrices")
        case 7:
            if isResult != False:
                matrixA = isResult
                print("Successfully inserted result into A")
                matrixA.printMatrix()
                print()
            else:
                print("You need to get result")

