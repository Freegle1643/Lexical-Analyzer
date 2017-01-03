# -*- coding: utf-8 -*-
# keywords.py
# 用来声明可能出现的Python语言中的关键字，如def, import, try等

# 列举可能的关键字
keyword = ['and', 'as', 'assert', 'break', 'class', 'def', 'del',
'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global','if', 'import',
'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']

# is_keyword接受一个字符输入
# 如果这是一个我们定义的关键字，则打印它并返回
def is_keyword(a , cnt):
    if a in keyword:
        print '<KEYWORD , "%s" , "%s">' % (a , cnt)
    return a in keyword
