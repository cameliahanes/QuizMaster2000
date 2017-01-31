from src.console.QuizConsole import ConsoleUI
from src.controller.QuizController import QuizController
from src.repository.QuizRepository import QuizRepository

repository = QuizRepository()
controller = QuizController(repository)
console = ConsoleUI(controller)

if __name__ == '__main__':
    console.run()