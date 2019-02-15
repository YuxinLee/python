#-*- encoding=UTF-8 -*-

"""
装饰器简介:拓展原来函数功能的一种函数，特殊之处为返回值也是一个函数
好处：在不改变元函数的代码的前提下给函数增加新的功能
"""

import time

# def func():
#     print("hello")
#     time.sleep(1)
#     print("world")

"""
对于func()函数，增加新功能即计算函数总的执行时间，最简单的方法是修改函数本身
"""
# def func():
#     startTime = time.time()
#     print("hello")
#     time.sleep(1)
#     print("world")
#     endTime = time.time()
#     msecs = (endTime - startTime) * 1000
#     print("time is %d ms" %msecs)

"""
无参装饰器的使用
"""
def deco(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print("time is %d ms" % msecs)
    return wrapper

@deco
def func():
    print("hello")
    time.sleep(1)
    print("world")

"""
有参装饰器的使用
"""
def deco(func):
    def wrapper(a,b):
        startTime = time.time()
        func(a,b)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper

@deco
def func(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))

"""
带有不定参数装饰器的使用
"""
def deco(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper

@deco
def func(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))

@deco
def func2(a,b,c):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b+c))

# func(3,4)
# func2(3,4,5)

"""
多个装饰器执行的顺序就是从最后一个装饰器开始，执行到第一个装饰器，再执行函数本身。
"""
def dec1(func):
    print("1111")
    def one():
        print("2222")
        func()
        print("3333")
    return one

def dec2(func):
    print("aaaa")
    def two():
        print("bbbb")
        func()
        print("cccc")
    return two

@dec1
@dec2
def test():
    print("test test")
test()
"""
输出结果为：
aaaa  
1111  
2222  
bbbb  
test test  
cccc  
3333
"""

"""
调用的装饰器带参数
"""
def log(level, *args, **kvargs):
    def inner(func):
        '''
        * 用来传递任意个无名字参数，这些参数会一个Tuple的形式访问
        ** 用来处理传递任意个有名字的参数，这些参数用dict来访问
        '''

        def wrapper(*args, **kvargs):
            print (level, 'before calling ', func.__name__)
            print (level, 'args', args, 'kvargs', kvargs)
            func(*args, **kvargs)
            print (level, 'end calling ', func.__name__)

        return wrapper
    return inner


@log(level='INFO')
def hello(name, age):
    print ('hello', name, age)


if __name__ == '__main__':
    func(3,4)
    func()
    hello(name='nowcoder', age=2) #= log(hello())
