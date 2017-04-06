from tkinter import *
from naturals import Natural
from rational import Rational
from polynome import Polynome
from integer import Integer

root = Tk()
root.title("Коллоквиум по дискретной математике")
root.minsize(600, 400)
# выключаем возможность изменять окно
root.resizable(width=False, height=False)

def rat_divis():
    def division(a, b):
        a1 = Rational(str(a))
        b1 = Rational(str(b))
        text =  a1, "/", b1, "=", a1/b1
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        """ Get the content of entries and passes result to the output area """
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(division(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Деление дробей")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первую дробь").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите вторую дробь").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10, command = handler).grid(row=1, column=7, padx=(10, 0))
    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def rat_sum():
    def division(a, b):
        a1 = Rational(str(a))
        b1 = Rational(str(b))
        text =  a1, "+", b1, "=", a1+b1
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        """ Get the content of entries and passes result to the output area """
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(division(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.resizable(width=False, height=False)
    win.title("Cумма дробей")
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первую дробь").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите вторую дробь").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10, command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def rat_sub():
    def division(a, b):
        a1 = Rational(str(a))
        b1 = Rational(str(b))
        text =  a1, "-", b1, "=", a1-b1
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        """ Get the content of entries and passes result to the output area """
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(division(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.resizable(width=False, height=False)
    win.title("Разность дробей")
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первую дробь").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите вторую дробь").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10, command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def rat_mul():
    def division(a, b):
        a1 = Rational(str(a))
        b1 = Rational(str(b))
        text =  a1, "*", b1, "=", a1*b1
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        """ Get the content of entries and passes result to the output area """
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(division(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Умножение дробей")
    frame = Frame(win)
    frame.grid()
    win.resizable(width=False, height=False)

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первую дробь").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите вторую дробь").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10, command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def rat_s():
    def division(a):
            a1 = Rational(str(a))
            text = a, "=", Rational.red(a1)
            return text

    def inserter(value):
            """ Inserts specified value into text widget """
            output.delete("0.0", "end")
            output.insert("0.0", value)

    def handler():
            """ Get the content of entries and passes result to the output area """

            a_val = str(a.get())
            inserter(division(a_val))

    win = Toplevel(root)
    win.title("Сокращение дроби")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(150, 0))
    a_lab = Label(frame, text="Введите дробь").grid(row=1, column=6)

    but = Button(frame, text="Рассчитать", width=10, command=handler).grid(row=1, column=7, padx=(100, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

#####################################################################################################################
def nat_sum():
    def sum(a, b):
        a1 = Natural(str(a))
        b1 = Natural(str(b))
        text = a1, "+", b1, "=", a1 + b1
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Сумма натуральных чисел")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первое число").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите второе число").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def nat_sub():
    def sum(a, b):
        a1 = Natural(str(a))
        b1 = Natural(str(b))
        text = a1, "-", b1, "=", a1 - b1
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Разность натуральных чисел")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первое число").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите второе число").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def nat_mult():
    def sum(a, b):
        a1 = Natural(str(a))
        b1 = Natural(str(b))
        text = a1, "*", b1, "=", a1 * b1
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Умножение натуральных чисел")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первое число").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите второе число").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def nat_DIV():
    def sum(a, b):
        a1 = Natural(str(a))
        b1 = Natural(str(b))
        if a1<b1:
            a1,b1 = b1,a1
        text = a1, "//", b1, "=", a1 // b1
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Деление без остатка(DIV) натуральных чисел")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первое число").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите второе число").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def nat_MOD():
    def sum(a, b):
        a1 = Natural(str(a))
        b1 = Natural(str(b))
        text = str(a1) + " % " + str(b1) + " = " + str(a1 % b1)
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Остаток от деления натуральных чисел")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первое число").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите второе число").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def nat_gcd():
    def sum(a, b):
        a1 = Natural(str(a))
        b1 = Natural(str(b))
        text = "GCD( "+ a +" , "+ b +" ) = " + str(Natural.gcd(a1,b1))
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Наибольший общий делитель двух натуральных чисел")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первое число").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите второе число").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def nat_lcm():
    def sum(a, b):
        a1 = Natural(str(a))
        b1 = Natural(str(b))
        text = "LCM( "+ a + "," + b + " ) = " + str(Natural.lcm(a1, b1))
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Наибольший общий делитель двух натуральных чисел")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первое число").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите второе число").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10, command=handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)


