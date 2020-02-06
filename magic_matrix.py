#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.

matrix1 = [[8,1,6],[3,5,7],[4,9,2]]
matrix2 = [[6,1,8],[7,5,3],[2,9,4]]
matrix3 = [[4,9,2],[3,5,7],[8,1,6]]
matrix4 = [[2,9,4],[7,5,3],[6,1,8]]
matrix5 = [[8,3,4],[1,5,9],[6,7,2]]
matrix6 = [[4,3,8],[9,5,1],[2,7,6]]
matrix7 = [[6,7,2],[1,5,9],[8,3,4]]
matrix8 = [[2,7,6],[9,5,1],[4,3,8]]

def matrix_loss(a, b):
  loss = 0
  for i in range(3):
    for j in range(3):
      loss += abs(a[i][j] - b[i][j])
  return loss

def formingMagicSquare(matrix):
    min_loss = min(matrix_loss(matrix, matrix1),
               matrix_loss(matrix, matrix2),
               matrix_loss(matrix, matrix3),
               matrix_loss(matrix, matrix4),
               matrix_loss(matrix, matrix5),
               matrix_loss(matrix, matrix6),
               matrix_loss(matrix, matrix7),
               matrix_loss(matrix, matrix8))
    return min_loss

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
