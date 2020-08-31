# coding=utf-8
import math
import random
import sympy

import numpy as np
from modules.generators.matrix import pmatrix_surds, pmatrix


def generate_random_surd(max_multiplicator, min_multiplicator, max_surd, min_surd=0):
    multiplicator = random.randint(min_multiplicator, max_multiplicator)
    surd = random.randint(min_surd, max_surd)

    return ((multiplicator, surd), multiplicator * math.sqrt(surd))

def generate_random_surd_sympy(max_multiplicator, min_multiplicator, max_surd, min_surd=0):
    multiplicator = random.randint(min_multiplicator, max_multiplicator)
    surd = random.randint(min_surd, max_surd)

    return (multiplicator * sympy.sqrt(surd))

def generate_question(max_multiplicator=6, min_multiplicator=-6, max_surd=9):
    v = []
    w = []
    for i in range(3):
        v.append([generate_random_surd_sympy(max_multiplicator, min_multiplicator, max_surd)])
        w.append([generate_random_surd_sympy(max_multiplicator, min_multiplicator, max_surd)])

    V = sympy.Matrix(v)
    W = sympy.Matrix(w)

    output = f"\\question Seien $v={sympy.latex(V)}$ und $w={sympy.latex(W)}$  $\\in \\mathbb{{R}}^3$\n"

    output += "\\begin{parts}\n"

    output += "\\part[1] Bestimmen Sie die Norm von $v$:\n"

    output += "\\begin{solutionorbox}[1in]\n"
    output += f"${sympy.latex(V.norm())}$"
    output += "\\end{solutionorbox}\n"


    output += "\\part[1] Bestimmen Sie den Cosinus des Winkels $\\alpha$ zwischen $v$ und $w$:\n"
    output += "\\begin{solutionorbox}[1in]\n"
    output += f"${sympy.latex(((V.dot(W)))/(V.norm() * W.norm()))}$"
    output += "\\end{solutionorbox}\n"

    x = []
    y = []
    z = []
    for i in range(3):
        x.append([generate_random_surd_sympy(max_multiplicator, min_multiplicator, max_surd)])
        y.append([generate_random_surd_sympy(max_multiplicator, min_multiplicator, max_surd)])
        z.append([generate_random_surd_sympy(max_multiplicator, min_multiplicator, max_surd)])

    X = sympy.Matrix(x)
    Y = sympy.Matrix(y)
    Z = sympy.Matrix(z)

    output += f"\\part[2] Bestimmen Sie zur Basis $({sympy.latex(X)},{sympy.latex(Y)},{sympy.latex(Z)})$ von $\\mathbb{{R}}^3$ mit dem Gram-Schmidt Verfahren die zugehörige Orthogonalbasis:\n"
    output += "\\makeemptybox{2in}\n"

    t = []
    for i in range(3):
        t.append([generate_random_surd_sympy(max_multiplicator, min_multiplicator, max_surd)])
    T = sympy.Matrix(t)

    output += f"\\part[2] Sei $U = \\langle {sympy.latex(T)} \\rangle $\\\\"
    output += f"Berechnen Sie eine Basis von $U^\\top$"
    output += "\\makeemptybox{2in}\n"

    output += "\\end{parts}\n"

    return [output]


if __name__ == "__main__":
    print(generate_question())
