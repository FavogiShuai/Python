#类型和运算
- 测试类型的三种方法(推荐第三种)
```
    if type(l) == type([]):
        print('l is list')
        
    if type(l) == list:
        print('l is list')
        
    # 推荐  
    if isinstance(l, list):
        print('l is list')
```
- 数据类型
    - 哈希类型 - 不能改变的变量类型，不可变类型。可利用hash函数查看其hash值，也可作为字典的key
        - 数字类型  
            int,  float,  decimal, Decimal, fractions.Fraction, complex
        - 字符串类型  
            str, bytes
        - 元组  
            tuple
        - 冻结集合  
            frozenset
        - 布尔类型  
            True, False
    - 不可hash类型 (list, dict, set) 不可以作为字典的key
    
- 数字常量
    - 整数  
        1234，-1234，0，99999
    - 浮点数   
        1.23, 1., 3.14e-10, 4e210, 4.0e+210
    - 八进制   
        0o177
    - 十六进制  
        0x9ff, 0X9FF
    - 二进制   
        0b101010
- 集合set是一个无序不重复的元素集
    - set支持union（联合），intersection（交），difference（差），symmertric difference（对称差集）

- open函数
    - 负责打开文件，带有很多参数
    - 第一个参数必须有（文件的路径和名称）
    - mode：表明文件用什么方式打开
        - r：只读
        - w：写；会覆盖以前的内容
        - x：创建方式；如文件已存在会报错
        - a：append方式；以追加的方式对文件内容进行写入
        - b：binary方式；二进制方式写入
        - t：文本方式
        - +：可读写
# 函数
- 形参定义
    - 位置
    - 星号元组  
        functional - formal_parameter.py
    - 命名关键字  
        functional - named_keyword_parameter.py
    - 双星号字典
        functional - double_star_dict_parameter.py
- 传参
    - 序列传参
    - 关键字传参
    - 字典关键字传参  
    1.字典的键名和形参名必须一致  
    2.字典键名必须是字符串  
    3.字典的键名要在形参中存在  
- 缺省参数
    - 缺省参数必须自右至左依次存在，如果一个参数有缺省参数，则其右侧的所有参数都必须有缺省参数
    - 缺省参数可以有0个或多个，甚至全部都是缺省参数

# 作用域（LEGB）
- 局部作用域 Local function
- 外部嵌套作用域 Enclosing Function Locals
- 函数定义所在模块（文件）的作用域 Global
- Python内置模块的作用域 Builtin

# Lambda表达式（匿名函数）
- 语法：  
lambda[参数1, 参数2...]: 表达式


# 闭包
- 必须满足三个条件
    - 必须有一个内嵌函数
    - 内嵌函数必须引用外部函数的变量
    - 外部的函数的返回值必须是内嵌函数
```python
def make_power(y):
    def fx(arg):
        return arg ** y
    return fx
```
    