# -*- coding: utf-8 -*-

from functools import cmp_to_key

persons = [
    {
        'name': 'zhangsan',
        'age': 20,
        'grade': 98
    },
    {
        'name': 'lisi',
        'age': 18,
        'grade': 88
    },
    {
        'name': 'lisi',
        'age': 18,
        'grade': 98
    },
    {
        'name': 'wangwu',
        'age': 20,
        'grade': 20
    },
    {
        'name': 'yanqing',
        'age': 15,
        'grade': 20
    },
    {
        'name': 'awu',
        'age': 20,
        'grade': 20
    },
]


def cmp(a, b):
    # 如果返回的是一个大于0的值，那么代表a>b
    # 如果返回的是一个小于0的值，那么代表a<b
    # 如果返回的是一个等于0的值，那么代表a=b
    if a['grade'] > b['grade']:
        return 1

    elif a['grade'] < b['grade']:
        return -1
    else:
        if a['age'] > b['age']:
            return 1
        elif a['age'] < b['age']:
            return -1
        else:
            if a['name'] > b['name']:
                return 1
            else:
                return -1

print(persons)
# persons.sort(key=cmp_to_key(cmp))
new_persons = sorted(persons, key=cmp_to_key(cmp))

print(new_persons)
