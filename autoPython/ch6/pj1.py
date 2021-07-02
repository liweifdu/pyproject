#!/usr/bin/python3

def printTable1(tableLst):
    lenParam = []
    for i in range(len(tableLst)):
        lenParam.append(0)
        for j in range(len(tableLst[i])):
            if len(tableLst[i][j]) >= lenParam[i]:
                lenParam[i] = len(tableLst[i][j]) + 1

    for j in range(len(tableLst[0])):
        for i in range(len(tableLst)):
            print(tableLst[i][j].rjust(lenParam[i]), end='')
        print()

def printTable2(tableLst):
    lenParam = [0] * len(tableLst)
    for i in range(len(tableLst)):
        for j in range(len(tableLst[i])):
            if len(tableLst[i][j]) >= lenParam[i]:
                lenParam[i] = len(tableLst[i][j]) + 1

    for j in range(len(tableLst[0])):
        for i in range(len(tableLst)):
            print(tableLst[i][j].rjust(lenParam[i]), end='')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable1(tableData)
printTable2(tableData)

