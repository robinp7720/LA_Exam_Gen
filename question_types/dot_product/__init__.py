# coding=utf-8
import math
import random

import numpy as np
from modules.generators.matrix import pmatrix_surds, pmatrix


def generate_random_surd(max_multiplicator, min_multiplicator, max_surd, min_surd=0):
    multiplicator = random.randint(min_multiplicator, max_multiplicator)
    surd = random.randint(min_surd, max_surd)

    return ((multiplicator, surd), multiplicator * math.sqrt(surd))

def generate_question(max_multiplicator=6, min_multiplicator=-6, max_surd=9):
    v = []
    w = []
    for i in range(3):
        v.append([generate_random_surd(max_multiplicator, min_multiplicator, max_surd)])
        w.append([generate_random_surd(max_multiplicator, min_multiplicator, max_surd)])

    output = f"\\question Seien $v={pmatrix_surds(v)}$ und $w={pmatrix_surds(w)}$  $\\in \\mathbb{{R}}^3$\n"

    output += "\\begin{parts}\n"

    output += "\\part[1] Bestimmen Sie die Norm von $v$:\n"
    output += "\\makeemptybox{1in}\n"
    output += "\\part[1] Bestimmen Sie den Cosinus des Winkels $\\alpha$ zwischen $v$ und $w$:\n"
    output += "\\makeemptybox{1in}\n"

    x = []
    y = []
    z = []
    for i in range(3):
        x.append([random.randint(min_multiplicator, max_multiplicator)])
        y.append([random.randint(min_multiplicator, max_multiplicator)])
        z.append([random.randint(min_multiplicator, max_multiplicator)])

    output += f"\\part[2] Bestimmen Sie zur Basis \\langle {pmatrix(x)}{pmatrix(y)}{pmatrix(z)} \\rangle von $\\mathbb{{R}}^3$ mit dem Gram-Schmidt Verfahren die zugehörige Orthogonalbasis:\n"
    output += "\\makeemptybox{2in}\n"

    t = []
    for i in range(3):
        t.append([random.randint(min_multiplicator, max_multiplicator)])

    output += f"\\part[2] Sie $U = ({pmatrix(t)})$\\\\"
    output += f"Berechnen Sie eine Basis von U^\\top"
    output += "\\makeemptybox{2in}\n"

    output += "\\end{parts}\n"

    solution = ""

    return [output, solution]


if __name__ == "__main__":
    print(generate_question())
