a=5

for i in range(1,a+1):
        c=65
        print(" "* (a-i),end="")
        for j in range(i):
            print(chr(c)+" ",end="")
            c+=1
        print(" " * (a-i))

#     A like this
#   A   B
# A B C D E

#if you want a bcd efgh like then place c=65 outside i loop