from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank) #have to define variable!
thequestion = quiz.next_question()
completedthequiz = quiz.completed_quiz()

#print(question_bank[0].answer)

# question_bank = Question(question_data[1].keys(), question_data[2].keys())
# print(question_bank)
# print(question_data[1].values())
# print(question_data[1].items())

# key, val = question_data[1].items()

# print(key)
# print(val)


# def set_variables():
#     for k, v, in question_data[1].items():
#         variable1 = None
#         variable1 = v
#         if variable1 != None:
#             variable2 = v
#         print(variable1)


# set_variables()

