# -*- coding: utf-8 -*-

class Solution:

    count = 0

    def op(self, op, x, y):
        # print('op ...')

        if op == '+':

            return x + y

        elif op == '-':

            return x - y

        elif op == '*':

            return x * y

        elif op == '/':

            return x // y

        else:
            pass

    def calculate(self, s: str) -> int:

        nums_sta = []

        op_sta = []

        index = 0

        n = len(s)

        m = ''

        while index < n:

            v = s[index]

            if v.isdigit():

                m += v

                if index + 1 < n and not s[index + 1].isdigit():
                    nums_sta.append(int(m))

                    m = ''
                elif index + 1 == n:

                    nums_sta.append(int(m))

                    m = ''

            elif v in ('+', '-'):

                if not op_sta:

                    op_sta.append(v)

                else:
                    while True:
                        if not op_sta:

                            break

                        op = op_sta.pop()

                        sec = nums_sta.pop()

                        fir = nums_sta.pop()

                        r = self.op(op, fir, sec)

                        nums_sta.append(r)

                    op_sta = [v]




            elif v in ('*', '/'):

                if not op_sta:

                    op_sta.append(v)

                else:

                    if op_sta[-1] in ('*', '/'):

                        op = op_sta.pop()

                        sec = nums_sta.pop()

                        fir = nums_sta.pop()

                        r = self.op(op, fir, sec)

                        nums_sta.append(r)

                        op_sta.append(v)

                    elif op_sta[-1] in ('+', '-'):

                        op_sta.append(v)

                    else:

                        pass

            else:

                pass

            # print('*' * 100, self.count)
            # self.count += 1
            # print('nums_sta', nums_sta)
            # print('op_sta', op_sta)

            index += 1

        while op_sta:

            if op_sta[-1] in ('*', '/'):
                op = op_sta.pop()

                sec = nums_sta.pop()

                fir = nums_sta.pop()

                r = self.op(op, fir, sec)

                nums_sta.append(r)

                continue

            fir = nums_sta.pop(0)

            sec = nums_sta.pop(0)

            op = op_sta.pop(0)

            r = self.op(op, fir, sec)

            nums_sta.insert(0, r)
        #
        # print(op_sta)
        # print(nums_sta)

        return nums_sta[0]


s = Solution()

a = "282-1*2*13-30-2*2*2/2-95/5*2+55+804+3024"

r = s.calculate(a)

print('r is', r)
