#!/usr/bin/python
# -*- coding: UTF-8 -*-
# pow() 方法返回 xy（x的y次方） 的值。

import math

print("math.pow(100, 2) : ", math.pow(100, 2))
# 使用内置，查看输出结果区别, 内置的 pow() 方法
# pow(x, y[, z]) 函数是计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z
print("pow(100, 2) : ", pow(100, 2))
print("pow(100, 2, 99) : ", pow(100, 2, 99))

print("math.pow(100, -2) : ", math.pow(100, -2))
print("math.pow(2, 4) : ", math.pow(2, 4))
print("math.pow(3, 0) : ", math.pow(3, 0))
