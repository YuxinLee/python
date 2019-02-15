# -*- encoding=UTF-8 -*-
import requests
import random
import re
from bs4 import BeautifulSoup

"""
python基础语法简介
"""
def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print (div.text.strip())


def demo_string():
    stra = 'hello world'
    print (stra.capitalize())   #首字母大写
    print (stra.replace('world', 'nowcoder'))
    strb = '  \n\rhello nowcoder \r \n'
    print (1, strb.lstrip())
    print (2, strb.rstrip())
    strc = 'hello w'
    print (3, strc.startswith('hel'))
    print (4, strc.endswith('x'))
    print (5, stra + strb + strc)
    print (6, len(strc))
    print (7, '-'.join(['a', 'b', 'c']))    #a-b-c
    print (8, strc.split(' '))
    print (9, strc.find('ello'))    #1


def demo_operation():
    print (1, 1 + 2, 5 / 2, 5 * 2, 5 - 2)
    print (2, True, not True)
    print (3, 1 < 2, 5 > 2)
    print (4, 2 << 3)
    print (5, 5 | 3, 5 & 3, 5 ^ 3)
    x = 2
    y = 3.3
    print (x, y, type(x), type(y))


def demo_buildinfunction():
    print (1, max(2, 1), min(5, 3))
    print (2, len('xxx'), len([1, 2, 3]))
    print (3, abs(-2))  # fabs,Math.fabs
    print (4, range(1, 10, 3))
    print (5, dir(list))
    x = 2
    print (6, eval('x + 3'))    #执行
    print (7, chr(65), ord('a'))    #A 97
    print (8, divmod(11, 3))    #11/3 = (3,2)


def demo_controlflow():
    score = 65
    if score > 99:
        print (1, 'A')
    elif score > 60:
        print (2, 'B')
    else:
        print (3, 'C')

    while score < 100:
        print (score)
        score += 10
    score = 65

    # for (int i = 0; i < 10; ++i)
    # continue ,break, pass
    for i in range(0, 10, 2):
        if i == 0:
            pass  # do_special
            # print 3, i
        if i < 5:
            continue
        print (3, i)
        if i == 6:
            break


def demo_list():
    lista = [1, 2, 3]  # vector<int> Arraylist
    print (1, lista)
    listb = [4, 5, 6, 3]
    print (2, listb)
    lista.extend(listb)     #扩展
    print (3, lista)
    print (4, len(lista))
    print (5, 10 in listb)
    lista = lista + listb   #扩展
    print (6, lista)
    listb.insert(0, 10)
    print (7, listb)
    listb.pop(1)    #第一位弹出
    print (8, listb)
    listb.reverse()
    print (9, listb)
    print (10, listb[0], listb[1])
    listb.sort()
    print (11, listb)
    listb.sort(reverse=True)
    print (12, listb)
    print (13, listb * 2)   #列表扩展为原来的2倍
    print (14, [0] * 14)  # memset(src, 0, len)
    tuplea = (1, 2, 3)  #只读
    listaa = [1, 2, 3]
    listaa.append(4)
    print (15, listaa)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def demo_dict():
    dicta = {4: 16, 1: 1, 2: 4, 3: 9}
    print (1, dicta)
    print (2, dicta.keys(), dicta.values())     #输出字典的键和值
    print(dicta.get(2))
    # for map<int,int>::iterator it = x.begin(); it != x.end()
    for key, value in dicta.items():        #遍历字典
        print ('key-value:', key, value)
    dictb = {'+': add, '-': sub}    #字典的值为函数
    print (4, dictb['+'](1, 2))     #调用add方法
    print (5, dictb.get('-')(15, 3))    #调用sub方法
    dictb['*'] = 'x'
    print (dictb)
    dicta.pop(4)
    print (6, dicta)
    del dicta[1]
    print (7, dicta)


def demo_set():
    lista = [1, 2, 3]
    seta = set(lista)
    setb = set((2, 3, 4))
    print (1, seta)
    print (3, seta.intersection(setb), seta & setb)     #交集
    print (4, seta | setb, seta.union(setb))    #并集
    print (5, seta - setb)  #{1}
    seta.add('x')   #{1, 2, 3, 'x'}
    print (6, seta)
    print (len(seta))
    print (seta.isdisjoint(set((1, 2))))


class User:
    type = 'USER'

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    #__repr__类似于java中的toString()
    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid)


class Guest(User):
    def __repr__(self):
        return 'im guest:' + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid, group):
        #调用父类的构造方法
        User.__init__(self, name, uid)
        self.group = group

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid) + ' ' + self.group

#多态方法
def create_user(type):
    if type == 'USER':
        return User('u1', 1)
    elif type == 'ADMIN':
        return Admin('a1', 101, 'g1')
    else:
        return Guest('gu1', 201)
        # raise ValueError('error')


def demo_exception():
    try:
        print (2 / 1)
        # print 2 / 0
        # if type == 'c':
        raise Exception('Raise Error', 'NowCoder')
    except Exception as e:
        print ('error:', e)
    finally:
        print ('clean up')


def demo_random():
    # 1 - 100
    # random.seed(1) 如果seed()指定的话，那么随机数将被固定
    # x = prex * 100007 % xxxx
    # prex  = x 幂等性
    #random()为0-1之间的浮点数
    print (1, int(random.random() * 100))
    print (2, random.randint(0, 200))
    print (3, random.choice(range(0, 100, 10)))     #10
    print (4, random.sample(range(0, 100), 4))      #[24, 88, 59, 70]
    a = [1, 2, 3, 4, 5]
    random.shuffle(a)
    print (5, a)        #[3, 2, 5, 4, 1] 打乱顺序

#正则表达式
def demo_re():
    str = 'abc123def12gh15'
    p1 = re.compile('[\d]+')    #\d表示数字
    p2 = re.compile('\d')
    print (1, p1.findall(str))  #['123', '12', '15'] 匹配数字
    print (2, p2.findall(str))  #['1', '2', '3', '1', '2', '1', '5']    匹配单个数字
    # \t\n
    str = 'a@163.com;b@gmail.com;c@qq.com;e0@163.com;z@qq.com'
    p3 = re.compile('[\w]+@[163|qq]+\.com')     #\w表示字母或数字
    print (3, p3.findall(str))      #['a@163.com', 'c@qq.com', 'e0@163.com', 'z@qq.com']

    str = '<html><h>title</h><body>xxx</body></html>'
    p4 = re.compile('<h>[^<]+</h>')     #^非
    print (4, p4.findall(str))      #['<h>title</h>']
    p4 = re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print (5, p4.findall(str))      #[('title', 'xxx')]

    str = 'xx2016-06-11yy'
    p5 = re.compile('\d{4}-\d{2}-\d{2}')
    print (p5.findall(str))     #['2016-06-11']

if __name__ == '__main__':
    '''
    user1 = User('u1', 1)
    print user1
    admin1 = Admin('a1', 101, 'g1')
    print admin1

    print create_user('USERX')
    '''

    # print 'hello nowcoder'
    # comment
    # demo_string()
    # demo_operation()
    # demo_buildinfunction()
    # demo_controlflow()
    # demo_list()
    # demo_dict()
    # demo_set()
    # demo_exception()
    # demo_random()
    demo_re()
