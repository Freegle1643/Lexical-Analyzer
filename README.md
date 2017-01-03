# Python Lexical Analyzer

## Info
This is a Python based Lexical Analyzer to do lexical analysis on a Python program. Cuz I'm Chinese, I wrote full Chinese comment in my code.

## Usage
- Download the project and run `analyze.py`
- Enter the Python file you want to do lexical analysis. I created for you as `example.py`. You can definitely add other files.
- Hit `Enter` key to see result in a form of `<Category , Words , Inner Code>`

## Further modification and extension
If you want to modify the project and transform it to lexical analysis for other language. Here are two ways you would like to try:
1. Change `keywords.py` (or `ID.py` and `punct.py` if necessary)to the language you want accordingly.
2. Add more Python file to manipulate keywords, punctuation and so on. Then you will need to add some codes in `analyze.py` so that it knows which files to use.
### Change details
You may need to change the following code segments for lexical analysis on other languages.

`keywords.py`
```Python
keyword = ['and', 'as', 'assert', 'break', 'class', 'def', 'del',
'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global','if', 'import',
'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

`punct.py`
```Python
puncList = [".",";",":","!","?","/","\\",",","@","$","&",")","(","\"","#",
"[", "]", "{", "}", "=", "+=", "-=", "*=", "/=", "//=", "%=", "&=", "|=",
"^=", ">>=", "<<=", "**=", "+", '-', '==']
```
