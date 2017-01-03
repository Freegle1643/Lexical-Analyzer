# -*- coding: utf-8 -*-
# analyze.py
# 用于词法分析的主程序
import re
from punct import is_punc
from punct import puncList
from keywords import is_keyword
from ID import is_ID


# 定义需要打开分析的程序文件
workfile = raw_input("Enter Python file (.py) fullname: ")

# 对于打开文件异常的处理
try:
    fin = open(workfile, 'r')
except:
    print "Input file does not exists: %s" % workfile
    quit(0)


# 对于可以打开的文件，但是文件内容为空的异常处理
lines = fin.readlines()
if len(lines) <= 0:
    print "Input file %s is empty" % workfile
    quit(0)


def breakup_line(line):
    # 将程序中的所有词都分开，存入words，但这里可能有误入的符号，如引号
    words = line.split()
    newwords = []
    # 对于words中的所有词，用for循环做如下处理
    for i in range(len(words)):
        if words[i][0] in ("'",'"') and words[i][-1] in ("'",'"'):
            # 有引号就不算单个word，并入所包含的词
            newwords.append(words[i])
        else: # 没有引号就正常的分割开来
            t = re.findall(r"[\w]+|[^\s\w]|[-:\w]", words[i])
            newwords.extend(t) # 在末尾追加我们分割的word
    return newwords

def get_strings(words):
    new_words = []
    adding = False
    tmpstring = ''
    skip = False
    for w in words:
        if ('"' in w or "'" in w) and (w.count('"') < 2 and w.count("'") < 2):
            # 如果分出来的是包含了引号的，我们需要等待闭合
            adding = not adding
        if not adding:
            # 所以先把这部分存到tmpstring中
            new_words.append(tmpstring+w)
            tmpstring = ''
            skip = True
        if adding:
            # 我们把需要加入的词前后加入空格再插入
            tmpstring += w + ' '
        else:
            if skip:
                # 如果是引号，不加入，看看下面是啥
                skip = False
            else:
                # 其他情况就加入即可
                new_words.append(w)
    return new_words


skip = False
# 设置一个计数器，用来打印内部码
cnt = 0
print "<Category , Words , Inner Code>"
# 对于文件内的程序进行逐行分析
for line in lines:
    if '#' in line:
        # "#"开头的是Python程序中的注释部分
        # 就把这行从"#"后截断，只保留前面的部分
        line = line[:line.index('#')]
    # 先分割开来
    tokens = breakup_line(line)
    # 然后再处理为有意义的多个词
    final = get_strings(tokens)

    for c, item in enumerate(final):
        cnt += 1
        # print cnt
        if not skip:
            if is_punc(item):
                try:
                    if is_punc(item + final[c+1]):
                        print '<PUNC , "%s" , "%s">' % (str(item + final[c+1]) , cnt)
                        skip = True
                    else:
                        print '<PUNC , "%s" , "%s">' % (item , cnt)
                except:
                    print '<PUNC , "%s" , "%s">' % (item , cnt)
            elif is_keyword(item , cnt):
                pass
            elif is_ID(item , cnt):
                pass
            else:
                print '<LIT , "%s" , "%s">' % (item , cnt)
        else:
            skip = False
print "<END OF FILE>"
