a=int(input("Enter the number"))

for i in range(a):
    print(" "*(a-i-1),end="")
    for j in range(i+1):
        
        print(j+1,end="")
    print()

#    1
#   12
#  123
# 1234