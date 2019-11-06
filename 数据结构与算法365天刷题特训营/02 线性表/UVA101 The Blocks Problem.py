# -*- coding: utf-8 -*-

'''
    题意翻译
初始时从左到右有n个木块，编号为0~n-1,要求实现下列四种操作:

move a onto b: 把a和b上方的木块全部放回初始的位置，然后把a放到b上面
move a over b: 把a上方的木块全部放回初始的位置，然后把a放在b所在木块堆的最上方
pile a onto b: 把b上方的木块部放回初始的位置，然后把a和a上面所有的木块整体放到b上面
pile a over b: 把a和a上面所有的木块整体放在b所在木块堆的最上方
一组数据的结束标志为"quit"，如果有非法指令(a和b在同一堆)，应当忽略。

输出:所有操作输入完毕后，从左到右，从下到上输出每个位置的木块编号。 感谢U27114 jxdql2001 提供的翻译
'''


'''
    题解: 
        通过四种操作可以归纳总结出规律:
            move: a上方的木块全部放回初始的位置
            onto: b上方的目前全部放回初始的位置
            公共操作: a和a上面的所有的木块整体放在b所在的木块堆的最上方
            
            而实际上,前两种操作可以算一个操作: a(或b)上木块全部放回初始位置的操作,
            简称归位.a和a上面所有的木块整体放在b所在的木块堆的最上方,简称移动.
            
            我们只需要判断执行归位和移动的操作就可以了!!
            
'''

n = 10

nums = [[i] for i in range(n)]


def issamestack(nums, a, b) -> bool:
    for i in range(n):

        if a in nums[i] and b in nums[i]:
            return True

    return False


def moveAontoB(nums, a, b):
    # 数据相同
    if a == b:
        return

    # 在同一个栈中!!!
    if issamestack(nums, a, b):
        return

    for e in nums[a][1:]:
        nums[e].append(e)

    for e in nums[b][1:]:
        nums[e].append(e)

    nums[a].pop()
    nums[b].append(a)


def moveAoverB(nums, a, b):
    # 数据相同
    if a == b:
        return

    # 在同一个栈中!!!
    if issamestack(nums, a, b):
        return

    for e in nums[a][1:]:
        nums[e].append(e)

    for vs in nums:

        if b in vs:
            nums[a].pop()

            vs.append(a)

            break


def pileAontoB(nums, a, b):
    # 数据相同
    if a == b:
        return

    # 在同一个栈中!!!
    if issamestack(nums, a, b):
        return

    aas = []

    for i in range(n):

        if a in nums[i]:
            index = nums[i].index(a)

            aas.extend(nums[i][index:])

            nums[i] = nums[i][: index]

            break

    for e in nums[b][1:]:
        nums[e].append(e)

    nums[b].extend(aas)


def pileAoverB(nums, a, b):
    # 数据相同
    if a == b:
        return

    # 在同一个栈中!!!
    if issamestack(nums, a, b):
        return

    aas = []

    for i in range(n):

        if a in nums[i]:
            index = nums[i].index(a)

            aas.extend(nums[i][index:])

            nums[i] = nums[i][: index]

            break

    for i in range(n):

        if b in nums[i]:
            nums[i].extend(aas)


ss = '''
move 9 onto 1
move 8 over 1
move 7 over 1
move 6 over 1
pile 8 over 6
pile 8 over 5
move 2 over 1
move 4 over 9
quit
'''
i = 0

ss = ss.strip().split('\n')
while True:

    # s = input()
    s = ss[i]

    if s == 'quit':
        break

    s = s.split()

    # print('s is', s)
    i += 1

    a, b = int(s[1]), int(s[3])

    if 'move' in s and 'onto' in s:

        moveAontoB(nums, a, b)

    elif 'move' in s and 'over' in s:

        moveAoverB(nums, a, b)

    elif 'pile' in s and 'onto' in s:

        pileAontoB(nums, a, b)

    elif 'pile' in s and 'over' in s:

        pileAoverB(nums, a, b)

    else:

        pass

for i, vs in enumerate(nums):

    print('{}: {}'.format(i, ' '.join(str(e) for e in vs)))