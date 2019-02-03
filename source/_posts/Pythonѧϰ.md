---
title: Python学习
date: 2018-11-10 17:56:29
tags: python
---

# 计划 #

1. 固定学习管道，mooc教程，练习python100例，Python核心编程第二版，廖雪峰python教程。
2. 熟练python特性，包括变量，条件，循环，数据类型，高阶函数（函数式编程），装饰器，函数式编程，面向对象编程。
3. 掌握二分、快排算法以及正则表达式。
4. 掌握python常用的标准库、第三方库及常用函数。
```
import sys,os,re,random,base64,md5,urllib,requests,socket,beautifulsoup,...

map(),reduce(),filter(),lambda,pprint(),...
```
5. 多写爬虫，POC，sqlmaptamper，Bruteforce之类的脚本来熟练运用。
6. 看项目写项目 `#TODO`

#  学习管道 #
https://www.imooc.com/learn/317 慕课python进阶，可以动手的教程

http://www.runoob.com/python/python-100-examples.html python100例

https://wizardforcel.gitbooks.io/core-python-2e/content/ Python 核心编程 第二版

https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000 廖雪峰python3教程（比较深 偏向开发）

http://www.runoob.com/python 菜鸟教程

#  查询管道 #

`help()`函数 #查看帮助

https://docs.python.org/3/ #官方文档 

http://www.pythondoc.com/pythontutorial3/index.html #中文文档 

其他的就是多google了


# 变量特点 #

大小写敏感，强类型，不需要声明即可使用（赋值时加上小数点即可变为浮点型，）
```
10/4 = 2

10.0/4 = 2.5
```
#  数据类型 #

list（列表）

用`[]`来声明，特点是有序、动态（同一list中可以包含str，int，float，bool多种数据形式）
`foo = ['foo',100,Ture]`

tuple（元组）
用`()`来声明，与list的唯一区别是创建后不可修改。
注意：由于`()`也是规定的优先运算符号，所以创建单元素tuple时需要使用`("foo",)`多加一个`,`。
```
#列表生成式一例
print [a*100+b*10+a for a in range(1,10) for b in range(0,10) ]
#生成121，222，232诸如此类3位对称数的列表
```
**dict**ionaries（字典）
用`{}`来声明，如字典其名，是key与value一一映射的数据类型。
特点是

1. 按key查找查找速度快，但占用内存大，与list正好相反。
2. 无序
```
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print(d)
#{'Lisa': 85, 'Adam': 95, 'Bart': 59}

```

3. key必须是不可变的数据类型，即不能是list。

```
d = {
    ['a', 'b']: True
}
print(d)

#TypeError: unhashable type: 'list'
```

4. set(组、集合)
基本就是只有key没有value的dict，判断元素是否在set中，使用in操作符。
```
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for name in L:
    if name in s:
        s.remove(name)
    else:
        s.add(name)
print s
```

# 条件判断和循环 #

**注意！判断语句后必须要有`:`，并且需要特别注意缩进！**

`if-elif-else`的多条件判断。

`for-in`的迭代遍历循环,可用于多重循环。 
```
#记得提前声明的变量才可以+=
L = range(1,101)
sum = 0
for i in L:
    sum += i*i
print sum
```

`while-continue-break`条件判断循环，利用break判断结束循环，continue判断跳过这次循环进行下一次循环。
```
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x%2 == 0:
        continue
    sum += x
print sum
```

# 切片 #

对有序的数据类型（list,tuple）可以进行切片（slipe）操作：
```
# 以下是pyhon2环境下的结果，因为py2中range()代表了一个List，py3中要使用list(range())才是一个List。
L = range(1, 101)
# 前10个数；
# 3的倍数；
# 不大于50的5的倍数。
# 最后10个数；
# 最后10个5的倍数。
print L[:10] #等同于L[0:10]
print L[2::3] 
print L[4:50:5] 
print L[-10:]
print L[-46::5]
```
对字符串的切片：
```
# 利用切片操作完成仅首字母变成大写的自定义函数
def firstCharUpper(s):
    return s[:1].upper()+s[1:]

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')
#Hello
#Sunday
#September
```

# 函数 #

## 函数特性 ##

