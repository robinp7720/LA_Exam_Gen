def pmatrix_displaymath(matrix, variable):
    output = "\\begin{displaymath}\n"

    if variable:
        output += f"{variable} ="

    output += pmatrix(matrix)

    output += "\\end{displaymath}\n"

    return output

def pmatrix(matrix):
    output = "\\begin{pmatrix}"

    for y in matrix:
        count = 0
        for x in y:
            count += 1
            if count < len(y):
                output += str(x) + " && "
                continue
            output += str(x) + " \\\\"

    output += "\\end{pmatrix}"

    return output

def pmatrix_surds(matrix):

    output = "\\begin{pmatrix}"

    for y in matrix:
        count = 0
        for x in y:
            count += 1

            if count < len(y):
                output += str(x[0][0]) + "\\sqrt{" + str(x[0][1]) + "} && "
                continue
            output += str(x[0][0]) + "\\sqrt{" + str(x[0][1]) + "} \\\\"

    output += "\\end{pmatrix}"

    return output