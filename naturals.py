class Natural:

    def __init__(self, digits):
        self.digits = [int(i) for i in reversed(digits)]

    def __str__(self):
        return ''.join([str(i) for i in reversed(self.digits)])
    
    def __le__(self, oth):
        '''COM_NN_D Сравнение двух чисел, Васильев Максим'''
        if len(self.digits) < len(oth.digits):
            return True
        elif len(self.digits) > len (oth.digits):
            return False
        else:
            for i in range(len(self.digits)):
                if self.digits[i] < oth.digits[i]:
                    return True
                elif self.digits[i] > oth.digits[i]:
                    return False
            return True

    def __add__(self, oth):
        '''ADD_NN_N Сложение двух чисел, Васильев Максим'''
        if (self <= oth): #Делаем так, чтобы в self хранилось большее число
            self.digits, oth.digits = oth.digits, self.digits
        over = 0
        for i in range(len(oth.digits)): #Складываем поразрядно с числом oth
            cur = over + self.digits[i] + oth.digits[i]
            over = cur // 10
            self.digits[i] = cur % 10

        i = len(oth.digits)
        while over > 0: #Избавляемся от переполнения разрядов
            if (i == len(self.digits)):
                self.digits.append(0)
            cur = over + self.digits[i]
            over = cur // 10
            self.digits[i] = cur % 10
            i += 1
        return self

    def __mod__(self, num):
        while self <= num:
            self = self - num
        return self

    def __floordiv__(self, num):
        k = 0
        while self <= num:
            self = self - num
            k += 1
        return k

    def mulk(self, k):
        '''MUL_ND_N Умножение на цифру, Гусева Екатерина'''
        res = [0] * len(self.digits)
        ost = 0
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

    def mulNk(self,k):
        '''MUL_Nk_N Умножение на 10^k, Гусева Екатерина'''
        return [0] * k + self.digits

    def shrinkZeros(self):
        '''Функция, убирающая лидирующие нули в числе'''
        while not self.digits[-1]:
            self.digits.pop()

    def __sub__(self, oth):
        '''SUB_NN_N Вычитание из большего натур. меньшего, Васильев Максим'''
        if (self <= oth):
            self.digits, oth.digits = oth.digits, self.digits
        over = 0
        for i in range(len(self.digits) - 1):
            self.digits[i + 1] -= 1
            self.digits[i] += 10
        for i in range(len(oth.digits)):
            self.digits[i] = self.digits[i] - oth.digits[i]
        for i in range(len(self.digits)):
            cur = self.digits[i] + over
            self.digits[i] = cur % 10
            over = cur // 10
        self.shrinkZeros()
        return self         
    
    def isZero(self):
        '''NZER_N_B Проверка на ноль, Васильев Максим'''
        if len(self.digits) == 1 and self.digits[i] == 0:
        #Число длины 1 и последней цифрой 0 - является нулём 
            return True
        else:
            return False

    def inc(self):
        '''ADD_1N_N Добавление единицы, Васильев Максим'''
        if (self.digits[0] < 9):
        #Если последняя цифра меньше 9, то переполнения разряда не возникает
        #И мы просто добавляем единицу
            self.digits[0] += 1
        else:
            i = 0
            while (self.digits[i] == 9):
            #Если переполнение разряда всёже возникает, то ищем пока
            #Текущий разряд перестанет быть 9 и добавляем единицу
                self.digits[i] = 0
                i += 1
                if i == len(self.digits):
                    self.digits.append(0)
            self.digits[i] += 1
        return self

    

a = Natural(input())

for i in range(10):
    print('For {} mul is {}'.format(i, ''.join(str(i) for i in reversed(a.mulNk(i)))))
    