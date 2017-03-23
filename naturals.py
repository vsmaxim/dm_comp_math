class Natural:

    def __init__(self, digits):
        '''Конструктор натурального числа, Васильев Максим'''
        self.digits = [int(i) for i in reversed(digits)]

    def __str__(self):
        '''Строковое представление натурального числа, Васильев Максим'''
        return ''.join([str(i) for i in reversed(self.digits)])
    
    def __lt__(self, oth):
        '''Перегрузка оператора < для натуральных чисел, Васильев Максим'''
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
        return False


    def __le__(self, oth):
        '''COM_NN_D Сравнение двух чисел, Васильев Максим'''
        if len(self.digits) < len(oth.digits):
            return True
        elif len(self.digits) > len (oth.digits):
            return False
        else:
            for i in range(len(self.digits) -1, -1, -1):
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
    
    def __mul__(self,oth):
        '''Умножение длинных чисел, Гусева Екатерина'''
        if (self <= oth):
            self.digits, oth.digits = oth.digits, self.digits
        p = Natural('0')
        for i in range(len(oth.digits)):
            k = oth.digits[i]
            c = self.mulk(k)
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
        #print("Division: self - {}".format(self))
        self.shrinkZeros()
        return self         
    
    def isZero(self):
        '''NZER_N_B Проверка на ноль, Васильев Максим'''
        for i in self.digits:
            if i:
                return False
        return True

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
                    #print('For {} run cur is {} num is {}'.format(k, cur, num))
                    cur = cur - num
                    k += 1
                    #print('For {} run cur is {} num is {}'.format(k, cur, num))
                    #print(num <= cur)
                res.digits.append(k)
            if curNum.isZero() and cur.isZero():
                res.digits = res.digits + curNum.digits
                break
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
                # print(b)
            else:
                self = self % b
                # print(self)
        return self + b

    def lcm(self, b):
        '''НОК двух натуральных чисел, Васильев Максим'''
        return (self * b) // self.gcd(b)

#Для тестов 
if __name__ == '__main__':
    a = Natural('1635203')
    b = Natural('8937')
    print(a.gcd(b))
    print(a.lcm(b))