# -*- coding: utf-8 -*-
from exercises import Exercises
# for anothers implements [comming soon]
# import os


class Imterface:
    switchOnOff = True
    exercises = Exercises()

    def division(self):
        print('-' * 120)

    def initFun(self):
        print('\nHello, this is a new interface in terminal')
        text = ''
        for x in range(7):
            text += '[{:x}] exercise\n'.format(x + 1)
        self.division()
        print(text)

    def switchEx(self):
        val = int(input('what is the exercise that you with resolve?:\n'))
        switcher = {
            1: self.exercises.ex1,
            2: self.exercises.ex2,
            3: self.exercises.ex3,
            4: self.exercises.ex4,
            5: self.exercises.ex5,
            6: self.exercises.ex6,
            7: self.exercises.ex7,
        }

        switcher.get(val, 'Invalid exercise!')()
        self.division()

    def offClass(self):
        msg = 'Deseas terminar la operación: [Si: S] [No: N]\n'
        value = str(input(msg))
        self.division()

        if value == 'S':
            self.switchOnOff = False


interface = Imterface()

while(interface.switchOnOff):
    interface.initFun()
    interface.switchEx()
    interface.offClass()
