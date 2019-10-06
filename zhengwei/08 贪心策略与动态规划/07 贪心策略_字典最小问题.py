# -*- coding: utf-8 -*-

'''
字典序最小问题
    给一个定长为N的字符串S,构造一个字符串T,长度也为N.

    起初,T是一个空串,随后返回进行下列任意的操作

    1,从S的头部删除一个字符,加到T的尾部
    2,从S的尾部删除一个字符,加到T的尾部

    目标是最后生成的字符的字典序尽可能小

1 <= N <= 2000
字符串S只包含大写英文字母

'''

'''
    Best Cow Line
Time Limit: 1000MS        Memory Limit: 65536K
Total Submissions: 32184        Accepted: 8533
Description

FJ is about to take his N (1 ≤ N ≤ 2,000) cows to the annual"Farmer of the Year" competition. In this contest every 
farmer arranges his cows in a line and herds them past the judges.

The contest organizers adopted a new registration scheme this year: simply register the initial letter of every cow in 
the order they will appear (i.e., If FJ takes Bessie, Sylvia, and Dora in that order he just registers BSD). After the 
registration phase ends, every group is judged in increasing lexicographic order according to the string of the initials
 of the cows' names.

FJ is very busy this year and has to hurry back to his farm, so he wants to be judged as early as possible. He decides 
to rearrange his cows, who have already lined up, before registering them.

FJ marks a location for a new line of the competing cows. He then proceeds to marshal the cows from the old line to the 
new one by repeatedly sending either the first or last cow in the (remainder of the) original line to the end of the new
line. When he's finished, FJ takes his cows for registration in this new order.

Given the initial order of his cows, determine the least lexicographic string of initials he can make this way.

Input

* Line 1: A single integer: N
* Lines 2..N+1: Line i+1 contains a single initial ('A'..'Z') of the cow in the ith position in the original line

Output

The least lexicographic string he can make. Every line (except perhaps the last one) contains the initials of 80 cows 
('A'..'Z') in the new line.

Sample Input

6
A
C
D
B
C
B

Sample Output

ABCBCD
'''

S = ['A', 'C', 'D', 'B', 'C', 'B', 'A']

T = ''

while S:

    if len(S) == 1:
        T += S[0]
        break

    le = 0
    ri = len(S) - 1
    # print('S is', S)

    while le < ri:
        # print('le, ri', le, ri)
        v_le = S[le]
        v_ri = S[ri]
        if v_le == v_ri:
            le += 1
            ri -= 1

        elif v_le < v_ri:
            T += S.pop(0)
            break
        else:

            T += S.pop()
            break


print('T is', T)