######################################################################################################################

def int_sum():
    def sum(a, b):
        a1 = Integer(str(a))
        b1 = Integer(str(b))
        text = a + " + " + b + " = " + str(a1 + b1)
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Сумма целых чисел")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первое число").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите второе число").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def int_abs():

    def division(a):
        a1 = Integer(str(a))
        text = '|'+ a + '| = ' + str(Integer.abs(a1))
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        """ Get the content of entries and passes result to the output area """

        a_val = str(a.get())
        inserter(division(a_val))

    win = Toplevel(root)
    win.title("Модуль целого числа")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(150, 0))
    a_lab = Label(frame, text="Введите число").grid(row=1, column=6)

    but = Button(frame, text="Рассчитать", width=10, command=handler).grid(row=1, column=7, padx=(100, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def int_sub():
    def sum(a, b):
        a1 = Integer(str(a))
        b1 = Integer(str(b))
        text = a + " - " + b + " = " + str(a1 - b1)
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Разность целых чисел")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первое число").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите второе число").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def int_mul():
    def sum(a, b):
        a1 = Integer(str(a))
        b1 = Integer(str(b))
        text = a + " * " + b + " = " + str(a1 * b1)
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Умножение целых чисел")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первое число").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите второе число").grid(row=1, column=4)
    but = Button(frame, text="Solve", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def int_div():
    def sum(a, b):
        a1 = Integer(str(a))
        b1 = Integer(str(b))
        text = a + " / " + b + " = " + str(a1 // b1)
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Деление целых чисел")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первое число").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите второе число").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def int_mod():
    def sum(a, b):
        a1 = Integer(str(a))
        b1 = Integer(str(b))
        text = a + " % " + b + " = " + str(a1 % b1)
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Остаток от деления целых чисел")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первое число").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите второе число").grid(row=1, column=4)
    but = Button(frame, text="Solve", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def int_pow():
    def sum(a, b):
        a1 = Integer(str(a))
        b1 = Integer(str(b))
        text = a + " ** " + b + " = " + str(a1 ** b1)
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Возведение в степень целого числа")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите число").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите степень").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def int_qr():
    def sum(a, b):
        a1 = Integer(str(a))
        b1 = Integer(str(b))
        text = a + " = (" + b + ") * (" + str(a1//b1) + ") +" + str(a1%b1)
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Представление деления в виде a = n*q + r")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите первое число").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите второе число").grid(row=1, column=4)
    but = Button(frame, text="Solve", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)
    
