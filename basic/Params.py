# -*- coding: UTF-8 -*-
# ** 代表字典
params = {'job': 'wusi', 'name': 'very rich'}


def story(**kwds):
    return 'story 函数接受到的参数' '%(job)s called %(name)s.' % kwds


print story(job='wusi', name='rich')
# 注意这个地方添加**
print story(**params)
del params['name']
print story(name='yuanyuan ', **params)


def power(x, y, *others):
    if others:
        print '接受到的额外参数是:', others
    return pow(x, y)


print power(2, 3)
print power(x=3, y=2)
params = (5,) * 2
print power(*params)
print power(3, 3, 'hello world')


def interval(start, stop=None, step=1):
    '模拟 step大于0的序列'
    if stop is None:
        # 指定参数
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

print interval(10)
print interval(1, 5)
print interval(3, 12, 4)
