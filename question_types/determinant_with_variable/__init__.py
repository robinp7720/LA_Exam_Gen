# coding=utf-8

import numpy as np
import sympy
from sympy.matrices import randMatrix

def generate_question(matrix_dimension=3, max_random_value=4, min_random_value=-4):
    output = f"\\question Für $a \in \mathbb{{R}}$ sei $A_{{a}} \in \mathbb{{R}}^{{{matrix_dimension} \\times {matrix_dimension}}}$ mit\n"
    # Generate a random matrix of size MATRIX_DIMENSION (defaults to 3)
    static_matrix = randMatrix(matrix_dimension, matrix_dimension, min_random_value, max_random_value, percent=30)
    coefficient_matrix = randMatrix(matrix_dimension, matrix_dimension, min_random_value, max_random_value, percent=60)

    a = sympy.symbols("a")

    matrix = (a*coefficient_matrix + static_matrix)

    output += "\\begin{displaymath}"
    output += sympy.latex(matrix)
    output += "\\end{displaymath}"

    output += "\\begin{parts}\n"

    output += "\\part[2] Berechnen Sie die Determinante von $A_{a}$:\n"
    output += "\\begin{solutionorbox}[1in]\n"
    output += f"${sympy.latex(matrix.det())}$"
    output += "\\end{solutionorbox}\n"

    output += "\\part[1] Für welche Werte von $a$ ist $A_{a}$ invertierbar?\n"
    output += "\\begin{solutionorbox}[1in]\n"
    output += f"$A_{{a}}$ ist invertierbar für alle ${sympy.latex(matrix.det())}\\neq0$\\\\"
    output += f"$\\Rightarrow a\\notin{sympy.latex(sympy.solveset(matrix.det(),a))}$"
    output += "\\end{solutionorbox}\n"

    output += f"\\part[1] Für welche $a \\in \\mathbb{{Z}}$ ist $A_{{a}}$ invertierbar in $\mathbb{{Z}}^{{{matrix_dimension} \\times {matrix_dimension}}}$ ?\n"
    output += "\\begin{solutionorbox}[1in]\n"
    output += f"$A_{{a}}$ ist invertierbar in $\\mathbb{{Z}}$ für alle $a \\in \\mathbb{{Z}}$ mit ${sympy.latex(matrix.det())} = 1$\\\\"
    output += f"$\\Rightarrow a \\in {sympy.latex(sympy.solveset(matrix.det() - 1,a, domain=sympy.Integers))}$"
    output += "\\end{solutionorbox}\n"

    output += "\\end{parts}\n"

    return [output]


if __name__ == "__main__":
    print(generate_question())
