from integer import Integer
from naturals import Natural

class Rational:
    def __init__(self, str):
        a = str.split('/')
        self.numer = Integer(a[0])
        self.denom = Integer(a[1])
    def __str__(self):
        return '{}/{}'.format(self.numer, self.denom)
if __name__ == '__main__':
    a = Rational(input())
    print(a)