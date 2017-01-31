class Quiz():
    def __init__(self, id, question, a1, a2, a3, correct_a, dif_level):
        self.__id = id
        self.__question = question
        self.__answer1 = a1
        self.__answer2 = a2
        self.__answer3 = a3
        self.__correct_answer = correct_a
        self.__difficulty_level = dif_level

    @property
    def question(self):
        return self.__question

    @property
    def correct_answer(self):
        return self.__correct_answer

    @property
    def id(self):
        return self.__id

    @property
    def answer1(self):
        return self.__answer1

    @property
    def answer2(self):
        return self.__answer2

    @property
    def answer3(self):
        return self.__answer3

    @property
    def difficulty_level(self):
        return self.__difficulty_level

    def __eq__(self, other):
        if other == None or not isinstance(other, Quiz):
            return False
        return self.__question == other.question

    def __str__(self):
        return ("{} | {} | {} | {} | {} | {} | {} ".format(self.__id, self.__question, self.__answer1, self.__answer2, self.__answer3, self.__correct_answer, self.__difficulty_level))

    @staticmethod
    def create_quiz_from_csv(line):
        line = line.split(',')
        q = Quiz(int(line[0]), line[1], line[2], line[3], line[4], line[5], line[6])
        return q

    @staticmethod
    def create_csv_from_quiz(quiz):
        s = str(quiz.id) + ","+str(quiz.question)+","+str(quiz.answer1)+","+str(quiz.answer2)+","+str(quiz.answer3)+\
            ","+str(quiz.correct_answer)+","+str(quiz.difficulty_level)
        return s