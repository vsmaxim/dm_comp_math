from naturals import Natural

class Integer(Natural):
    def __init__(self, digits):
        '''Конструктор целого числа, Васильев Максим'''
        self.negative = digits[0] == '-'
        if self.negative:
            digits = digits[1:]
        self.digits = [int(i) for i in reversed(digits)]
   
    def __str__(self):
        '''Представление целого числа в строке, Васильев Максим'''
        s = ''
        if self.isZero():
            return '0'
        if self.negative:
            s = '-'
        return s + ''.join(str(i) for i in reversed(self.digits))

    def __neg__(self):
        '''MUL_ZM_Z Умножение целого на -1, Васильев Максим'''
        a = Integer(str(self))
        a.negative = not a.negative
        return a

    def abs(self):
        '''ABS_Z_N Абсолютная величина числа, Васильев Максим''' 
        res = Integer('0')
        res.digits = self.digits
        res.negative = False
        return res
    
    def isZero(self):
        '''Проверка целого числа на ноль, Васильев Максим'''
        for i in range(len(self.digits)):
            if self.digits[i]:
                return False
        return True

    def __pow__(self, oth):
        '''Возведение целого числа в степень, Васильев Максим'''
        a = Natural(str(self.abs()))
        b = Natural(str(oth.abs()))
        res = Integer(str(a ** b))
        if self.negative and (b % Natural('2') == Natural('1')):
            res.negative = self.negative
        return res 

    def positivity(self):
        '''POZ_Z_D Определение положительности числа, Васильев Максим'''
        if isZero(self):
            return 0
        elif self.negative:
            return -1
        else:
            return 1
                
    def ton(self):
        '''Преобразование Integer->Natural, Васильев Максим'''
        return Natural(str(self.abs()))

    def __add__(self, oth):
        '''Сложение двух целых чисел, Васильев Максим'''
        result = Integer('0')
        a = self.ton()
        b = oth.ton()
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
            
    def __sub__(self, oth):
        '''Вычитание двух целых чисел, Васильев Максим'''
        return self + -oth

    def __mul__(self, oth):
        '''Умножение двух целых чисел, Васильев Максим'''
        a = self.ton()
        b = oth.ton()
        result = Integer(str(a * b))
        result.negative = self.negative != oth.negative
        return result
    
    def div(self, oth):
        '''Деление, возвращающее остаток и целую часть, Васильев Максим'''
        a = self.ton()
        b = oth.ton()
        res = a.div(b)
        for i in range(len(res)):
            res[i] = Integer(str(res[i]))
            res[i].negative = self.negative != oth.negative
        return res

    def __mod__(self, oth):
        '''Перегрузка операции %, остаток от деления'''
        res = self.div(oth)[1]
        if res.negative:
            res = res + oth.abs()
        return res           


    def __div__(self, oth):
        '''Перегрузка операции //, целая часть от деления'''
        return self.div(oth)[0]
            
#Для тестов
if __name__ == '__main__':
    a = Integer('-100')
    b = Integer('7')
    print(a ** b)