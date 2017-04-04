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
        two = Natural('2')
        res = ''
        # Пока наше число больше нуля, делим его на 2 и добавляем в конец
        # остаток от деления на 2 (0 или 1)
        while Natural('0') < a:
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
        # Складываем поразрядно с числом oth
        for i in range(len(b.digits)):
            # cur - рабочая переменная, которая хранит в себе
            # сумму двух разрядов
            cur = over + a.digits[i] + b.digits[i]
            # Переполнение разряда - целая часть от деления на 10
            over = cur // 10
            # Разряд результата, хранится в a <object Natural>
            a.digits[i] = cur % 10

        i = len(b.digits)
        # Избавляемся от переполнения разрядов, если после сложения
        # оно осталось
        while over:
            # Добавляем новый разряд, если возникло переполнение
            # и все разряды числа уже "израсходованы"
            if (i == len(a.digits)):
                a.digits.append(0)
            # Делаем действия, аналогичные сложению
            cur = over + a.digits[i]
            over = cur // 10
            a.digits[i] = cur % 10
            i += 1
        # Возвращаем результат <object Natural>
        return a

    def __mul__(self, oth):
        '''Умножение длинных чисел, Гусева Екатерина'''
        # Делаем копии
        a = Natural(str(self))
        b = Natural(str(oth))
        # Меняем местами, если нужно, в b - меньшее
        if a < b:
            a.digits, b.digits = b.digits, a.digits
        # p - результат умножения, инициализирован нулём
        p = Natural('0')
        for i in range(len(b.digits)):
            # k - текущий разряд на которое умножаем число
            k = b.digits[i]
            # Умножаем исходное число на k
            c = a.mulk(k)
            # Умножаем результат на 10^i, чтобы "сдвинуть" его
            c = c.mulNk(i)
            # Добавляем к результату
            p = p + c
        # Возвращаем результат <object Natural>
        return p

    def reverse(self):
        '''Функция, переворачивающая число, Васильев Максим'''
        self.digits = self.digits[::-1]
        return self

    def mulk(self, k):
        '''MUL_ND_N Умножение на цифру, Гусева Екатерина'''
        # Заводим массив под результат, длиной self.digits,
        # потому что при самом плохом случае, у нас не будет переполнения
        # более чем на один разряд
        res = [0] * len(self.digits)
        # r - переполнение разряда
        r = 0
        for i in range(len(self.digits)):
            # Умножаем текущий разряд на k и прибавляем к нему
            # переполнение из предыдущего действия
            res[i] = self.digits[i] * k + r
            # Находим переполнение в следующий разряд
            r = res[i] // 10
            # Текущий разряд находим по модулю 10
            res[i] %= 10
        # Если закончились разряды и осталось переполнение
        # добавляем его в начало числа
        if r:
            res.append(r)
        # Преобразуем массив в <object Natural>
        b = Natural('')
        b.digits = res
        # Возвращаем <object Natural>
        return b

    def mulNk(self, k):
        '''MUL_Nk_N Умножение на 10^k, Гусева Екатерина'''
        oth = Natural('')
        oth.digits = [0] * k + self.digits
        return oth

    def shrinkZeros(self):
        '''Функция, убирающая лидирующие нули в числе'''
        try:
            # Если наше число имеет ненулевую длину, то пытаемся убрать
            # лидирующие нули
            while not self.digits[-1] and len(self.digits) - 1:
                self.digits.pop()
        except:
            pass

    def __sub__(self, oth):
        '''SUB_NN_N Вычитание из большего натур. меньшего, Васильев Максим'''
        # Делаем копии исходных объектов
        a = Natural(str(self))
        b = Natural(str(oth))
        # Меняем местами, чтобы меньшее число лежало в a
        if (a <= b):
            a.digits, b.digits = b.digits, a.digits
        # Переменная под переполнение разряда
        over = 0
        # Занимаем из каждого разряда по 1 в предыдущий, чтобы без проблем
        # сделать вычитание двух чисел
        for i in range(len(a.digits) - 1):
            a.digits[i + 1] -= 1
            a.digits[i] += 10
        # Вычитаем из разрядов большего числа, разряды меньшего
        for i in range(len(b.digits)):
            a.digits[i] = a.digits[i] - b.digits[i]
        # Избавляемся от рязрядов больше 9
        for i in range(len(a.digits)):
            cur = a.digits[i] + over
            a.digits[i] = cur % 10
            over = cur // 10
        # Избавляемся от возможных лидирующих нулей в числе
        a.shrinkZeros()
        # Возвращаем <object Natural>
        return a

    def isZero(self):
        '''NZER_N_B Проверка на ноль, Васильев Максим'''
        for i in self.digits:
            # Если встретился ненулевой разряд число - не ноль
            if i:
                return False
            # Если ненулевых разрядов нет - число ноль
        # Возвращаем <object bool>
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
                # Если переполнились все разряды - добавляем ещё один
                if i == len(self.digits):
                    self.digits.append(0)
            # Добавляем к последнему обработаному разряду 1
            self.digits[i] += 1
        return self

    def div(self, num):
        '''Деление числа на число столбиком, Васильев Максим'''
        # Заводим пару <object Natural> для результатов
        cur = Natural('')
        res = Natural('')
        # curNum - число, которое остается в результате вычитаний
        curNum = Natural(str(self))
        # divided - флаг, отвечающий за то, что найдена хотя бы одна цифра
        # результата
        divided = False
        # cur - текущее число, полученное сносом разрядов вниз
        # при делении столбиком
        for i in range(len(self.digits) - 1, -1, -1):
            cur.digits = [self.digits[i]] + cur.digits
            # Если мы уже нашли хоть одну цифру, то при сносе
            # разрядов вниз, мы должны добавлять нули к результату
            if divided and cur < num:
                res.digits.append(0)
            # Удаляем снесённый разряд из curNum
            curNum.digits.pop()
            # Если число полученное снесением разрядов стало меньше, чем
            # делитель, то делим
            if num <= cur:
                # Устанавливаем флаг, что мы разделили число
                divided = True
                # k - цифра результата, количество вычитаний
                k = 0
                while num <= cur:
                    # Вычитаем, пока делитель меньше делимого
                    cur = cur - num
                    k += 1
                    # В cur - остаток от деления, если он равен нулю
                    # заменяем массив его цифр на пустой, чтобы в результате
                    # не возникли лишние нули
                    if cur.isZero():
                        cur.digits = []
                # Добавляем текущую цифру к результату
                res.digits.append(k)
            # Если в числе из которого сносим остались одни нули,
            # дописываем их в результат
            if curNum.isZero() and cur.isZero():
                res.digits = res.digits + curNum.digits
                break
        # Если в остатке не осталось цифр, делаем его равным нулю
        if not len(cur.digits):
            cur.digits = [0]
        # Возвращаем пару значений целая часть, остаток
        # [<object Natural> , <object Natural>]
        return [res.reverse(), cur]

    def __mod__(self, num):
        '''Взятие остатка от деления, Васильев Максим'''
        # Возвращаем второй элемент из деления, реализованного в .div()
        return self.div(num)[1]

    def __floordiv__(self, num):
        '''Взятие целой части от деления, Васильев Максим'''
        # Возвращаем первый элемент из деления, реализованного в .div()
        return self.div(num)[0]

    def gcd(self, b):
        '''НОД двух натуральных чисел (алгоритм Евклида), Васильев Максим'''
        # Пока оба числа больше нуля
        while Natural('0') < self and Natural('0') < b:
            # Заменяем большее остатком от деления на меньшее
            if (self < b):
                b = b % self
            else:
                self = self % b
        # Возвращаем НОД(а, b) как сумму self, b
        # так как одно из них гарантированно равно нулю
        # <object Natural>
        return self + b

    def lcm(self, b):
        '''НОК двух натуральных чисел, Васильев Максим'''
        # Вычисляем НОК исходя из связи НОД и НОК
        # НОК(A, B) = A * B / НОД(A, B)
        # Возвращаем <object Natural>
        return (self * b) // self.gcd(b)

    def sqrt(self):
        '''Поиск примерного корня бинарным поиском, Васильев Максим'''
        two = Natural('2')
        a = Natural(str(self))
        # Задаем левую и правую границу для бинарного поиска
        left = Natural('0')
        right = Natural(str(a))
        # Пока разница между границами > 1
        while left < right - Natural('1'):
            # Находим середину
            m = (left + right) // two
            # Если число из середины в квадрате меньше искомого
            # то сужаем границу слева
            if (m ** two) < a:
                left = m
            # Иначе сужаем границу справа
            else:
                right = m
        # Результат - найденное число, <object Natural>
        return m
