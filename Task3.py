from ClassLineTask3 import Line
from ClassLineTask3 import Point
import math
import tkinter as tk
from tkinter import filedialog

import sys
import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    return parser
def fromfile():
    try:
        listClass = []
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        f = open(file_path)
        matrix = f.readlines()
        matrix = [[int(n) for n in x.split()] for x in matrix]
        for i in range(len(matrix)):
            listClass.append(Line(int(matrix[i][0]), int(matrix[i][1]), int(matrix[i][2])))
        f.close()
        return listClass
    except IOError:
        print('Проблема с файлом')
def printClassList(list1):
    for i in list1:
        print(i)
def findIntersectionPoints(listLines):
    pointList = list()
    for i in range(len(listLines)):
        for j in range(i+1,len(listLines)):
            y = (listLines[j].a * listLines[i].c - listLines[i].a * listLines[j].c) / (
                        listLines[i].a * listLines[j].b - listLines[j].a * listLines[i].b)
            x = (-listLines[j].b*y-listLines[j].c)/listLines[j].a
            if(listLines[i].a * x + listLines[i].b * y + listLines[i].c == 0):
                point = Point(x, y, listLines[i], listLines[j])
                pointList.append(point)
    return pointList
def findMinIntersectionPoint(pointList):
    distance = list()
    for i in range(len(pointList)):
        c = math.sqrt(math.pow((pointList[i].x),2) + math.pow((pointList[i].y),2))
        distance.append(c)
    minIndex = distance.index(min(distance))
    return pointList[minIndex]
def printPoint(minPoint):
    print('Координаты: ', minPoint.x, minPoint.y)
    print('Пересекающиеся линия 1:', minPoint.intersectionLine1.a, minPoint.intersectionLine1.b,
          minPoint.intersectionLine1.c)
    print('Пересекающиеся линия 2:', minPoint.intersectionLine2.a, minPoint.intersectionLine2.b,
          minPoint.intersectionLine2.c)
if __name__=='__main__':
    parser = createParser()
    namespace = parser.parse_args()
    if namespace.command == 'f':
        mylist = fromfile()
        minPoint = findIntersectionPoints(mylist)
        printPoint(findMinIntersectionPoint(minPoint))