class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        rowString = self.matrix_string.splitlines()[index - 1]
        return [int(x) for x in rowString.split()]

    def column(self, index):
        matrixString = [x.split() for x in self.matrix_string.splitlines()]
        columnStringList = [x[index - 1] for x in matrixString]
        return [int(x) for x in columnStringList]
