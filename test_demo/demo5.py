class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        SIN = ('-', '+')

        if not (s[0].isdigit() or s[0] in SIN):
            return 0

        sign = None

        if s[0] == '-':

            sign = False

            s = s[1:]

        elif s[0] == '+':

            s = s[1:]

            sign = True

        r = ''
        count = 0
        for e in s:
            if e.isdigit():

                r += e

            elif e == '.':

                if count == 0:

                    r += e
                    count += 1

                else:

                    break
            else:

                break

        if not r:
            return 0

        if sign == False:
            r = '-' + r

        elif sign == True:
            r = '+' + r

        # print('r is', r)
        if '.' in r:

            r = int(float(r))

        else:

            r = int(r)

        if r <= -(2 ** 31):
            r = -(2 ** 31)

        if r >= 2 ** 31 - 1:
            r = 2 ** 31 - 1

        return r


m: int = 3
print(m)
