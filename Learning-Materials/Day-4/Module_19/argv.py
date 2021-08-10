# Using sys module
import sys

print(sys.argv)

# C style
for i in range(len(sys.argv)): 
    print('sys.argv[' + str(i) + '] : ' + sys.argv[i]) 
print()

# Python style
for arg in sys.argv:
    print(arg)
