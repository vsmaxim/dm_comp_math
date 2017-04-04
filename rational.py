from integer import Integer
from naturals import Natural


def contForm(stri):
    '''Возвращает непрерывную дробь в виде [x; x1, x2...], Васильев Максим'''
    strf = stri.split()
    res = ''
    for i in range(len(strf)):
        res = res + strf[i]
        if i == 0:
            res += '; '
        elif i != len(strf) - 1:
            res += ', '
    return '[' + res + ']'


class Rational:
    def __init__(self, str):
        '''Конструктор рационального числа, Васильев Максим'''
        # self.numer - хранит числитель (numerator), self.denom
        # хранит знаменатель (denominant), числа вводятся в виде
        # num/den
        a = str.split('/')
        self.numer = Integer(a[0])
        self.denom = Natural(a[1])

    def __str__(self):
        '''Строковое представление рационального числа, Васильев Максим'''
        # Возвращает строку вида 'num/den'
        return '{}/{}'.format(self.numer, self.denom)

    def __neg__(self):
        '''Умножение дроби на -1, Васильев Максим'''
        # Меняем знак на противоположный у числителя
        a = Rational(str(self))
        a.numer = -a.numer
        # Возвращаем <object Rational>
        return a

    def __gt__(self, oth):
        '''Сравнение двух дробей, Васильев Максим'''
        # Смотрим на знак разности двух дробей, если
        # отрицательный, то дробь больше, иначе меньше
        return (oth - self).numer.negative

    def isZero(self):
        '''Проверка дроби на ноль, Васильев Максим'''
        # Проверяем знаменатель на ноль, уже имеющимся методом
        return self.numer.isZero()

    def __add__(self, oth):
        '''Сложение рациональных чисел, Гусева Екатерина'''
        a = Rational(str(self))
        b = Rational(str(oth))
        # n_den - НОК знаменателей
        n_den = a.denom.lcm(b.denom)
        # Коэффицент на который домножаем первый числитель
        a_k = n_den // a.denom
        # Коэффициент на который домножжаем второй числитель
        b_k = n_den // b.denom
        # Умножаем коэффициенты и числители, знаменатель - НОК
        n_num = a.numer * Integer(str(a_k)) + b.numer * Integer(str(b_k))
        # Возвращаем <object Rational>
        return Rational(str(n_num) + '/' + str(n_den))

    def __sub__(self, oth):
        '''Вычитание рациональных чисел, Васильев Максим'''
        # Аналогично с целыми
        # Возращаем <object Rational>
        return self + -oth

    def __mul__(self, oth):
        '''Умножение рациональных чисел, Гусева Екатерина'''
        # Умножаем числители и знаменатели и сокращаем их
        # Возвращаем <object Rational>
        return Rational(str(self.numer * oth.numer) + '/' + str(self.denom * oth.denom)).red()

    def isInteger(self):
        '''Проверка, является ли дробь - целым, Васильев Максим'''
        # Проверяем делится ли числитель на знаменатель нацело,
        # остаток от деления - 0
        # Возвращаем <object Bool>
        return (self.numer.ton() % self.denom).isZero()

    def red(self):
        '''Сокращение дроби, Гусева Екатерина'''
        num = self.numer.ton()
        den = self.denom
        # Находим НОД числителя и знаменателя
        gcd = num.gcd(den)
        # Делим числитель и знаменатель на НОД
        self.numer.digits = (num // gcd).digits
        self.denom = den // gcd
        # Возвращаем <object Rational>
        return self

    def turn(self):
        '''Получение вида 1/x - для дроби, Васильев Максим'''
        # Числитель становится знаменателем
        # Знаменатель числителем
        n_den = Natural(str(self.numer.abs()))
        n_num = Integer(str(self.denom))
        n_num.negative = self.numer.negative
        # Возвращаем <object Rational>
        return Rational(str(n_num) + '/' + str(n_den))

    def __truediv__(self, oth):
        '''Деление рациональных, Васильев Максим'''
        # Сводим деление к умножению на обратное
        # Возвращаем <object Rational>
        return self * oth.turn()

    def isNegative(self):
        '''Возвращает True если отрицательный, False если положительный'''
        return self.numer.negative

    def toContinued(self):
        '''Дробь в непрерывную, Васильев Максим'''
        a = Natural(str(self.numer.abs()))
        b = Natural(str(self.denom))
        res = ''
        # Применяем алгоритм Евклида к дробям, записываем
        # в res строку вида '1 2 3 4 5' где цифры - остатки
        # от деления
        while not a.isZero() and not b.isZero():
            if a > b:
                res += str(a // b) + ' '
                a = a % b
            else:
                res += str(b // a) + ' '
                b = b % a
        # Вызываем функцию которая возвращает красивое представление
        # непрерывной дроби
        # Возвращает <object String>
        return contForm(res)

    def toi(self):
        '''Преобразование в целое рационального, Васильев Максим'''
        self.red()
        # Если знаменатель после сокращения равен 1 - то число целое
        if self.denom == Natural('1'):
            # Возвращаем <object Integer>
            return Integer(str(self.numer))
