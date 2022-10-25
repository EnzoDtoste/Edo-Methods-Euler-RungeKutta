
class NumS:
    integer = ""
    decimal = ""
    negative = False

    def __init__(self, integer = '0', decimal = '', negative = False):
        
        self.integer = integer
        self.negative = negative

        for i in range(len(decimal) - 1, -1, -1):
            if decimal[i] != '0':
                self.decimal = decimal[:i+1]
                break

    def __add__(self, other):

        if (self.negative and not other.negative):
            num1 = NumS(self.integer, self.decimal)
            num2 = NumS(other.integer, other.decimal)

            if num2 < num1:
                r = self.minus(num1, num2)
                r.negative = True
                return r

            return self.minus(num2, num1)

        if (other.negative and not self.negative):
            num1 = NumS(self.integer, self.decimal)
            num2 = NumS(other.integer, other.decimal)

            if num2 < num1:
                return self.minus(num1, num2)

            r = self.minus(num2, num1)
            r.negative = True
            return r

        if (other.negative and self.negative):
            num1 = NumS(self.integer, self.decimal)
            num2 = NumS(other.integer, other.decimal)

            r = num1 + num2
            r.negative = True
            return r

        integer = ""
        decimal = ""

        arrastre = 0

        for i in range(max(len(self.decimal), len(other.decimal)) - 1, -1, -1):
             d = arrastre

             try:
                d += int(self.decimal[i])
             except:
                pass
             try:
                d += int(other.decimal[i])
             except:
                pass

             if d > 9:
               decimal = str(d)[1] + decimal
               arrastre = 1
             else:
               decimal = str(d) + decimal
               arrastre = 0

        rs = self.integer[::-1]
        ro = other.integer[::-1]

        for i in range(max(len(self.integer), len(other.integer))):
             d = arrastre

             try:
                d += int(rs[i])
             except:
                pass
             try:
                d += int(ro[i])
             except:
                pass

             if d > 9:
               integer = str(d)[1] + integer
               arrastre = 1
             else:
               integer = str(d) + integer
               arrastre = 0

        negative = self.negative and other.negative

        if arrastre == 1:
           return NumS('1' + integer, decimal, negative)
        return NumS(integer, decimal, negative)

    def __mul__(self, other):
        sumandos = []

        count = len(other.integer) + len(other.decimal) - 1

        for n in other.integer + other.decimal:
            sumandos.append('')

            arrastre = 0

            for m in (self.integer + self.decimal)[::-1]:

                mult = int(n) * int(m) + arrastre

                s = str(mult)

                if len(s) > 1:
                   sumandos[-1] = s[1] + sumandos[-1]
                   arrastre = int(s[0])

                else:
                   sumandos[-1] = s + sumandos[-1]
                   arrastre = 0

            
            if arrastre > 0:
                  sumandos[-1] = str(arrastre) + sumandos[-1]

            sumandos[-1] += '0' * count
            count -= 1

        sum = NumS(sumandos[0], '0')

        for i in range(1, len(sumandos), 1):
             sum = sum + NumS(sumandos[i], '0')

        num = NumS(sum.integer[:(len(sum.integer) - len(self.decimal) - len(other.decimal))], sum.integer[(len(sum.integer) - len(self.decimal) - len(other.decimal)):])
        
        for i in range(len(num.integer)):
            if num.integer[i] != '0':
                break

        num.integer = num.integer[i:]

        if len(num.decimal) > 25:
            num.decimal = num.decimal[:25]

        if (self.negative and not other.negative) or (other.negative and not self.negative):
            num.negative = True

        return num


    def __lt__(self, other):
        if (self.negative and not other.negative):
            return True

        if (other.negative and not self.negative):
            return False

        k = 1

        if self.negative:
            k = -1

        if k * len(self.integer) < k * len(other.integer):
            return True

        if k * len(self.integer) > k * len(other.integer):
            return False

        for i in range(len(self.integer)):
            si = k * int(self.integer[i])
            so = k * int(other.integer[i])
            if si < so:
                return True
            if si > so:
                return False

        for i in range(max(len(self.decimal), len(other.decimal))):
            try:
                si = k * int(self.decimal[i])
            except:
                return True
            try:
                so = k * int(other.decimal[i])
            except:
                return False

            if si < so:
                return True
            if si > so:
                return False

        return False


    def minus(self, num1, num2):
        integer = ""
        decimal = ""

        arrastre = 0

        for i in range(max(len(num1.decimal), len(num2.decimal)) - 1, -1, -1):
             d = arrastre

             try:
                d += int(num1.decimal[i])
             except:
                pass
             try:
                if d < int(num2.decimal[i]):
                    d += 10
                    arrastre = -1
                else:
                    arrastre = 0
                
                d -= int(num2.decimal[i])
             except:
                pass
            
             decimal = str(d) + decimal
               
        rs = num1.integer[::-1]
        ro = num2.integer[::-1]

        for i in range(max(len(num1.integer), len(num2.integer))):
             d = arrastre

             try:
                d += int(rs[i])
             except:
                pass
             try:
                if d < int(ro[i]):
                    d += 10
                    arrastre = -1
                else:
                    arrastre = 0

                d -= int(ro[i])
             except:
                arrastre = 0
                pass

             integer = str(d) + integer

        for i in range(len(integer)):
            if integer[i] != '0':
                break

        integer = integer[i:]

        return NumS(integer, decimal)


    def __sub__(self, other):
          if self.negative and other.negative:
              if other < self:
                  num1 = NumS(other.integer, other.decimal)
                  num2 = NumS(self.integer, self.decimal)
                  return self.minus(num1, num2)
              else:
                  num1 = NumS(self.integer, self.decimal)
                  num2 = NumS(other.integer, other.decimal)
                  r = self.minus(num1, num2)
                  r.negative = True
                  return r

          if not self.negative and other.negative:
              num1 = NumS(self.integer, self.decimal)
              num2 = NumS(other.integer, other.decimal)
              return num1 + num2
       
          if self.negative and not other.negative:
              num1 = NumS(self.integer, self.decimal)
              num2 = NumS(other.integer, other.decimal)
              r = num1 + num2
              r.negative = True
              return r

          if self < other:
              r = self.minus(other, self)
              r.negative = True
              return r

          return self.minus(self, other)

    def __str__(self):
        return ('-' if self.negative else '') + self.integer + ('.' + self.decimal if self.decimal != '' else '')