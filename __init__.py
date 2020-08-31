import question_types.determinant
import question_types.char_polynomial
import question_types.dot_product

OUTPUT_DIR = "output"

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

    def generateAnswers(self):
        generated = "\\begin{questions}"

        for question in self.questions:
            generated += question[1]

        generated += "\\end{questions}"

        return generated


if __name__ == '__main__':
    generator = exam_generator()

    generator.addQuestion(question_types.char_polynomial.generate_question())
    generator.addQuestion(question_types.determinant.generate_question())
    generator.addQuestion(question_types.dot_product.generate_question())


    with open("template.tex", 'r') as file:
        template = file.read()
        template = template.replace("{{QUESTIONS}}", generator.generateQuestions())

        output_file_path = f"{OUTPUT_DIR}/generated.tex"

        with open(output_file_path, 'w') as output_file:
            output_file.write(template)
