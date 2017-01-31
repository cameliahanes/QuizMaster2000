from collections import deque

from src.domain.Quiz import Quiz


class QuizRepository():
    def __init__(self):
        self.__quizes = deque()
        self.load_from_file()

    def load_from_file(self):
        with open("quizes.txt", "r") as f:
            for q in f.read().splitlines():
                quizz = Quiz.create_quiz_from_csv(q.strip())
                self.__quizes.append(quizz)

    def get_all(self):
        return self.__quizes

    def add_quiz(self, quiz):
        if quiz in self.__quizes:
            raise Exception("Question already in database!")
        self.__quizes.append(quiz)

    def save_repository(self):
        with open("quizes.txt", "w") as f:
            for quiz in self.__quizes:
                line = Quiz.create_csv_from_quiz(quiz)
                f.write(line)
                f.write('\n')