1. python中自定义函数对全局变量的引用比较特殊。
```
sum = 0
def square_of_sum(L):
    for i in L:
        sum += i*i
    return sum
print square_of_sum([1, 2, 3, 4, 5])
# UnboundLocalError: local variable 'sum' referenced before assignment （报错：本地变量sum在赋值之前被引用了
# 说明在def定义函数之前所进行赋值的sum其实没有被引用在def中
# 不推荐使用全局变量，如若真的要使用全局变量可参考下例示范
sum = 0
def square_of_sum(L):
    for i in L:
        global sum
        sum += i*i
    return sum
print square_of_sum([1, 2, 3, 4, 5])
```

2. 在python函数的结果中返回多个值的时候其实就是返回了一个`tuple`元组。
3. 递归函数：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
```
以经典的汉诺塔问题为例
# move(n, a, b, c)表示的是有n个盘子在a柱子上，将要移到b柱子上面去
def move(n, a, b, c):
# 如果a柱子上面只有一个盘子，则直接移到c柱子上面去并输出路径，结束递归
    if n == 1:  
        print a, '-->', c
        return
# 表示的是将n-1的盘子从a柱子上面移到b柱子上面去
    move(n-1, a, c, b)
# 输出最下面个盘子移从a移到c的路径
    print a, '-->', c
# 将b柱子上面的n-1个盘子移动到c柱子上面
    move(n-1, b, a, c)

move(4, 'A', 'B', 'C')
```
4. 默认参数只能定义在必需参数的后面：
```# OK:
def fn1(a, b=1, c=2):
    pass
# Error:
def fn2(a=1, b):
    pass
```

## 常用函数 ##

### map()
高阶函数：map()将列表中的变量遍历并且一一传入第一个参数的函数中进行处理：
```
求每个数的平方
def f(x):
    return x*x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#[1, 4, 9, 16, 25, 36, 49, 64, 81]
#注意：map()函数不改变原有的 list，而是返回一个新的 list。
```
### reduce()
高阶函数：相当于传两个参数的map()
```
#求乘积
def prod(x, y):
    return x*y
print reduce(prod, [2, 4, 5, 7, 12])
#3360
```
### filter()
高阶函数：filter()，经常用于过滤作用，函数返回的bool为true则保留，为false则丢弃
```
#只取1到100中能二次开根结果为整数的值
import math

def is_sqr(x):
    return math.sqrt(x)%1==0

print filter(is_sqr, range(1, 101))
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
### 匿名函数 lambda

```
#简化代码，可以不用专门去定义一些简单的自定义函数
def is_not_empty(s):
    return s and len(s.strip()) > 0

print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
#以下代码作用相同
print filter(lambda s:s and len(s.strip())>0, ['test', None, '', 'str', '  ', 'END'])
```

### 返回函数

Python的函数不但可以返回int、str、list、dict等数据类型，还可以返回函数！
由于可以返回函数，我们在后续代码里就可以决定到底要不要调用该函数。
```
def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, lst)
    return lazy_prod
f = calc_prod([1, 2, 3, 4])
print f() #适当的延迟调用 可以优化程序运行
```
###闭包

https://www.imooc.com/code/6059 大致就是返回函数不要引用任何循环变量，或者后续会发生变化的变量。
```
def count():
    fs = []
    for i in range(1, 4):
        def f(j=i):
            return j*j
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()
```

### cmp()

比较函数，如果x,y是字符串则比较ASCII码的大小
cmp(...)
    cmp(x, y) -> integer
    
    Return -1 if x<y, 0 if x==y, 1 if x>y.

### sorted()
依从小到大（如果其中有字符串则比较ASCII码）来对list进行排序的函数，也可以作为高阶函数使用，如下例子
```
# 对字符串排序时，有时候忽略大小写排序更符合习惯。请利用sorted()高阶函数，实现忽略大小写排序的算法。

# 输入：['bob', 'about', 'Zoo', 'Credit']
# 输出：['about', 'bob', 'Credit', 'Zoo']
def cmp_ignore_case(s1, s2):
    return cmp(s1.lower(), s2.lower()) #返回1则将s1往后排

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
```

### enumerate()
enumerate() 函数可以为list建立索引：
```
#['Adam', 'Lisa', 'Bart', 'Paul']
#经过enumerate()变成了类似：
#[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
     print index, '-', name
... 
0 - Adam
1 - Lisa
2 - Bart
3 - Paul
```

### values()方法
dict 对象有一个 values() 方法，这个方法把dict转换成一个包含所有value的list，这样，我们迭代的就是 dict的每一个 value：
```
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.values()
# [85, 95, 59]
for v in d.values():
    print v
# 85
# 95
# 59
```


