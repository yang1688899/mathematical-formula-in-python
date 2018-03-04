# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 13:23:18 2018

@author: yang
"""

"""
相关系数是用以反映变量之间相关关系密切程度的统计指标。相关系数是按积差方法计算，同样以两变量
与各自平均值的离差为基础，通过两个离差相乘来反映两变量之间相关程度；着重研究线性的单相关系数。
详细链接：http://wiki.mbalib.com/wiki/%E7%9B%B8%E5%85%B3%E7%B3%BB%E6%95%B0
"""

import numpy as np

#taken 2 numpy array as input, output the correlation_coefficent
def correlation_coefficent(lx,ly):
    if lx.shape[0] != ly.shape[0]:
        raise Exception("lx,ly must have equeal length!")
    n = lx.shape[0]
    lx_sq_sum = np.sum(np.square(lx))
    ly_sq_sum = np.sum(np.square(ly))
    lx_sum_sq = np.square(np.sum(lx))
    ly_sum_sq = np.square(np.sum(ly))
    
    numerator = n*lx.dot(ly) - np.sum(lx)*np.sum(ly)
    denominator = np.sqrt(n*lx_sq_sum-lx_sum_sq) * np.sqrt(n*ly_sq_sum-ly_sum_sq)
    
    return numerator/denominator

if __name__ == '__main__':
    a = np.array([1,2,3,5,4])
    b = np.array([2,4,6,10,8])
    print (correlation_coefficent(a,b))
    
    

    