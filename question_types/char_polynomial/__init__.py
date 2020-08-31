# coding=utf-8

import numpy as np
from modules.generators.matrix import pmatrix_displaymath
import sympy


def generate_question(matrix_dimension=4, max_random_value=4, min_random_value=-4):
    output = f"\\question Sei $A \\in \\mathbb{{R}}^{{{matrix_dimension} \\times {matrix_dimension}}}$ mit\n"
    # Generate a random matrix of size MATRIX_DIMENSION (defaults to 3)
    matrix = np.random.randint(min_random_value, max_random_value + 1, (matrix_dimension, matrix_dimension))

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if np.random.randint(0, 5) < 3:  # but less than 50%
                matrix[y, x] = 0

    output += pmatrix_displaymath(matrix, "A")

    output += "\\begin{parts}\n"

    M = sympy.Matrix(matrix)

    output += "\\part[2] Berechnen Sie das charakteristische Polynom von A:\n"
    output += "\\begin{solutionorbox}[1in]\n"
    output += f"char(A) $= {sympy.latex(M.charpoly('X'))}$\n"
    output += "\\end{solutionorbox}\n"
    output += "\\part[1] Berechnen Sie die Eigenwerte von A:\n"
    output += "\\begin{solutionorbox}[1in]\n"
    output += f"${sympy.latex(M.eigenvals())}$\n"
    output += "\\end{solutionorbox}\n"
    output += "\\part[2] Geben Sie zu jedem Eigenwert von A eine Basis des Eigenraumes an:\n"
    output += "\\begin{solutionorbox}[1in]\n"
    output += f"${sympy.latex(M.eigenvects())}$\n"
    output += "\\end{solutionorbox}\n"
    output += "\\part[2] Was sind die geometrischen und algebraischen Vielfachheiten der Eigenwerte von A:\n"
    output += "\\makeemptybox{1in}\n"

    output += "\\end{parts}\n"

    return [output]


if __name__ == "__main__":
    print(generate_question())
