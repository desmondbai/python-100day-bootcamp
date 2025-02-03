from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import requests
import json



#Ask user how many question to put into the quiz bank
n_questions = int(input("Hello there, how many quizzes you would like to answer today?"))


opentdb_result = requests.get(f"https://opentdb.com/api.php?amount={n_questions}&type=boolean").content

opentdb_result = json.loads(opentdb_result)

questions = [Question(qa_element["question"],qa_element["correct_answer"]) for qa_element in opentdb_result["results"]]



quiz_brain = QuizBrain(questions)


while quiz_brain.still_has_question():
    quiz_brain.ask_question()
    


print(f"That's the end of the quiz, your total score is {quiz_brain.user_score}")