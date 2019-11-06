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


def loc(nums, a) -> (int, int):  # a所在的堆的索引以及返回的a包括a所在的堆中的索引

    # print('nums {} a {}'.format(nums, a))

    for i, vs in enumerate(nums):

        if a in vs:
            return i, vs.index(a)

    raise Exception('不可能的错误!!!')


def goback(nums, index, h):
    vs = nums[index]

    for e in vs[h + 1:]:
        nums[e].append(e)

    nums[index] = vs[: h + 1]


def move_all(nums, indexa, h, indexb):  # 这里的h代表的是在indexa所在的高于a的索引值,
    # print('nums before is', nums)
    # print('indexa {} h {} indexb {}'.format(indexa, h, indexb))

    vas = nums[indexa]

    vbs = nums[indexb]

    vbs.extend(vas[h:])

    nums[indexa] = vas[: h]

    # print('nums', nums)


def issamestack(nums, a, b) -> bool:
    for i in range(n):

        if a in nums[i] and b in nums[i]:
            return True

    return False


ss = '''
move 9 onto 1
move 8 over 1
move 7 over 1
move 6 over 1
pile 8 over 6
pile 8 over 5
move 2 over 1
move 4 over 9
move 9 into 8
move 9 into 4
pile 3 into 2
pile 4 over 9
quit
'''
i = 0

ss = ss.strip().split('\n')

while True:

    # s = input()
    s = ss[i]
    # print('s is', s)
    i += 1

    if s[0] == '#':

        continue

    if s == 'quit':
        break
    #
    # if i == 2:
    #     break

    s = s.split()

    a, b = int(s[1]), int(s[3])

    # 查找a所在的堆
    indexa, ha = loc(nums, a)

    # 查找b所在的堆
    indexb, hb = loc(nums, b)

    # 只有两者不在同一个位置的时候我们做如下的操作!!!
    if indexa != indexb:

        if 'move' in s:
            goback(nums, indexa, ha)

        if 'onto' in s:
            goback(nums, indexb, hb)

        # 切记goback之后并没有更新ha和hb相关的值!!!

        move_all(nums, indexa, ha, indexb)

        # print('nums is', nums)

for i, vs in enumerate(nums):
    print('{}: {}'.format(i, ' '.join(str(e) for e in vs)))
