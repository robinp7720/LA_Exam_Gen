import os, subprocess
import sympy

import question_types.determinant
import question_types.char_polynomial
import question_types.dot_product

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
    print('Starting exam generation')

    generator = exam_generator()

    print('Generating questions')
    generator.addQuestion(question_types.char_polynomial.generate_question())
    generator.addQuestion(question_types.determinant.generate_question())
    generator.addQuestion(question_types.dot_product.generate_question())

    print('Questions generated')
    with open("template_questions.tex", 'r') as file:
        print('Generating latex documents')
        template = file.read()
        template = template.replace("{{QUESTIONS}}", generator.generateQuestions())

        without_answers = template.replace("{{PREAMBLE}}", "")
        with_answers = template.replace("{{PREAMBLE}}", "\\printanswers")

        without_answers_output_file_path = f"{OUTPUT_DIR}/generated.tex"
        with_answers_output_file_path = f"{OUTPUT_DIR}/generated_answers.tex"

        with open(with_answers_output_file_path, 'w') as output_file:
            output_file.write(with_answers)
        with open(without_answers_output_file_path, 'w') as output_file:
            output_file.write(without_answers)

    print('Generating PDFs')

    subprocess.run(['pdflatex', '-output-directory=output', without_answers_output_file_path])
    subprocess.run(['pdflatex', '-output-directory=output', with_answers_output_file_path])
