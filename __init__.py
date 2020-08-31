import os, subprocess
import getopt
import sys
import sympy

import question_types.determinant
import question_types.char_polynomial
import question_types.dot_product
import question_types.determinant_with_variable

import question_types.text_based.dot_product

OUTPUT_DIR = "output"

sympy.init_printing()

class exam_generator:
    questions = []

    def __init__(self):
        pass

    def addQuestion(self, question):
        self.questions.append(question)

    def generateQuestions(self):
        generated = "\\begin{questions}"

        for question in self.questions:
            generated += question[0]

        generated += "\\end{questions}"

        return generated


if __name__ == '__main__':
    argv = sys.argv[1:]

    opts, args = getopt.getopt(argv, 'vhs', ['gradetable'])

    gradetable = False
    for (arg, mod) in opts:
        if arg == '--gradetable':
            gradetable = True


    print('Starting exam generation')

    generator = exam_generator()

    print('Generating questions')

    #generator.addQuestion(question_types.char_polynomial.generate_question())
    generator.addQuestion(question_types.determinant.generate_question())
    generator.addQuestion(question_types.dot_product.generate_question())
    generator.addQuestion(question_types.determinant_with_variable.generate_question())

    # Text based questions
    # TODO: Randomize text based questions
    generator.addQuestion(question_types.text_based.dot_product.generate_question())

    print('Questions generated')
    with open("template_questions.tex", 'r') as file:
        print('Generating latex documents')
        template = file.read()
        template = template.replace("{{QUESTIONS}}", generator.generateQuestions())

        if gradetable:
            template = template.replace("{{AFTER_INSTRUCTIONS}}", "\\begin{center}\\gradetable[h]\\end{center}\\vspace{0.2in}{{AFTER_INSTRUCTIONS}}")


        template = template.replace("{{AFTER_INSTRUCTIONS}}", "")

        without_answers = template.replace("{{PREAMBLE}}", "")
        with_answers = template.replace("{{PREAMBLE}}", "\\printanswers")

        without_answers_output_file_path = f"{OUTPUT_DIR}/generated.tex"
        with_answers_output_file_path = f"{OUTPUT_DIR}/generated_answers.tex"

        with open(with_answers_output_file_path, 'w') as output_file:
            output_file.write(with_answers)
        with open(without_answers_output_file_path, 'w') as output_file:
            output_file.write(without_answers)

    print('Generating PDFs')

    compile_count = 1

    if (gradetable):
        compile_count = 2

    for i in range(compile_count):
        subprocess.run(['pdflatex', '-output-directory=output', without_answers_output_file_path])
        subprocess.run(['pdflatex', '-output-directory=output', with_answers_output_file_path])
