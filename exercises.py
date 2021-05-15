# -*- coding: utf-8 -*-
from math import sqrt
from colorsStatus import ColorsStatus


class Exercises:

    def division(self):
        print('-' * 120)

    # first exercise
    def getMsg(self, number):
        self.msg1 = '{:x}. Digit number: '.format(number)

    def setterValsEx1(self, *ex1Param):
        self.a = ex1Param[0]
        self.b = ex1Param[1]
        self.c = ex1Param[2]

    def secondGradeEx(self):
        # ax^2 + bx + c = 0
        # x = (-b [+/-] raiz(b^2-4ac)) / (2*a)
        isError = False
        try:
            div = (2 * self.a)
            sqrtCurrent = sqrt(self.b**2 - 4 * self.a * self.c)
            xInMinor = (-self.b - sqrtCurrent) / div
            xInMajor = (-self.b + sqrtCurrent) / div

            self.division()
            if (xInMajor and xInMinor) == 0:
                return print('response: x=%4.3f' % xInMajor)
            return print('response: xInMajor=%4.3f and xInMinor=%4.3f' % (xInMajor, xInMinor))
        except ZeroDivisionError:
            isError = True
            msg = 'in operation, you input value 1 like \'0\' and the operation has not resolve the division by zero'
            print(ColorsStatus.WARNING + msg + ColorsStatus.ENDC)
        except ValueError:
            isError = True
            msg = 'the operation is was division or mult any zero, and response with this error or strings when expected any type of number'
            print(ColorsStatus.WARNING + msg + ColorsStatus.ENDC)
        finally:
            if not isError:
                return
            self.ex1()

    def ex1(self):
        numbers = []
        for x in range(3):
            self.getMsg(x + 1)
            self.division()
            numbers.append(float(input(self.msg1)))

        self.setterValsEx1(*numbers)
        self.secondGradeEx()

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
