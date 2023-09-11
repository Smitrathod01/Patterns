#print(chr(65))  #A#
#print(chr(97))  #a#

a=5
c=65
for i in range(a):
    for j in range(i+1):
        print(chr(c),end="")
        c+=1
    print()

# A
# BC
# DEF
# GHIJ

a=5
c=65
for i in range(a):
    
    for j in range(i+1):
        print(chr(c),end="")
        
    print()
    c+=1