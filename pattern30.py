import math
a=5
temp=math.ceil(a/2)
k=0

for i in range(a):
    if (i<temp):
        print(" "*(temp-i),end="")
        print("* "*i)
    if (i==temp):
        print("*   "*(temp-1))

for j in range(temp-1,0,-1):
        print(" "*((temp-2)+k),end="")
        print("* "*j)
        k+=1
        


#    *
#   * *  
#  *   *
#   * *
#    *