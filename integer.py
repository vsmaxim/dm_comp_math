from naturals import Natural

class Integer(Natural):
    def __init__(self, digits):
        self.negative = digits[0] == '-'
        if self.negative:
            digits = digits[1:]
        self.digits = [int(i) for i in reversed(digits)]
    def __str__(self):
        s = ''
        if self.negative:
            s = '-'
        return s + ''.join(str(i) for i in reversed(self.digits))
    def __neg__(self):
        '''MUL_ZM_Z Умножение целого на -1, Васильев Максим'''
        self.negative = not self.negative
        return self
    def abs(integer):
        '''ABS_Z_N Абсолютная величина числа, Васильев Максим''' 
        return Natural(''.join(str(i) for i in reversed(integer.digits)))
    def positivity(self):
        '''POZ_Z_D Определение положительности числа, Васильев Максим'''
        if isZero(self):
            return 0
        elif self.negative:
            return -1
        else:
            return 1
    def ntoi(self):
        pass
    def iton(self):
        pass
#Для тестов
if __name__ == '__main__':
    a = Integer('-1233')