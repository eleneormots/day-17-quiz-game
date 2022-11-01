from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
def play():
    question_bank=[]
    for question in question_data:
        new_question = Question(question.get("text"), question.get("answer"))
        question_bank.append(new_question)
    quiz=QuizBrain(question_bank)

    while quiz.still_has_qeestions():
        quiz.next_question()
    print("You've completed quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")



def main():
    play()

if __name__ == "__main__":
    main()