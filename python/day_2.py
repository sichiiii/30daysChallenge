#https://www.codewars.com/kata/5263a84ffcadb968b6000513/train/python
def matrix_mult(a, b):
    result_matrix = [[0 for i in range(len(a))] for i in range(len(a))]
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            for ii in range(0, len(a)):
                result_matrix[i][j]+= a[i][ii] * b[ii][j]
    return result_matrix
