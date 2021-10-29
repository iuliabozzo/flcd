from controller.controller import *


class Main:
    def __init__(self):
        self.controller = Controller("p2.txt")


main = Main()
main.controller.run()
