import random
from collections import deque

from src.domain.Quiz import Quiz


class InexistentFileException(Exception):
    pass


class NoFileException(Exception):
    pass


class QuizController():
    def __init__(self, repository):
        self.__repository = repository


    def get_all(self):
        return self.__repository.get_all()

    def compute_score(self, answers):
        """
        :param answers: a dictionary containing the correct and incorrect answers of the person
        :return: the score of the person and the total points that could have been obtained
        """"""
        """
        score = 0
        points = {'easy':1, 'medium':2, 'hard':3}
        for answer in answers['solved']:
            score += points[answer]
        total = score
        for answer in answers['incorrect']:
            total += points[answer]
        return score, total

    def start_quiz(self, file_name):
        answers = {
            'solved': [],
            'incorrect': []
        }
        try:
            with open(file_name, 'r') as f:
                for line in f.read().splitlines():
                    line = Quiz.create_quiz_from_csv(line)
                    while True:
                        print(str(line.question), '\n', str(line.answer1), '\n', str(line.answer2), '\n',
                              str(line.answer3),
                              '\n', str(line.difficulty_level), '\n')
                        # prints the data for the currect question
                        answer = input("> ")

                        if answer in [line.answer1, line.answer2, line.answer3]:
                            if answer == str(line.correct_answer):
                                answers['solved'].append(str(line.difficulty_level))
                                break
                            else:
                                answers['incorrect'].append(str(line.difficulty_level))
                                break
                        else:
                            print("Please provide one of the available answers (one is correct for sure :) .\n)")
                return self.compute_score(answers)
        except IOError:
            raise NoFileException("File with name {} not found.".format(file_name))


    def add_quiz(self, args):
        args = args.strip().split(",")
        if self.valid_add(args):
            quiz = Quiz(int(args[0]), args[1], args[2], args[3], args[4], args[5], args[6])
            self.__repository.add_quiz(quiz)
        else:
            raise Exception("Invalid parametizing!")

    def count_difficulty(self, difficulty):
        counter = 0
        for quiz in self.get_all():
            if quiz.difficulty_level == difficulty:
                counter += 1
        return counter


    def give_lists(self):
        """"
        function to return three lists containing the quesions of each type
        """
        hard = []
        easy = []
        medium = []
        for question in self.get_all():
            if question.difficulty_level == "easy":
                easy.append(question)
            elif question.difficulty_level == "medium":
                medium.append(question)
            else:
                hard.append(question)
        return easy,medium,hard


    def create_quiz(self, args):
        #args = args.split(" ")
        print(args, "args")
        if not self.valid_create(args):
            raise Exception("Arguments not passed correctly...")
        else:
            try:
                file = args[2]
                difficulty = args[0]
                number_qst = int(args[1])
                easy, medium, hard = self.give_lists()
                if args[0] == "easy":
                    if len(easy) < number_qst//2:
                        raise Exception("Can't make easy quiz, too few easy questions...")
                    else:
                        if len(easy) >= number_qst // 2:
                            """"if we have more easy questions than expected"""
                            ll = deque()
                            ll.extend(random.sample(
                                filter([lambda value: x for x in self.get_all() if x.difficulty_level == args[0]],
                                       self.get_all())), number_qst // 2)
                            # now we have the list with easy questions for half of the quiz
                            remained = len(self.get_all()) - number_qst // 2
                            ll.extend(random.sample(
                                filter([lambda value: x for x in self.get_all() if x not in ll], self.get_all())),
                                      remained)
                            """"now we have the entire list, completed with quizes, all we need to do is return it to a main function to add it to the file"""
                            self.add_quiz_to_new_file(ll, file)
                            return
                elif args[0] == "medium":
                    if len(medium) < number_qst//2:
                        raise Exception("Can't make medium quiz, too few easy questions...")
                    else:
                        if len(medium) >= number_qst // 2:
                            """"if we have more easy questions than expected"""
                            ll = deque()
                            ll.extend(random.sample(
                                filter([lambda value: x for x in self.get_all() if x.difficulty_level == args[0]],
                                       self.get_all())), number_qst // 2)
                            # now we have the list with easy questions for half of the quiz
                            remained = len(self.get_all()) - number_qst // 2
                            ll.extend(random.sample(
                                filter([lambda value: x for x in self.get_all() if x not in ll], self.get_all())),
                                      remained)
                            """"now we have the entire list, completed with quizes, all we need to do is return it to a main function to add it to the file"""
                            self.add_quiz_to_new_file(ll, file)
                            return
                elif args[0] == "hard":
                    if len(medium) < number_qst // 2:
                        raise Exception("Can't make hard quiz, too few easy questions...")
                    else:
                        if len(easy) >= number_qst // 2:
                            """"if we have more easy questions than expected"""
                            ll = deque()
                            ll.extend(random.sample(
                                filter([lambda value: x for x in self.get_all() if x.difficulty_level == args[0]],
                                       self.get_all())), number_qst // 2)
                            # now we have the list with easy questions for half of the quiz
                            remained = len(self.get_all()) - number_qst // 2
                            ll.extend(random.sample(
                                filter([lambda value: x for x in self.get_all() if x not in ll], self.get_all())),
                                      remained)
                            """"now we have the entire list, completed with quizes, all we need to do is return it to a main function to add it to the file"""
                            self.add_quiz_to_new_file(ll, file)
                            return
                else:
                    raise Exception("Invalid input...")
            except Exception:
                raise ValueError("Cannot create quiz. Error occured...")

    def add_quiz_to_new_file(self, quiz_list, file_name):
        try:
            with open(file_name, "w") as f:
                for quiz in quiz_list:
                    line = Quiz.create_csv_from_quiz(quiz)
                    f.write(line)
                    f.write("\n")
        except IOError:
            raise InexistentFileException("File provided doesn't exist!")

    def save(self):
        self.__repository.save_repository()

    @staticmethod
    def valid_create(args):
        if len(args) < 3:
            return False
        if args[0] not in ["easy", "medium", "hard"]:
            return False
        #if not isinstance(int, int(args[1])):
         #   return False
        return True

    @staticmethod
    def valid_add(args):
        if len(args) < 7:
            return False
        elif args[5] not in [args[3], args[4], args[2]]:
            return False
        elif args[6] not in ["easy", "medium", "hard"]:
            return False
        return True