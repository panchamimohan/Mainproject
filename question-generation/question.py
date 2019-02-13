
from question_generator import QuestionGenerator



def makequestion(input_val):
    q  = QuestionGenerator()
    question_list = q.generate_question(input_val, ['Wh', 'Are', 'Who', 'Do'])
    return question_list
