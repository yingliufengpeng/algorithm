# -*- coding: utf-8 -*-

'''
    使用递归的模式来合并两个有序的数组的模式
'''


def meragesort(numsA, numsB):
    if not numsA or not numsB:
        return numsA + numsB

    a = numsA[0]
    b = numsB[0]

    if a < b:
        return [a] + meragesort(numsA[1:], numsB)
    else:
        return [b] + meragesort(numsA, numsB[1:])


nums1 = list(range(10))
nums2 = list(range(10, 20))

r = meragesort(nums1, nums2)

print('r is ', r)


'''
    关于逆序对的思路方法
    
    使用归并的思路,我们只关注右边区域当前值小于左边区域当前值,那么右边当前值 
    就小于所有左边的值
'''


