# coding=utf-8

import numpy as np
from modules.generators.matrix import bmatrix_displaymath


def generate_question(matrix_dimension=3, max_random_value=4, min_random_value=-4):
    output = f"\\question Sei $A \\in \\mathbb{{R}}^{{{matrix_dimension} \\times {matrix_dimension}}}$ mit\n"
    # Generate a random matrix of size MATRIX_DIMENSION (defaults to 3)
    matrix = np.random.randint(min_random_value, max_random_value + 1, (matrix_dimension, matrix_dimension))

    output += bmatrix_displaymath(matrix, "A")

    output += "\\begin{parts}\n"

    output += "\\part[1] Berechnen Sie die Determinante von A:\n"
    output += "\\makeemptybox{1in}\n"

    output += "\\end{parts}\n"

    solution = ""

    return [output, solution]


if __name__ == "__main__":
    print(generate_question())
