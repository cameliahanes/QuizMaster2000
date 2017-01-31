starting_display = ' '*27 + "===  QUIZ MASTER 2000  ===" + '\n' +\
                   ' '*10 + "add <id>,<question>,<first_answer>,<second_answer>,<third answer>, <correct_ansswer>,<difficulty_level>" + '\n'+\
    ' '*10 + "create <difficulty_level> <number_of_questions> <file_name>" + '\n' +\
    ' '*10 + "start <file_name> "+'\n' +\
    ' '*10 + "exit" + '\n'

class ConsoleUI():
    def __init__(self, controller):
        self.__controller = controller


    def run(self):
        while True:
            print(starting_display)
            command = input("Enter command: ")
            if command == "exit":
                self.__controller.save()
                print("Thank you for using QuizMaster!")
                break
            command = command.split(" ")
            cmd = command[0].strip()
            args = command[1].strip()
            if cmd == "add":
                self.__controller.add_quiz(args)
            elif cmd == "create":
                args = command[1:]
                #args = str(args).split(" ")
                self.__controller.create_quiz(args)
            elif str(cmd) == "display" and str(args) == "all":
                for q in self.__controller.get_all():
                    print(q)
            elif str(cmd) == "start" and str(args) != None:
                score, total = self.__controller.start_quiz(str(args).strip())
                print("Yu obtained {} from {} points. \n".format(score, total))
            else:
                print("Unknown command...")

