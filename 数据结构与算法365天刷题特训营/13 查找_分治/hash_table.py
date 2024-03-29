# -*- coding: utf-8 -*-

N = 20
hash_table = [[] for _ in range(N)]


# 开始制作hash表的模式

def hash_fun(e):
    return e % N

'''
    散列函数:
        1 直接定址法 --- 需要知道关键字的一些相关的信息
        2 去留余数法 去留余数法是一种最简单,最常用的构造函数列表的方法,并且不需要事先知道关键字
            的分布.假定散列表的表长为m,取一个不大于表长的最大素数p,设计散列函数为:
                hash(key) = key % p
            为什么选择素数,是因为为了避免冲突,因为在实际的应用中,访问往往具有某种周期性,若周期性与p
            有公共的素因子,则冲突的概率将会急剧上升.
            
        3 随机数法
            hash(key) = rand(key) % p (p为素数)
            
        4 数字分析法
        
            此处略
            
        5 平方取中法
        
        6 折叠法
        
        7 基数转换法
        
        8 全域散列法
        
        
        
    散列函数解决冲突:
        
        1 开放地址法
        
            hash2(key) = (hash(key) + di) % m (di 为增量序列, m为表长)
            
            开放地址法分为: 线性探测, 二次探测, 随机探测, 再散列法
        
        2 链地址法
        
        3 建立公共溢出区
         
'''

print('hash_table', hash_table)
