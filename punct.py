# -*- coding: utf-8 -*-
# punct.py
# 用来定义所有可能出现的分隔符并确定某个输入是否是分隔符（即punctuation）

# 列举出可能的分隔符
puncList = [".",";",":","!","?","/","\\",",","@","$","&",")","(","\"","#",
"[", "]", "{", "}", "=", "+=", "-=", "*=", "/=", "//=", "%=", "&=", "|=",
"^=", ">>=", "<<=", "**=", "+", '-', '==']

# is_punc 会接受一个字符输入
# 若该字符在预先定义的puncList中则返回True
def is_punc(a):
    if a in puncList:
        return True
	#	print '(PUNC "%s")' % a
	return a in puncList

#if \ then punc, then ignore it
