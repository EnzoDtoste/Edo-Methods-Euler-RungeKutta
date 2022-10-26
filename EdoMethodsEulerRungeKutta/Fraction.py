class Fraction:
    numerator = 0
    denominator = 0

    def __init__(self, numerator, denominator):
       self.numerator = numerator
       self.denominator = denominator


    def __add__(self, other):
        numerator = other.denominator * self.numerator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = other.denominator * self.numerator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __iadd__(self, other):
        numerator = other.denominator * self.numerator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __isub__(self, other):
        numerator = other.denominator * self.numerator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __imul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __itruediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)


    @property
    def reduce(self):
        if self.numerator % self.denominator == 0:
            self.numerator //= self.denominator
            self.denominator = 1
            return True

        primes = [2,3,5,7,11]

        reduced = False

        for prime in primes:
        
          if self.numerator % prime == 0 and self.denominator % prime == 0:
            self.numerator //= prime
            self.denominator //= prime
            reduced = True

        return reduced

    @property
    def fullReduce(self):
        while self.reduce:
            if self.denominator == 1:
               return

    @property
    def value(self):
        return self.numerator / self.denominator

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)

        return str(self.numerator) + "/" + str(self.denominator)




