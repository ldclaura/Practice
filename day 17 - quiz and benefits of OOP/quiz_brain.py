#TODO: asking the questions
#TODO: checking if the answer was correct 
#TODO: checking if we're at the end of the quiz

class QuizBrain:
    current_score = 0
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_score = 0
    def next_question(self):
        play_game = True
        while play_game == True:
            try:
                current_question = self.question_list[self.question_number]
                self.question_number += 1
                yourinput = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").capitalize()
                
                
                if yourinput == current_question.answer:
                    print("You got it right!")
                    self.current_score += 1
                else:
                    print("WRONG")
                
                print(f"The correct answer was: {current_question.answer}.")
                print(f"Your current score is: {self.current_score}/{self.question_number}.")
            except:
                IndexError
                break
    def completed_quiz(self):
        print(f"---------------------------------------")
        print("You've completed the quiz")
        print(f"Your final score was: {self.current_score}/{self.question_number}.")




        

# class QuizBrain:
#     def __init__(self, question_number, questions_list):
#         self.question_number = 0
#         self.questions_list = questions_list
#     def next_question(self, question_number, questions_list):
#         self.question_number = question_number
#         question_number += 1
#         return question_number
#     thenextquestion = next_question(question_number)
        # print(questions_list[0].answer)

    #attributes:
    #  question_number = 0 (default value 0)
    #questions_list
    #methods
    #next_question()
    #----
    #Q.1: a slug's blood is green. (True/False)?:
    