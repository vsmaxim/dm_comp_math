from naturals import Natural


class Integer(Natural):
    def __init__(self, digits):
        '''Конструктор целого числа, Васильев Максим'''
        # Целое число хранится в перевёрнутом виде в .digits
        # Знак целого числа хранится в bool в .negative
        # True - отрицательное, False - неотрицательное
        self.negative = digits[0] == '-'
        if self.negative:
            digits = digits[1:]
        self.digits = [int(i) for i in reversed(digits)]

    def __str__(self):
        '''Строковое представление integer, Васильев Максим'''
        s = ''
        # Если ноль - возвращаем строку с нулём
        if self.isZero():
            return '0'
        # Если отрицательное, то добавляем '-'
        if self.negative:
            s = '-'
        # Возвращаем <object String>
        return s + ''.join(str(i) for i in reversed(self.digits))

    def __neg__(self):
        '''MUL_ZM_Z Умножение целого на -1, Васильев Максим'''
        # Делаем копию
        a = Integer(str(self))
        # Меняем флаг negative на противоположный
        a.negative = not a.negative
        # Возвращаем <object Integer>
        return a

    def abs(self):
        '''ABS_Z_N Абсолютная величина числа, Васильев Максим'''
        res = Integer('0')
        res.digits = self.digits
        # Делаем число положительным
        res.negative = False
        # Возвращаем <object Integer>
        return res

    def isNegative(self):
        '''Возвращает True если отрицательный, False в ином случае'''
        return self.negative

    def isZero(self):
        '''Проверка целого числа на ноль, Васильев Максим'''
        # Алгоритм, аналогичный реализованному для натуральных
        for i in range(len(self.digits)):
            if self.digits[i]:
                return False
        return True

    def __pow__(self, oth):
        '''Возведение целого числа в степень, Васильев Максим'''
        a = Natural(str(self.abs()))
        b = Natural(str(oth.abs()))
        # Результат - возведение натурального a в b
        res = Integer(str(a ** b))
        # Отрицательность получается из соображений четности степени
        if self.negative and (b % Natural('2') == Natural('1')):
            res.negative = self.negative
        # Возвращаем <object Integer>
        return res

    def positivity(self):
        '''POZ_Z_D Определение положительности числа, Васильев Максим'''
        # Возвращает 0 если число равно нулю, если отрицательное -1
        # и если положительное - 1
        if self.isZero():
            return 0
        elif self.negative:
            return -1
        else:
            return 1

    def __le__(self, oth):
        # Перегрузка оператора < для целых чисел
        # если отрицательность чисел разная - возвращает
        # значение отрицательности первого числа, что в
        # точности совпадает с результатом оператора <,
        # можете проверить и удостовериться в этом
        if self.negative != oth.negative:
            return self.negative
        else:
            if self.negative:
                return not self.ton() < oth.ton()
            else:
                return self.ton() < oth.ton()

    def ton(self):
        '''Преобразование Integer->Natural, Васильев Максим'''
        # Возвращаем <object Natural>
        return Natural(str(self.abs()))

    def __add__(self, oth):
        '''Сложение двух целых чисел, Васильев Максим'''
        # Инициализируем по аналогии с предыдущими модулями
        # a и b натуральные значения целых
        result = Integer('0')
        a = self.ton()
        b = oth.ton()
        # Если числа одного знака, то просто складываем со
        # взглядом на знак
        if self.negative == oth.negative:
            result = Integer(str(a + b))
            result.negative = self.negative
        else:
            # Если числа разных знаков, то вычитаем и отдаем знак большего
            # из двух чисел
            result = Integer(str(a - b))
            if (a < b):
                result.negative = oth.negative
            else:
                result.negative = self.negative
        # Возвращаем <object Integer>
        return result

    def __sub__(self, oth):
        '''Вычитание двух целых чисел, Васильев Максим'''
        # Преобразуем вычитание к сложению с унарным минусом
        # возвращаем <object Integer>
        return self + -oth

    def __mul__(self, oth):
        '''Умножение двух целых чисел, Васильев Максим'''
        a = self.ton()
        b = oth.ton()
        # Результат - умножение натуральных
        result = Integer(str(a * b))
        # Знак результата соответствует данному булеву выражению
        result.negative = self.negative != oth.negative
        # Возвращаем <object Integer>
        return result

    def div(self, oth):
        '''Деление, возвращающее остаток и целую часть, Васильев Максим'''
        # Деление целых аналогично умножению целых, также пользуемся
        # Уже готовым модулем для натуральных чисел
        a = self.ton()
        b = oth.ton()
        res = a.div(b)
        for i in range(len(res)):
            res[i] = Integer(str(res[i]))
            res[i].negative = self.negative != oth.negative
        if not res[1].isZero() and res[1].isNegative():
            if not oth.isNegative():
                res[1] = res[1] + oth
                res[0] = res[0] - Integer('1')
            else:
                res[1] = -res[1]
        if not res[0].isNegative():
            if not res[1].isZero() and self.isNegative():
                res[1] = (res[1] + oth).abs()
                res[0] = res[0] + Integer('1')

        # Возвращаем <object Integer>
        return res

    def __mod__(self, oth):
        '''Перегрузка операции %, остаток от деления'''
        # Возвращаем <object Integer>
        return self.div(oth)[1]

    def __div__(self, oth):
        '''Перегрузка операции //, целая часть от деления'''
        # Пользуемся результатом метода .div()
        # Возвращаем <object Integer>
        return self.div(oth)[0]

    def ferma(self):
        '''Метод ферма для нечетных чисел, и четных имеющих в разложении 2
        более чем в 1 степени, Васильев Максим'''
        # Задаем начальные значения rx, ry и rxy исходя из примерного значения
        # корня из числа
        a = Integer(str(self.ton().sqrt()))
        rx = Integer('2') * a + Integer('1')
        ry = Integer('1')
        rxy = a ** Integer('2') - self
        # Пока выражение от x, y не равно нулю, увеличиваем или уменьшаем в
        # зависимости от ситуации rx и ry и добавляем или вычитаем их же
        while not rxy.isZero():
            if rxy <= Integer('0'):
                rxy = rxy + rx
                rx = rx + Integer('2')
            else:
                rxy = rxy - ry
                ry = ry + Integer('2')
        # Возвращаем результат разложения в виде a * b где a и b - делители
        return str((rx - ry) // Integer('2')) + '*' + str((rx + ry) // Integer('2') - Integer('1'))

if __name__ == '__main__':
    a = Integer('3')
    b = Integer('-4')
    print(a // b)
    print(a % b)