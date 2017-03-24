from integer import Integer
from naturals import Natural

class Rational:
    def __init__(self, str):
        '''Конструктор рационального числа, Васильев Максим'''
        a = str.split('/')
        self.numer = Integer(a[0])
        self.denom = Natural(a[1])
    
    def __str__(self):
        '''Строковое представление рационального числа, Васильев Максим'''
        return '{}/{}'.format(self.numer, self.denom)

    def __neg__(self):
        a = Rational(str(self))
        a.numer = -a.numer
        return a
    
    def __add__(self,oth):
        '''Сложение рациональных чисел, Гусева Екатерина'''
        a = Rational(str(self))
        b = Rational(str(oth))
        n_den = a.denom.lcm(b.denom)
        a_k = n_den // a.denom #Коэффицент на который домножаем первый числитель
        b_k = n_den // b.denom #Коэффициент на который домножжаем второй числитель
        n_num = a.numer * Integer(str(a_k)) + b.numer * Integer(str(b_k))
        return Rational(str(n_num) + '/' + str(n_den))

    
    def __sub__(self, oth):
        '''Вычитание рациональных чисел, Васильев Максим'''
        return self + -oth

    def isInteger(self):
        '''Проверка, является ли дробь - целым, Васильев Максим'''
        if (self.numer.ton() % self.denom).isZero():
            return True
        return False

    def red(self):
        '''Сокращение дроби, Гусева Екатерина'''
        num = self.numer.ton()
        den = self.denom
        gcd = num.gcd(den)
        self.numer.digits = (num // gcd).digits
        self.denom = den // gcd
        return self

    def toi(self):
        '''Преорбразование в целое рационального, Васильев Максим'''
        if self.denom == Natural('1'):
            return Integer(str(self.numer))

if __name__ == '__main__':
    a = Rational('1/3')
    b = Rational('1/4')
    print(a + b)