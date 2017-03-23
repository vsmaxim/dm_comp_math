from naturals import Natural

class Integer(Natural):
    def __init__(self, digits):
        self.negative = digits[0] == '-'
        if self.negative:
            digits = digits[1:]
        self.digits = [int(i) for i in reversed(digits)]
    def __str__(self):
        s = ''
        if self.isZero():
            return '0'
        if self.negative:
            s = '-'
        return s + ''.join(str(i) for i in reversed(self.digits))
    def __neg__(self):
        '''MUL_ZM_Z Умножение целого на -1, Васильев Максим'''
        self.negative = not self.negative
        return self

    def abs(self):
        '''ABS_Z_N Абсолютная величина числа, Васильев Максим''' 
        res = Integer('0')
        res.digits = self.digits
        res.negative = False
        return res
    
    def isZero(self):
        for i in range(len(self.digits)):
            if self.digits[i]:
                return False
        return True


    def positivity(self):
        '''POZ_Z_D Определение положительности числа, Васильев Максим'''
        if isZero(self):
            return 0
        elif self.negative:
            return -1
        else:
            return 1
    def ton(self):
        return Natural(''.join(str(i) for i in self.digits))

    def __add__(self, oth):
        result = Integer('0')
        a = Natural(str(self.abs()))
        b = Natural(str(oth.abs()))
        if self.negative == oth.negative:
            result = Integer(str(a + b))
            result.negative = self.negative
        else:
            result = Integer(str(a - b))
            if (a < b):
                result.negative = oth.negative
            else:
                result.negative = self.negative
        return result
            
            
#Для тестов
if __name__ == '__main__':
    a = Integer('1233')
    b = Integer('-1233')
    print(a + b)