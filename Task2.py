import tkinter as tk
from tkinter import filedialog
def find_min_max_elements(matrix):
    min = matrix[0][0]
    max = matrix[0][0]
    min_col = 0
    max_col = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if min > matrix[i][j]:
                min = matrix[i][j]
                min_col = j
            elif min == matrix[i][j] and min_col<j:
                min_col = j
            if max < matrix[i][j]:
                max = matrix[i][j]
                max_col = j
            elif max == matrix[i][j] and min_col>j:
                max_col = j
    list_elem = list()
    list_elem.append(min_col)
    list_elem.append(max_col)
    return list_elem
def change_places(col1, col2, matrix):
    tmp = 0
    for i in range(len(matrix)):
        tmp = matrix[i][col1]
        matrix[i][col1] = matrix[i][col2]
        matrix[i][col2] = tmp


def readConsole(mas):
    print('Введите кол-во строк двумерного массива')
    a = int(input())
    print('Введите кол-во столбцов')
    b = int(input())
    for i in range(a):
        maslist = list(map(int,input().split()))
        for j in range(b):
            mas[i][j] = maslist[j]
    return mas
def printMatrix(mas):
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            print(mas[i][j], end='   ')
        print('\n')
def from_file():
    try:
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        f = open(file_path)
        s_matrix = f.readlines()
        s_matrix = [[int(n) for n in x.split()] for x in s_matrix]
        f.close()
        return s_matrix
    except IOError:
        print('Проблема с файлом')
def main():
    print('Исходный массив:\n')
    s_matrix = from_file()
    printMatrix(s_matrix)
    min_max = find_min_max_elements(s_matrix)
    new_matrix = change_places(min_max[0], min_max[1], s_matrix)
    print('итоговая матрица')
    printMatrix(new_matrix)

main()