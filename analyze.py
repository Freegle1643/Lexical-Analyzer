# -*- coding: utf-8 -*-
import re
from punct import is_punc
from punct import puncList
from keywords import is_keyword
from ID import is_ID


myfile = raw_input()

try:
    fin = open(myfile, 'r')
except:
    print "Input file does not exists: %s" % myfile
    quit(0)



lines = fin.readlines()
if len(lines) <= 0:
    print "Input file %s is empty" % myfile
    quit(0)

def breakup_line(line):
    words = line.split()
    newwords = []
    for i in range(len(words)):
        if words[i][0] in ("'",'"') and words[i][-1] in ("'",'"'): # don't break strings
            newwords.append(words[i])
        else: # break up further based on punctuation
            t = re.findall(r"[\w]+|[^\s\w]|[-:\w]", words[i])
            newwords.extend(t)
    return newwords

def get_strings(words):
    new_words = []
    adding = False
    tmpstring = ''
    skip = False
    for w in words:
        if ('"' in w or "'" in w) and (w.count('"') < 2 and w.count("'") < 2):
            adding = not adding
        if not adding:
            new_words.append(tmpstring+w)
            tmpstring = ''
            skip = True
        if adding:
            tmpstring += w + ' '
        else:
            if skip:
                skip = False
            else:
                new_words.append(w)
    return new_words


skip = False
for line in lines:
    if '#' in line:
        line = line[:line.index('#')]
    tokens = breakup_line(line)
    final = get_strings(tokens)
    for c, item in enumerate(final):
        if not skip:
            if is_punc(item):
                try:
                    if is_punc(item + final[c+1]):
                        print '(PUNC "%s")' % str(item + final[c+1])
                        skip = True
                    else:
                        print '(PUNC "%s")' % item
                except:
                    print '(PUNC "%s")' % item
            elif is_keyword(item):
                pass
            elif is_ID(item):
                pass
            else:
                print "(LIT %s)" % item
        else:
            skip = False
print "(ENDMARKER)"
