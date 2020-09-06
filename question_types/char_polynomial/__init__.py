# coding=utf-8

import numpy as np
from modules.generators.matrix import pmatrix_displaymath
from question_types.char_polynomial.polynoms import vielfachheit
import sympy

def is_good_matrix(matrix):
    M = sympy.Matrix(matrix)
    eigenvalues = M.eigenvals()
    for i in eigenvalues:
        if not i.is_integer:
            return False

    return True


def generate_good_matrix(matrix_dimension=4, max_random_value=4, min_random_value=-4):
    print("Trying to find a suitable matrix. This may take a while")

    matrix = np.random.randint(min_random_value, max_random_value + 1, (matrix_dimension, matrix_dimension))

    while not is_good_matrix(matrix):
        matrix = np.random.randint(min_random_value, max_random_value + 1, (matrix_dimension, matrix_dimension))

    return matrix


def generate_question(matrix_dimension=4, max_random_value=4, min_random_value=-4):
    output = f"\\question Sei $A \\in \\mathbb{{R}}^{{{matrix_dimension} \\times {matrix_dimension}}}$ mit\n"
    # Generate a random matrix of size MATRIX_DIMENSION (defaults to 4)

    matrix = generate_good_matrix(matrix_dimension, max_random_value, min_random_value)

    output += pmatrix_displaymath(matrix, "A")

    output += "\\begin{parts}\n"

    M = sympy.Matrix(matrix)
    C = M.charpoly('X')

    output += "\\part[2] Berechnen Sie das charakteristische Polynom von A:\n"
    output += "\\begin{solutionorbox}[1in]\n"
    output += f"$\\chi_{{A}}(X) = {sympy.latex(C.as_expr())}$\n"
    output += "\\end{solutionorbox}\n"
    output += "\\part[1] Berechnen Sie die Eigenwerte von A:\n"
    output += "\\begin{solutionorbox}[1in]\n"

    eigenvalues = M.eigenvals()
    count = 0

    charpoly = C.all_coeffs()

    for idx in eigenvalues:
        eigenvalues[idx]= { "g": eigenvalues[idx], "m": vielfachheit(charpoly, idx) }

    for i in eigenvalues:
        count += 1
        output += f"${sympy.latex(i)}$"
        if count < len(eigenvalues):
            output += ', '

    output += "\\end{solutionorbox}\n"
    output += "\\part[2] Geben Sie zu jedem Eigenwert von A eine Basis des Eigenraumes an:\n"
    output += "\\begin{solutionorbox}[1in]\n"
    output += f"${sympy.latex(M.eigenvects())}$\n"
    output += "\\end{solutionorbox}\n"
    output += "\\part[2] Was sind die geometrischen und algebraischen Vielfachheiten der Eigenwerte von A:\n"
    output += "\\begin{solutionorbox}[1in]\n"
    output += f"${sympy.latex(eigenvalues)}$\n"
    output += "\\end{solutionorbox}\n"

    output += "\\end{parts}\n"

    return [output]


if __name__ == "__main__":
    print(generate_question())
