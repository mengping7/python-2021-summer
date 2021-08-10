# Using sys and os modules
import sys
import os

if len(sys.argv) != 2:
    print('Usage:',sys.argv[0],'<directory>')
    sys.exit(2)

dfiles = os.listdir(sys.argv[1])

print(sys.argv[1],':')
for f in dfiles: 
    print('    ',f)
