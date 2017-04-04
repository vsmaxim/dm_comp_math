from rational import Rational


def xi(i):
    # Возвращает моном в красивом виде ax^b
    if i == 1:
        return 'x'
    elif i:
        return 'x^{}'.format(i)
    else:
        return ''


class Polynome:
    def __init__(self, str):
        '''Конструктор для класса многочленов, Васильев Максим'''
        # Полином хранится как массив рациональных чисел (коэфициентов)
        self.coeffs = [Rational(i) for i in reversed(str.split())]

    def __str__(self):
        '''Возвращает строковое представление многочлена, Васильев Максим'''
        s = ''
        # Черная магия
        for i in range(len(self.coeffs)):
            # Мономы с коэффициентом 0 не выводим
            if self.coeffs[i].numer.isZero():
                continue
            # Если моном положительный - выводим с плюсиком
            if not self.coeffs[i].numer.negative:
                buf = '+ {}'.format(self.coeffs[i])
            else:
                # Иначе просто выводим
                buf = '{}'.format(self.coeffs[i])
            # Ага
            s = '{}{} '.format(buf, xi(i)) + s
        # Негоже первое положительное число с плюсом выводить
        if len(s) and s[0] == '+':
            s = s[2:]
        # Или ничего не выводить, если нулевой многочлен
        elif not len(s):
            s = '0'
        # Возвращаем <object String>
        return s

    def tostr(self):
        '''Возвращает строку (из коэффициентов многочлена),
        которую требует конструктор на вход, Васильев Максим'''
        return ' '.join(str(i) for i in reversed(self.coeffs))

    def deg(self):
        '''Возвращает степень многочлена, Васильев Максим'''
        for i in range(len(self.coeffs) - 1, -1, -1):
            # Возвращаем порядковый номер первого ненулевого монома
            if not self.coeffs[i].numer.isZero():
                return i
        # Если многочлен нулевой, возвращаем -1
        return -1

    def lead(self):
        '''Возвращает старший коэффициент многочлена, Васильев Максим'''
        # Возвращаем старший коэффициент, наверное не нулевой, правда,я надеюсь
        # Возвращаем <object Rational>
        return self.coeffs[-1]

    def lessDeg(self, oth):
        '''Возвращает true если степень self < oth, Васильев Максим'''
        return self.deg() < oth.deg()

    def moreeqDeg(self, oth):
        '''Возвращает true если степень self >= oth, Васильев Максим'''
        return self.deg() >= oth.deg()

    def __gt__(self, oth):
        '''Перегрузка > для класса Polynome, Васильев Максим'''
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
        # В a - многочлен наибольшей степени
        if a.lessDeg(b):
            a, b = b, a
        # Складываем все коэффициенты
        for i in range(len(b.coeffs)):
            a.coeffs[i] = a.coeffs[i] + b.coeffs[i]
        # Возвращаем <object Polynome>
        return a

    def __neg__(self):
        '''Унарный минус для многочленов, Васильев Максим'''
        a = Polynome(self.tostr())
        # Проходимся по всем коэфициентам унарным минусом, всего-то лишь
        for i in range(len(a.coeffs)):
            a.coeffs[i].numer.negative = not a.coeffs[i].numer.negative
        # Возвращаем <object Polynome>
        return a

    def __sub__(self, oth):
        '''Вычитание многочленов, Васильев Максим'''
        # Возвращаем <object Polynome>
        return self + -oth

    def mulM(self, k, n):
        '''Умножение многочлена на моном с рациональным коэффициентом
        k и степенью i, Васильев Максим'''
        a = Polynome('0/1')
        # Находим максимальную степень многочлена в результате
        maxDeg = len(self.coeffs) + n
        # Присваиваем новым мономам коэфициент 0/1
        while len(a.coeffs) != maxDeg:
            a.coeffs.append(Rational('0/1'))
        # Находим коэффициенты при старших степенях
        for i in range(len(self.coeffs)):
            a.coeffs[i + n] = self.coeffs[i] * k
        # Возвращаем <object Polynome>
        return a

    def __mul__(self, oth):
        '''Умножение многочленов, Васильев Максим'''
        a = Polynome(self.tostr())
        b = Polynome(oth.tostr())
        res = Polynome('0/1')
        if a.lessDeg(b):
            a, b = b, a
        # Результат умножения - сумма умножений большего полинома
        # на мономы меньшего
        for i in range(len(b.coeffs)):
            res = res + a.mulM(b.coeffs[i], i)
        # Возвращаем <object Polynome>
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
        # Заводим многочлен под результат, степени разность двух + 1
        res.coeffs = [Rational('0/1') for i in range(da + 1)]
        i = 0
        # Пока степень делимого больше степени делителя
        while a.moreeqDeg(b):
            res.coeffs[da - i] = a.coeffs[-1]
            # Вычитаем полином умноженный на коэфициент при старшем члене
            if not a.coeffs[-1].isZero():
                cur = b.mulM(a.coeffs[-1], da - i)
                a = a - cur
            i += 1
            # Выкидываем первый коэффициент, т.к. мы его вычли
            a.coeffs.pop()
        # Возвращаем целую часть и остаток от деления
        # Возвращаем [<object Polynome>, <object Polynome>]
        return [res, a]

    def __floordiv__(self, oth):
        '''Целая часть от деления многочленов, Васильев Максим'''
        # Возвращаем <object Polynome>
        return self.div(oth)[0]

    def __mod__(self, oth):
        '''Остаток от деления многочленов, Васильев Максим'''
        # Возвращаем <object Polynome>
        return self.div(oth)[1]

    def gcd(self, oth):
        '''НОД многочленов, Васильев Максим'''
        # Алгоритм аналогичен НОД целых чисел
        a = Polynome(self.tostr())
        b = Polynome(oth.tostr())
        zero = Polynome('0/1')
        while a > zero and b > zero:
            if (a > b):
                a = a % b
            else:
                b = b % a
        # Возвращаем <object Rational>
        return a + b

    def nmr(self):
        '''Кратные корни в простые, Васильев Максим'''
        # Делим многочлен на НОД от многочлена и его производной
        # Возвращаем <object Polynome>
        return self // self.gcd(self.derivative())


if __name__ == '__main__':
    x = Polynome('1/1 0/1 -1/1')
    y = Polynome('1/1 1/1')
    print(x // y)
    print(x % y)
  