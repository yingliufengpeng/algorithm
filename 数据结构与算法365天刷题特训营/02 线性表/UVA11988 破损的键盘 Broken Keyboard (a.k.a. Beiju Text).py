# -*- coding: utf-8 -*-

'''
    题意翻译
你在输入文章的时候，键盘上的Home键和End键出了问题，会不定时的按下。你却不知道此问题，而是专心致志地打稿子，甚至显示器都没开。
当你打开显示器之后，展现你面前的数一段悲剧文本。你的任务是在显示器打开前计算出这段悲剧的文本。 给你一段按键的文本，其中'['表示Home键，
']'表示End键，输入结束标志是文件结束符（EOF）。

输出一行，即这段悲剧文本。 翻译贡献者UID：71371
'''

# s = '''
#     This_is_a_[Beiju]_text
# [[]][][]Happy_Birthday_to_Tsinghua_University
# '''.strip()
#
#
# s = '[' + s + ']'
#
# print('s is', s)
#
# res = []
#
# sta = []
# i = 0
#
# while i < len(s):
#
#     e = s[i]
#
#     if s[i] == '[':
#
#         sta.append([])
#
#     elif s[i] == ']':
#
#         r = sta.pop()
#
#         res.extend(r)
#
#     else:
#
#         sta[-1].append(e)
#
#     i += 1
#
# # for vs in res:
# # #
# # #     print(vs)
#
# print(''.join(res))


# 官方的解答方案!!!

s = '''This_is_a_[Beiju]_text
[[]][][]Happy_Birthday_to_Tsinghua_University
'''

def process(s):
    res = []

    index = 0

    for e in s:

        if e == '[':

            index = 0

        elif e == ']':

            index = len(res)

        else:

            res.insert(index, e)

            index += 1

    # print('res', ''.join(res))

    return ''.join(res)


# res = []
#
# for vs in s.split('\n'):
#
#     res.append(process(vs))
#
#
# print('\n'.join(res))


s = 'This_is_a_[Beiju]_text'

r = process(s)

print(r)