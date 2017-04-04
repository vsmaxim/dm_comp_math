class Natural:
    def __init__(self, digits):
        '''Конструктор натурального числа, Васильев Максим'''
        # Натуральное число хранится в виде массива его цифр в 10сс
        self.digits = [int(i) for i in reversed(digits)]

    def __str__(self):
        '''Строковое представление натурального числа, Васильев Максим'''
        # Метод, возвращающий строковое представление числа, необходим
        # в python для работы многих функций, таких как print(), str(),
        # и так далее
        return ''.join([str(i) for i in reversed(self.digits)])

    def __eq__(self, oth):
        '''Перегрузка оператора == для натуральных чисел, Васильев Максим'''
        # Если длины чисел различаются, то они неравны
        if len(self.digits) != len(oth.digits):
            return False
        else:
            # Поразрядное сравнение цифр, до того момента, как не будет
            # найден первый разряд, в котором разряды отличаются
            for i in range(len(self.digits)):
                if self.digits[i] != oth.digits[i]:
                    return False
            return True

    def __lt__(self, oth):
        '''Перегрузка оператора < для натуральных чисел, Васильев Максим'''
        # Если длина числа меньше длины второго, то первое число точно
        # меньше чем второе число, лидирующие нули не хранятся.
        if len(self.digits) < len(oth.digits):
            return True
        elif len(self.digits) > len(oth.digits):
            return False
        else:
            # Если же длины чисел совпали, то поразрядно ищем с конца
            # разряд, в котором они будут отличаться, и в зависимости
            # от характера различия (<>) делаем вывод и возвращаем значение
            for i in range(len(self.digits) - 1, -1, -1):
                if self.digits[i] < oth.digits[i]:
                    return True
                elif self.digits[i] > oth.digits[i]:
                    return False
        # Если таких разрядов не было найдено, то числа равны
        return False

    def bin(self):
        '''Возвращает двоичное представление числа, Васильев Максим'''
        # Создаём копию чисел, чтобы не повредить исходные в результате
        # операций над ними
        a = Natural(str(self))
        zero = Natural('0')
        two = Natural('2')
        res = ''
        # Пока наше число больше нуля, делим его на 2 и добавляем в конец
        # остаток от деления на 2 (0 или 1)
        while zero < a:
            res += str(a % two)
            a = a // two
        # Так как представление числа в 2сс получилось перевёрнутым, возвращаем
        # строку в обратном порядке
        return res[::-1]

    def __pow__(self, oth):
        '''Быстрое возведение в степень, Васильев Максим'''
        a = Natural(str(self))
        b = oth.bin()
        # res - переменная в которой хранится результат возведения в
        # степень <object Natural>
        res = Natural('1')
        for i in b:
            # Если текущий бит равен 1 - это эквивалентно возведению в квадрат
            #  и умножению на основание
            if i == '1':
                res = res * res * a
            # Иначе - это эквивалентно возведению в квадрат
            else:
                res = res * res
        # Возвращаем результат <object Natural>
        return res

    def __le__(self, oth):
        '''COM_NN_D Сравнение двух чисел, Васильев Максим'''
        # Перегрузка оператора <= работает по аналогии с
        # предыдущими перегрузками таких же операторов
        if len(self.digits) < len(oth.digits):
            return True
        elif len(self.digits) > len(oth.digits):
            return False
        else:
            for i in range(len(self.digits) - 1, -1, -1):
                if self.digits[i] < oth.digits[i]:
                    return True
                elif self.digits[i] > oth.digits[i]:
                    return False
            return True

    def __add__(self, oth):
        '''ADD_NN_N Сложение двух чисел, Васильев Максим'''
        # Создаём копии чисел, чтобы не испортить исходные
        a = Natural(str(self))
        b = Natural(str(oth))
        # Делаем так, чтобы в a хранилось большее число
        if (a <= b):
            a.digits, b.digits = b.digits, a.digits
        # over - переменная под переполнение разряда
        over = 0
        for i in range(len(b.digits)):  # Складываем поразрядно с числом oth
            cur = over + a.digits[i] + b.digits[i]
            over = cur // 10
            a.digits[i] = cur % 10

        i = len(b.digits)
        while over > 0:  # Избавляемся от переполнения разрядов
            if (i == len(a.digits)):
                a.digits.append(0)
            cur = over + a.digits[i]
            over = cur // 10
            a.digits[i] = cur % 10
            i += 1
        return a

    def __mul__(self, oth):
        '''Умножение длинных чисел, Гусева Екатерина'''
        a = Natural(str(self))
        b = Natural(str(oth))
        if a < b:
            a.digits, b.digits = b.digits, a.digits
        p = Natural('0')
        for i in range(len(b.digits)):
            k = b.digits[i]
            c = a.mulk(k)
            c = c.mulNk(i)
            p = p + c
        return p

    def reverse(self):
        '''Функция, переворачивающая число, Васильев Максим'''
        self.digits = [int(i) for i in reversed(self.digits)]
        return self

    def mulk(self, k):
        '''MUL_ND_N Умножение на цифру, Гусева Екатерина'''
        res = [0] * len(self.digits)
        r = 0
        for i in range(len(self.digits)):
            res[i] = self.digits[i] * k + r
            r = res[i] // 10
            res[i] %= 10
        if r:
            res.append(r)
        b = Natural('')
        b.digits = res
        return b

    def mulNk(self, k):
        '''MUL_Nk_N Умножение на 10^k, Гусева Екатерина'''
        oth = Natural('')
        oth.digits = [0] * k + self.digits
        return oth

    def shrinkZeros(self):
        '''Функция, убирающая лидирующие нули в числе'''
        try:
            while not self.digits[-1] and len(self.digits) - 1:
                self.digits.pop()
        except:
            pass

    def __sub__(self, oth):
        '''SUB_NN_N Вычитание из большего натур. меньшего, Васильев Максим'''
        a = Natural(str(self))
        b = Natural(str(oth))
        if (a <= b):
            a.digits, b.digits = b.digits, a.digits
        over = 0
        for i in range(len(a.digits) - 1):
            a.digits[i + 1] -= 1
            a.digits[i] += 10
        for i in range(len(b.digits)):
            a.digits[i] = a.digits[i] - b.digits[i]
        for i in range(len(a.digits)):
            cur = a.digits[i] + over
            a.digits[i] = cur % 10
            over = cur // 10
        a.shrinkZeros()
        return a

    def isZero(self):
        '''NZER_N_B Проверка на ноль, Васильев Максим'''
        for i in self.digits:
            if i:
                return False
        return True

    def inc(self):
        '''ADD_1N_N Добавление единицы, Васильев Максим'''
        if (self.digits[0] < 9):
            # Если последняя цифра меньше 9, то переполнения
            # разряда не возникает и мы просто добавляем единицу
            self.digits[0] += 1
        else:
            i = 0
            while (self.digits[i] == 9):
                # Если переполнение разряда всёже возникает, то ищем пока
                # Текущий разряд перестанет быть 9 и добавляем единицу
                self.digits[i] = 0
                i += 1
                if i == len(self.digits):
                    self.digits.append(0)
            self.digits[i] += 1
        return self

    def subNk(self, oth, k):
        '''SUB_NDN_N Вычитание из натурального числа другого
        натурального умноженного на цифру Васильев Максим'''
        return self - oth.mulk(k)

    def div(self, num):
        '''Деление числа на число столбиком, Васильев Максим'''
        cur = Natural('')
        res = Natural('')
        curNum = Natural(str(self))
        divided = False
        for i in range(len(self.digits) - 1, -1, -1):
            cur.digits = [self.digits[i]] + cur.digits
            if divided and cur < num:
                res.digits.append(0)
            curNum.digits.pop()
            if num <= cur:
                divided = True
                k = 0
                while num <= cur:
                    cur = cur - num
                    k += 1
                    if cur.isZero():
                        cur.digits = []
                res.digits.append(k)
            if curNum.isZero() and cur.isZero():
                res.digits = res.digits + curNum.digits
                break
        if not len(cur.digits):
            cur.digits = [0]
        return [res.reverse(), cur]

    def __mod__(self, num):
        '''Взятие остатка от деления, Васильев Максим'''
        return self.div(num)[1]

    def __floordiv__(self, num):
        '''Взятие целой части от деления, Васильев Максим'''
        return self.div(num)[0]

    def gcd(self, b):
        '''НОД двух натуральных чисел (алгоритм Евклида), Васильев Максим'''
        zero = Natural('0')
        while zero < self and zero < b:
            if (self < b):
                b = b % self
            else:
                self = self % b
        return self + b

    def lcm(self, b):
        '''НОК двух натуральных чисел, Васильев Максим'''
        return (self * b) // self.gcd(b)

    def sqrt(self):
        '''Поиск примерного корня двоичным поиском, Васильев Максим'''
        two = Natural('2')
        a = Natural(str(self))
        left = Natural('0')
        right = Natural(str(a))
        while left < right - Natural('1'):
            m = (left + right) // two
            if (m ** two) < a:
                left = m
            else:
                right = m
        return m


# Для тестов
if __name__ == '__main__':
    a = Natural('5')
    b = Natural('3')
