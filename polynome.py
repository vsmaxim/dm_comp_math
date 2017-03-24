from rational import Rational

def xi(i):
    if i == 1:
        return 'x'
    elif i:
        return 'x^{}'.format(i)
    else:
        return ''

class Polynome:
    def __init__(self, str):
        '''Конструктор для класса многочленов, Васильев Максим'''
        coeffs = str.split()
        self.coeffs = [Rational(i) for i in reversed(coeffs)]
    def __str__(self):
        '''Возвращает строковое представление многочлена, Васильев Максим'''
        s = ''
        for i in range(len(self.coeffs)):
            if not self.coeffs[i].numer.negative:
                buf = '+ {}'.format(self.coeffs[i])
            else:
                buf = '{}'.format(self.coeffs[i])
            s = '{}{} '.format(buf, xi(i)) + s
        if s[0] == '+':
            s = s[2:]
        return s
    
    def tostr(self):
        '''Возвращает строку (из коэффициентов многочлена), 
        которую требует конструктор на вход, Васильев Максим'''
        return ' '.join(str(i) for i in reversed(self.coeffs))

    def deg(self):
        '''Возвращает степень многочлена, Васильев Максим'''
        for i in range(len(self.coeffs) - 1, -1, -1):
            if not self.coeffs[i].numer.isZero():
                return i
        if len(self.coeffs) == 0:
            return -1
    
    def lead(self):
        '''Возвращает старший коэффициент многочлена, Васильев Максим'''
        return self.coeffs[-1]

    def lessDeg(self, oth):
        '''Возвращает true если степень self < oth, Васильев Максим'''
        if self.deg() < oth.deg():
            return True
        else:
            return False

    def moreeqDeg(self, oth):
        if self.deg() >= oth.deg():
            return True
        else:
            return False

    def __gt__(self, oth):
        if self.deg() > oth.deg():
            return True
        elif self.deg() < oth.deg():
            return False
        else:
            for i in range(self.deg(), -1, -1):
                if self.coeffs[i] > oth.coeffs[i]:
                    return True
                else:
                    return False

    def __add__(self, oth):
        '''Сложение многочленов, Васильев Максим'''
        a = Polynome(self.tostr())
        b = Polynome(oth.tostr())
        if a.lessDeg(b):
            a, b = b, a
        for i in range(len(b.coeffs)):
            a.coeffs[i] = a.coeffs[i] + b.coeffs[i]
        return a
    
    def __neg__(self):
        '''Унарный минус для многочленов, Васильев Максим'''
        a = Polynome(self.tostr())
        for i in range(len(a.coeffs)):
            a.coeffs[i].numer.negative = not a.coeffs[i].numer.negative
        return a

    def __sub__(self, oth):
        '''Вычитание многочленов, Васильев Максим'''
        return self + -oth

    def mulM(self, k, n):
        '''Умножение многочлена на моном с рациональным коэффициентом
        k и степенью i, Васильев Максим'''
        a = Polynome('0/1')
        maxDeg = len(self.coeffs) + n
        while len(a.coeffs) != maxDeg:
            a.coeffs.append(Rational('0/1'))
        for i in range(len(self.coeffs)):
            a.coeffs[i + n] = self.coeffs[i] * k
        return a

    def __mul__(self, oth):
        '''Умножение многочленов, Васильев Максим'''
        a = Polynome(self.tostr())
        b = Polynome(oth.tostr())
        res = Polynome('0/1')
        if a.lessDeg(b):
            a, b = b, a
        for i in range(len(b.coeffs)):
            res = res + a.mulM(b.coeffs[i], i)
        return res
    
    def derivative(self):
        '''Вычисление производной от многочлена, Васильев Максим'''
        a = Polynome(self.tostr())
        a.coeffs = a.coeffs[1:]
        for i in range(len(a.coeffs)):
            a.coeffs[i] = a.coeffs[i] * Rational(str(i + 1) + '/1')
        return a
    
    def div(self, oth):
        '''Деление многочленов столбиком, Васильев Максим'''
        a = Polynome(self.tostr())
        b = Polynome(oth.tostr())
        da = a.deg() - b.deg()
        res = Polynome('0/1')
        res.coeffs = [Rational('0/1') for i in range(da + 1)]
        i = 0
        while a.moreeqDeg(b):
            cur = b.mulM(a.coeffs[-1], da - i)
            res.coeffs[da - i] = a.coeffs[-1]
            a = a - cur
            i += 1
            a.coeffs.pop()
        return [res, a]

    def __floordiv__(self, oth):
        '''Целая часть от деления многочленов, Васильев Максим'''
        return self.div(oth)[0]

    def __mod__(self, oth):
        '''Остаток от деления многочленов, Васильев Максим'''
        return self.div(oth)[1]

    # def gcd(self, oth):
    #     a = Polynome(self.tostr())
    #     b = Polynome(oth.tostr())
    #     while a.deg() >= 0 and b.deg() >= 0:
    #         if (a > b):
    #             a = a % b
    #         else:
    #             b = b % a
    #     return a + b
            

if __name__ == '__main__':
    x = Polynome('2/1 -1/1 0/1 12/1 -72/1 0/1 3/1') 
    y = Polynome('1/1 2/1 0/1 -1/1') 
    print(x // y)
    print(x % y)
    print(x.gcd(y))
