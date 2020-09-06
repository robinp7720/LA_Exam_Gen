# coding=utf-8

import numpy as np
from modules.generators.matrix import pmatrix_displaymath
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

    output += "\\part[2] Berechnen Sie das charakteristische Polynom von A:\n"
    output += "\\begin{solutionorbox}[1in]\n"
    output += f"$\\chi_{{A}}(X) = {sympy.latex(M.charpoly('X').as_expr())}$\n"
    output += "\\end{solutionorbox}\n"
    output += "\\part[1] Berechnen Sie die Eigenwerte von A:\n"
    output += "\\begin{solutionorbox}[1in]\n"

    eigenvalues = M.eigenvals()
    eigenvectors = M.eigenvects()

    # generate sorted list form of the eigenvalues

    eigenvalues_list = []

    for i in eigenvalues:
        eigenvalues_list.append(i)

    eigenvalues_list.sort()
    eigenvalues_list = map(lambda x: str(x), eigenvalues_list);

    eigenvalues_string = ", ".join(eigenvalues_list);

    # generate good looking version of the eigenvectors

    eigenvectors_dic = {}

    for i in eigenvectors:
        eigenvectors_dic[i[0]] = i[2]

    # generate multiplicities of eigenvalues

    multiplicities = {}

    for i in eigenvectors:
        multiplicities[i[0]] = { "g": len(i[2]), "m": i[1] }

    output += f"${sympy.latex(eigenvalues_string)}$\n"
    output += "\\end{solutionorbox}\n"
    output += "\\part[2] Geben Sie zu jedem Eigenwert von A eine Basis des Eigenraumes an:\n"
    output += "\\begin{solutionorbox}[1in]\n"
    output += f"${sympy.latex(eigenvectors_dic)}$\n"
    output += "\\end{solutionorbox}\n"
    output += "\\part[2] Was sind die geometrischen und algebraischen Vielfachheiten der Eigenwerte von A:\n"
    output += "\\begin{solutionorbox}[1in]\n"
    output += f"${sympy.latex(multiplicities)}$\n"
    output += "\\end{solutionorbox}\n"

    output += "\\end{parts}\n"

    return [output]


if __name__ == "__main__":
    print(generate_question())
