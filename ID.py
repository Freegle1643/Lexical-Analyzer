# -*- coding: utf-8 -*-
# ID.py
# 用来标识用户定义的函数中的各个变量

# 标记出所有可能被用于变量名的字符
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
"p", "q", "r", "s", "t", "u", "v", "w", "x", "z"]

uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
"S","T","U","V","W","X","Y","Z"]

digit = ["1","2","3","4","5","6","7","8","9","0","_"]

#pass in a string, if all characters are found in 3 arrays above it will be true
# 接受一个字符串输入，也就是用户定义的变量名，如果其中每个字符都在上述的3个数组中出现则返回True
def is_ID(a , cnt):
    try:
        a.index('"')
        return False
    except:
        pass
    try:
        a.index("'")
        return False
    except:
        pass
    try:
        int(a[0])
        return False
    except:
        pass
	k =  all(i in digit or uppercase or lowercase for i in a)
	if k:
   		print '<ID , "%s" , "%s">' % (a , cnt)
	return k
