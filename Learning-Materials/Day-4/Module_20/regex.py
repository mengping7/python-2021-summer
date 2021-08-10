# Regex module
import re
import sys

if len(sys.argv)!=2:
    print('Usage:',sys.argv[0],'<source file>')
    sys.exit(2)

pat=r'the'
print(pat,'\n')
reg = re.compile(pat)

with open(sys.argv[1]) as sf:
    for line in sf:
        line=line[:-1]
        mo = reg.search(line)
        #mo = reg.findall(line)
        if mo:
            print(line)
            print(mo.group(),'\n')
            #print(mo,'\n')
