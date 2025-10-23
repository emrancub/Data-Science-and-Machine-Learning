# TransposeJagged.py
# Transpose a jagged matrix using zip_longest.

from itertools import zip_longest

matrix = [[1,2,3],[4,5],[6]]
transposed = [list(filter(lambda x: x is not None, row)) for row in zip_longest(*matrix)]

if __name__ == '__main__':
    print(transposed)