# -*- coding: utf-8 -*-

class Exercise1:
    switchOnOff = True

    def division(self):
        print('-' * 120)

    # first exercise
    def getFistEx(self, *ex1Param):
        print(ex1Param)
        pass

    def ex1(self):
        self.getFistEx(1, 2, 3)
        pass

    # second exercise
    def ex2(self):
        print('ex2')
        pass

    # thercy exercise
    def ex3(self):
        print('ex3')
        pass

    # quanty exercise
    def ex4(self):
        print('ex4')
        pass

    # fifty exercise
    def ex5(self):
        print('ex5')
        pass

    # sexty exercise
    def ex6(self):
        print('ex6')
        pass

    # seventy exercise
    def ex7(self):
        print('ex7')
        pass

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
            1: self.ex1,
            2: self.ex2,
            3: self.ex3,
            4: self.ex4,
            5: self.ex5,
            6: self.ex6,
            7: self.ex7,
        }

        switcher.get(val, 'Invalid exercise!')()
        self.division()

    def offClass(self):
        msg = 'Deseas terminar la operación: [Si: S] [No: N]\n'
        value = str(input(msg))
        self.division()

        if value == 'S':
            self.switchOnOff = False


exercise = Exercise1()

while(exercise.switchOnOff):
    exercise.initFun()
    exercise.switchEx()
    exercise.offClass()
