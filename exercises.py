# -*- coding: utf-8 -*-
from math import sqrt
from colorsStatus import ColorsStatus


class Exercises:
    # dictionary of code morse
    dic = {
        'a': '•\u2013',
        'b': '\u2013•••',
        'c': '\u2013•\u2013•',
        'd': '\u2013••',
        'e': '•',
        'f': '••\u2013•',
        'g': '\u2013\u2013•',
        'h': '••••',
        'i': '••',
        'j': '•\u2013\u2013\u2013',
        'k': '\u2013•\u2013',
        'l': '•\u2013••',
        'm': '\u2013\u2013',
        'n': '\u2013•',
        'ñ': '\u2013\u2013•\u2013\u2013',
        'o': '\u2013\u2013\u2013',
        'p': '•\u2013\u2013•',
        'q': '\u2013\u2013•\u2013\u2013',
        'r': '•\u2013•',
        's': '•••',
        't': '\u2013',
        'u': '••\u2013',
        'v': '•••\u2013',
        'w': '•\u2013\u2013',
        'x': '\u2013••\u2013',
        'y': '\u2013•\u2013\u2013',
        'z': '\u2013\u2013••',
    }

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
                return print(ColorsStatus.OKGREEN + 'response: x=%4.3f' % xInMajor + ColorsStatus.ENDC)
            return print(ColorsStatus.OKGREEN + 'response: xInMajor=%4.3f and xInMinor=%4.3f' % (xInMajor, xInMinor) + ColorsStatus.ENDC)
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
    def formatTextGetter(self, text):
        return str(text).lower().replace(' ', '')

    def ex2(self):
        msg = 'Digit your palindrome:\n'

        self.division()
        newText = str(self.formatTextGetter(input(msg)))
        inverseText = newText[::-1]
        if newText == inverseText:
            msg = 'the text is palindrome: [compare]'
            print(ColorsStatus.OKGREEN + msg + ColorsStatus.ENDC)
            print('text before:',
                  ColorsStatus.OKGREEN + newText + ColorsStatus.ENDC)
            print('text after:',
                  ColorsStatus.OKGREEN + inverseText + ColorsStatus.ENDC)
            return
        msg = 'the text isn\'t a palindrome: [compare]'
        print(msg)
        print('text before:',
              ColorsStatus.FAIL + newText + ColorsStatus.ENDC)
        print('text after:',
              ColorsStatus.FAIL + inverseText + ColorsStatus.ENDC)

    # thercy exercise
    def ex3(self):
        numbers = {}
        for x in range(10):
            x += 1
            numbers.setdefault(x, x**2)
        self.division()
        print(numbers)

    # quanty exercise

    def ex4(self):
        self.division()
        val = str(input('digit the text for transform in code morse:\n'))
        finalVal = ''
        for x in range(val.__len__()):
            finalVal += self.dic[val[x]]
        print(finalVal)

    # fifty exercise
    def ex5(self):
        key1 = {'pass': 1234}
        key2 = {'pass': 4321}
        x = 1

        self.division()
        print('[1]: key1 || [2]: key2\n')
        op = int(input('Digit the option that you wish: '))
        if op == 1:
            op2 = int(input(
                '\nAre you wish know the key1 or add other to object? [1]: add || [2]: know\n'))
            if op2 == 1:
                val = str(input('digit the value: '))
                key1.setdefault('pass{:x}'.format(x), val)
                x += 1
                print(ColorsStatus.OKGREEN + key1 + ColorsStatus.ENDC)
            else:
                print(ColorsStatus.OKGREEN + key1 + ColorsStatus.ENDC)
        else:
            op2 = int(input(
                '\nAre you wish know the key2 or add other to object? [1]: add || [2]: know\n'))
            if op2 == 1:
                val = str(input('digit the value: '))
                key2.setdefault('pass{:x}'.format(x), val)
                x += 1
                print(ColorsStatus.OKGREEN + key2 + ColorsStatus.ENDC)
            else:
                print(ColorsStatus.OKGREEN + key2 + ColorsStatus.ENDC)

    # sexty exercise
    def ex6(self):
        notPrimes = []
        msgTrue = '\nThis number is prime, is divisible between 1 and her self'
        msgFalse1 = '\nThis number hasn\'t prime because is divisible more than 1 and her self'
        msgFalse2 = 'Numbers that is divisible:'
        valToDiv = 1
        steps = 0

        self.division()
        N = int(input('Digit the value that you wish know if it is a number prime:\n'))

        while valToDiv <= N:
            result = N % valToDiv
            valToDiv += 1

            if result == 0:
                steps += 1
                continue
            notPrimes.append(valToDiv)

        if steps == 2:
            return print(ColorsStatus.OKGREEN + msgTrue + ColorsStatus.ENDC)

        print(ColorsStatus.FAIL + msgFalse1 + ColorsStatus.ENDC)
        print(ColorsStatus.FAIL + msgFalse2 + ColorsStatus.ENDC)
        return print(ColorsStatus.FAIL + notPrimes.__str__() + ColorsStatus.ENDC)

    # seventy exercise
    def ex7(self):
        print('ex7')
        pass