######################################################################################################################
def oth_ferma():
    def division(a):
        a1 = Integer(str(a))
        text = a + "=" + str(Integer.ferma(a1))
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        """ Get the content of entries and passes result to the output area """

        a_val = str(a.get())
        inserter(division(a_val))

    win = Toplevel(root)
    win.resizable(width=False, height=False)
    win.title("Метод ферма для нечетных чисел, и четных имеющих в разложении более чем в 1 степени")
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(150, 0))
    a_lab = Label(frame, text="Введите число").grid(row=1, column=6)

    but = Button(frame, text="Рассчитать", width=10, command=handler).grid(row=1, column=7, padx=(100, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def oth_sqrt():
    def division(a):
        a1 = Integer(str(a))
        text = "sqrt(" + a + ")=" + str(Integer.sqrt(a1))
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        """ Get the content of entries and passes result to the output area """

        a_val = str(a.get())
        inserter(division(a_val))

    win = Toplevel(root)
    win.title("Приблизительный квадратный корень из числа")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(150, 0))
    a_lab = Label(frame, text="Введите число").grid(row=1, column=6)

    but = Button(frame, text="Рассчитать", width=10, command=handler).grid(row=1, column=7, padx=(100, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def oth_pow():
    def sum(a, b):
        a1 = Natural(str(a))
        b1 = Natural(str(b))
        text = a + "**" + b + "=" + str(a1 ** b1)
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Быстрое возведение в степень")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите число").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите степень").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def oth_toCont():

    def division(a):
        a1 = Rational(str(a))
        text = a + "=" + str(Rational.toContinued(a1))
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        """ Get the content of entries and passes result to the output area """

        a_val = str(a.get())
        inserter(division(a_val))

    win = Toplevel(root)
    win.title("Представление дроби в виде непрерывной")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(150, 0))
    a_lab = Label(frame, text="Введите дробь").grid(row=1, column=6)

    but = Button(frame, text="Рассчитать", width=10, command=handler).grid(row=1, column=7, padx=(100, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)
#########################################################################################################################################
def pol_sum():
    def sum(a, b):
        a1 = Polynome(str(a))
        b1 = Polynome(str(b))
        text = "( "+str(a1)+ " ) + (" + str(b1) + ") = " + str(a1 + b1)
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Сложение двух многочленов (ввод коэффициентов)")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=23)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите коэфф. первого многочлена, ввод дробный").grid(row=1, column=2)

    b = Entry(frame, width=23)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите коэфф. второго многочлена").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=100, height=20)
    output.grid(row=2, columnspan=8)

def pol_sub():
    def sum(a, b):
        a1 = Polynome(str(a))
        b1 = Polynome(str(b))
        text = "( "+str(a1)+ " ) - (" + str(b1) + ") = " + str(a1 - b1)
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Разность двух многочленов (ввод коэффициентов)")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=23)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите коэфф. первого многочлена, ввод дробный").grid(row=1, column=2)

    b = Entry(frame, width=23)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите коэфф. второго многочлена").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=100, height=20)
    output.grid(row=2, columnspan=8)

def pol_mul():
    def sum(a, b):
        a1 = Polynome(str(a))
        b1 = Polynome(str(b))
        text = "( "+str(a1)+ " ) * (" + str(b1) + ") = " + str(a1 * b1)
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Перемножение двух многочленов (ввод коэффициентов)")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=23)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите коэфф. первого многочлена, ввод дробный").grid(row=1, column=2)

    b = Entry(frame, width=23)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите коэфф. второго многочлена").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=100, height=20)
    output.grid(row=2, columnspan=8)

def pol_div():
    def sum(a, b):
        a1 = Polynome(str(a))
        b1 = Polynome(str(b))
        text = "( "+str(a1)+ " ) // (" + str(b1) + ") = " + str(a1 // b1)
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Целочисленное деление двух многочленов (ввод коэффициентов)")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=23)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите коэфф. первого многочлена, ввод дробный").grid(row=1, column=2)

    b = Entry(frame, width=23)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите коэфф. второго многочлена").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=100, height=20)
    output.grid(row=2, columnspan=8)

def pol_mod():
    def sum(a, b):
        a1 = Polynome(str(a))
        b1 = Polynome(str(b))
        text = "( "+str(a1)+ " ) % (" + str(b1) + ") = " + str(a1 % b1)
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Остаток от деления двух многочленов (ввод коэффициентов)")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=23)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите коэфф. первого многочлена, ввод дробный").grid(row=1, column=2)

    b = Entry(frame, width=23)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите коэфф. второго многочлена").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=100, height=20)
    output.grid(row=2, columnspan=8)

def pol_gcd():
    def sum(a, b):
        a1 = Polynome(str(a))
        b1 = Polynome(str(b))
        text = "GCD( [" + str(a1) + "] , [" + str(b1) + "] ) = " + str(Polynome.gcd(a1,b1))
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = str(a.get())
            b_val = str(b.get())
            inserter(sum(a_val, b_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("НОД двух многочленов (ввод коэффициентов)")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=23)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите коэфф. первого многочлена, ввод дробный").grid(row=1, column=2)

    b = Entry(frame, width=23)
    b.grid(row=1, column=3, )
    b_lab = Label(frame, text="Введите коэфф. второго многочлена").grid(row=1, column=4)
    but = Button(frame, text="Рассчитать", width=10,command = handler).grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=100, height=20)
    output.grid(row=2, columnspan=8)

