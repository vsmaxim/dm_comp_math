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

    def lessDeg(self, oth):
        '''Возвращает true если степень self < oth, Васильев Максим'''
        if len(self.coeffs) < len(oth.coeffs):
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
            

if __name__ == '__main__':
    x = Polynome('1/1 1/1 1/1 1/1')
    y = Polynome('1/1 1/1 1/1')
    print(x - y)
