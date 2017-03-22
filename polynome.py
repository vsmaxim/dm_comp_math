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
        coeffs = str.split()
        self.coeffs = [Rational(i) for i in reversed(coeffs)]
    def __str__(self):
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

if __name__ == '__main__':
    x = Polynome(input())
    print(x)