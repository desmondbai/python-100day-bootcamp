#ask user the question
#check if answer is correct
#check if user's at the end of the quiz


## Attributes:
    #question_number
    #question_list

## Methods:
    #next_question

from question_model import Question


class QuizBrain():
    def __init__(self,qa_list:list):
        self.question_number = 1
        self.question_list = qa_list
        self.user_score = 0
    
    def still_has_question(self):
        """
        Check existence of remaining questions in the question bank
        """
        return self.question_number <= len(self.question_list)
        


    def ask_question(self):
        """
        1. Ask user input for current question;
        2. Compare user answer against correct answer
        3. Increment question number
        """
        question = self.question_list[self.question_number - 1]
        user_answer = input(f"Q.{self.question_number}.{question.text}, (True or False) ? ")
        self.check_answer(user_answer,question.answer)
        self.question_number += 1
        
        
    

    def check_answer(self,user_answer,system_answer):
        """
        Check if the answer user put in is correct, all lower-cased
        """
        if user_answer == system_answer:
            print("Bingo, you are correct!")
            self.user_score += 1
        else:
            print("Sorry you got it wrong")
            print(f"The correct answer was:{system_answer}")

        
    



    
     
        
    