def pol_der():
    def division(a):
        a1 = Polynome(str(a))
        text = "(" + str(a1) + ")'=" + str(Polynome.derivative(a1))
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        """ Get the content of entries and passes result to the output area """

        a_val = str(a.get())
        inserter(division(a_val))

    win = Toplevel(root)
    win.title("Производная многочлена")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=20)
    a.grid(row=1, column=1, padx=(150, 0))
    a_lab = Label(frame, text="Введите коэфф.").grid(row=1, column=6)

    but = Button(frame, text="Рассчитать", width=10, command=handler).grid(row=1, column=7, padx=(100, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)

def pol_nmr():
    def division(a):
        a1 = Polynome(str(a))
        text = "(" + str(a1) + ")=" + str(Polynome.nmr(a1))
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        """ Get the content of entries and passes result to the output area """
        a_val = str(a.get())
        inserter(division(a_val))

    win = Toplevel(root)
    win.title("Кратные корни в простые")
    win.resizable(width=False, height=False)
    frame = Frame(win)
    frame.grid()

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(150, 0))
    a_lab = Label(frame, text="Введите коэфф.").grid(row=1, column=6)

    but = Button(frame, text="Рассчитать", width=10, command=handler).grid(row=1, column=7, padx=(100, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=60, height=15)

    output.grid(row=2, columnspan=8)



m = Menu(root)
root.config(menu=m)

fm = Menu(m,tearoff=0) #меню для натуральных чисел
m.add_cascade(label="Натуральные числа",menu=fm)
fm.add_command(label="Сумма", command = nat_sum)
fm.add_command(label="Разность", command = nat_sub)
fm.add_command(label="Умножение", command = nat_mult)
fm.add_command(label="Деление", command = nat_DIV)
fm.add_command(label="MOD (остаток от деления)", command = nat_MOD)
fm.add_command(label="НОД", command = nat_gcd)
fm.add_command(label="НОК", command = nat_lcm)

hm = Menu(m,tearoff=0)  # второй пункт меню , целые числа
m.add_cascade(label="Целые числа",menu=hm)
hm.add_command(label="Модуль", command = int_abs)
hm.add_command(label="Сложение", command = int_sum)
hm.add_command(label="Вычитание", command = int_sub)
hm.add_command(label="Умножение", command = int_mul)
hm.add_command(label="DIV", command = int_div)
hm.add_command(label="MOD", command = int_mod)
hm.add_command(label="Возведение целого числа в степень", command = int_pow)
hm.add_command(label="Представление деления в виде a = n*q + r", command = int_qr)

dm = Menu(m,tearoff=0) #и еще один пункт, ого (Дроби)
m.add_cascade(label="Рациональные числа", menu = dm)
dm.add_command(label="Cокращение дроби", command = rat_s)
dm.add_command(label="Сложение", command = rat_sum)
dm.add_command(label="Вычитание", command = rat_sub)
dm.add_command(label="Умножение", command = rat_mul)
dm.add_command(label="Деление", command = rat_divis)

pm = Menu(m,tearoff=0) #и еще один пункт
m.add_cascade(label="Многочлены", menu = pm)
pm.add_command(label="Сложение многочленов", command = pol_sum)
pm.add_command(label="Разность многочленов", command = pol_sub)
pm.add_command(label="Умножение многочленов", command = pol_mul)
#pm.add_command(label="Деление многочленов", command = pol_divis)
pm.add_command(label="Вычисление производной", command = pol_der)
pm.add_command(label="Целая часть от деления многочленов", command = pol_div)
pm.add_command(label="Остаток от деления многочленов", command = pol_mod)
pm.add_command(label="НОД многочленов", command = pol_gcd)
pm.add_command(label="Кратные корни в простые", command = pol_nmr)

tm = Menu(m,tearoff=0)
m.add_cascade(label="Дополнительные модули", menu = tm)
tm.add_command(label="Метод Ферма", command = oth_ferma)
tm.add_command(label="Поиск примерного корня",command=oth_sqrt)
tm.add_command(label="Быстрое возведение в степень", command = oth_pow)
tm.add_command(label="Дробь в непрерывную", command = oth_toCont)

root.mainloop()
