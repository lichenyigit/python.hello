# 字符串
a = 'hello word';
b = 'python 你好';

print("a[0]", a[0])
print('b[0]', b[8]);

# 字符串运算符
'''
+   字符串连接
*   重复输入字符串
[]  通过索引获取字符串中字符
[:] 截取字符串中的一部分
in  成员运算符-如果包含该字符返回Ture
not in  成员运算符-如果不包含改字符返回True
r/R 原始字符串-原始

'''

print("a + b 输出结果：", a + b)
print(
    "a * 2 输出结果：", a * 2)
print(
    "a[1] 输出结果：", a[1])
print(
    "a[1:4] 输出结果：", a[1:4])

if ("H" in a):
    print(
        "H 在变量 a 中")
else:
    print(
        "H 不在变量 a 中")

if ("M" not in a):
    print(
        "M 不在变量 a 中")
else:
    print(
        "M 在变量 a 中")

print(
    r'\n')
print(
    R'\n')

