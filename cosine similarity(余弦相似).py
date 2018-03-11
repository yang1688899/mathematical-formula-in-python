# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 18:06:34 2018

@author: yang
"""
"""
余弦相似度，又称为余弦相似性，是通过计算两个向量的夹角余弦值来评估他们的相似度。
详细：https://baike.baidu.com/item/%E4%BD%99%E5%BC%A6%E7%9B%B8%E4%BC%BC%E5%BA%A6/17509249?fr=aladdin
"""
import numpy as np

#taken 2 numpy array as input, output the cosine similarity of this 2 vector
def cosine_similarity(a,b):
    a_sq_sum = np.sum(np.square(a))
    b_sq_sum = np.sum(np.square(b))
    return a.dot(b)/(np.sqrt(a_sq_sum)*np.sqrt(b_sq_sum))

if __name__ == "__main__":
    a = np.array([3,5,4])
    b = np.array([4,3,5])
    print (cosine_similarity(a,b))