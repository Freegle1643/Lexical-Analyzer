# -*- coding: utf-8 -*-
puncList = [".",";",":","!","?","/","\\",",","@","$","&",")","(","\"","#",
"[", "]", "{", "}", "=", "+=", "-=", "*=", "/=", "//=", "%=", "&=", "|=",
"^=", ">>=", "<<=", "**=", "+", '-', '==']

def is_punc(a):
    if a in puncList:
        return True
	#	print '(PUNC "%s")' % a
	return a in puncList

#if \ then punc, then ignore it
