def bmatrix_displaymath(matrix, variable):
    output = "\\begin{displaymath}\n"

    if variable:
        output += f"{variable} ="

    output += "\\begin{pmatrix}\n"

    for y in matrix:
        count = 0
        for x in y:
            count += 1
            if count < len(y):
                output += str(x) + " && "
                continue
            output += str(x) + " \\\\\n"

    output += "\\end{pmatrix}\n"

    output += "\\end{displaymath}\n"

    return output