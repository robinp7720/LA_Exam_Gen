# coding=utf-8

import numpy as np
from modules.generators.matrix import pmatrix_displaymath
import sympy


def generate_question(matrix_dimension=4, max_random_value=4, min_random_value=-4):
    output = "Sei $V$ ein $\mathbb{R}$ -Vektorraum mit einem Skalarprodukt $\\langle\\cdot, \\cdot\\rangle .$"

    output += "\\begin{parts}\n"

    output += "\\part[1] Sei $v \in V$ fest gewählt. Zeigen Sie, dass die Abbildung $\\varphi_{v}: V \\rightarrow \\mathbb{R}$ mit $\\varphi_{v}(w)=\\langle v, w\\rangle$ eine lineare Abbildung ist."
    output += "\\begin{solutionorbox}[3in]\n"

    output += "So das $\\varphi_{v}(w)$ eine Lineare Abbildung ist, muss Folgendes gelten: \\\\"
    output += "$\\varphi_{v}(\\lambda w) = \\lambda \\varphi_{v}(w)$ und $\\varphi_{v}(x + w) = \\varphi_{v}(x) + \\varphi_{v}(w)$\\\\ \\\\"
    output += "$\\varphi_{v}(\\lambda w) = \\langle v, \\lambda w\\rangle = v_{1} \\lambda w_{1} + v_{2} \\lambda w_{2} + \\hdots = \\lambda (v_{1} w_{1} + v_{2} w_{2} + \\hdots) = \\lambda \\langle v, w\\rangle = \\lambda \\varphi_{v}(w)$\\\\"
    output += "$\\varphi_{v}(x + w) = \\langle v, x + w\\rangle = v_{1} (x_{1} + w_{1}) + v_{2} (x_{2} + w_{2}) + \\hdots  = v_{1} x_{1} + v_{2} x_{2} + \\hdots + v_{1}  w_{1} + v_{2} w_{2} + \\hdots = \\langle v, x\\rangle + \\langle v, w\\rangle = \\varphi_{v}(x) + \\varphi_{v}(w)$\\\\ \\\\"
    output += "$\\Rightarrow \\varphi_{v}(w)=\\langle v, w\\rangle$ ist eine lineare Abbildung."

    output += "\\end{solutionorbox}\n"

    output += "\\part[4] Sei $W \\leq V$ ein Unterraum von $V$ und $W^{\\perp}=\\{x \\in V \\mid\\langle x, y\\rangle=0$ für alle $y \\in W\\}.$ Zeigen Sie, dass für $w \\in W, u \\in W^{\\perp}$ und $v=w+u$ gilt $\\|v\\|^{2}=\\|w\\|^{2}+\\|u\\|^{2}$\\\\"
    output += "\\begin{solutionorbox}[7in]\n"
    # TODO: Add answer for sub vector space question for skalar functions
    output += "\\end{solutionorbox}\n"
    output += "\\end{parts}\n"

    return [output]


if __name__ == "__main__":
    print(generate_question())
