# -*- coding: utf-8 -*-
from exercises import Exercises
from colorsStatus import ColorsStatus
# for anothers implements [comming soon]
# import os


class Imterface:
    switchOnOff = True
    exercises = Exercises()

    def division(self):
        print('-' * 120)

    def initFun(self):
        print(ColorsStatus.OKBLUE +
              '\nHello, this is a new interface in terminal'
              + ColorsStatus.ENDC
              )
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
        msg = 'are you wish finish the operation?: [Yes: Y] [No: N]\n'
        value = str(input(msg))
        self.division()

        if value == 'Y':
            self.switchOnOff = False
            self.msgExit()

    def msgExit(self):
        print(ColorsStatus.OKGREEN + 'Exit, bye user ;3\n' + ColorsStatus.ENDC)


interface = Imterface()

while(interface.switchOnOff):
    try:
        interface.initFun()
        interface.switchEx()
        interface.offClass()
    except KeyboardInterrupt:
        interface.division()
        interface.msgExit()
        exit()
    except TypeError:
        interface.division()
        msg = 'type of error when try input an string or number in your expected'
        print(ColorsStatus.WARNING + msg + ColorsStatus.ENDC)
    except ValueError:
        interface.division()
        msg = 'type of error when try input an string or number in your expected'
        print(ColorsStatus.WARNING + msg + ColorsStatus.ENDC)
