a=4
k=0
l=0
for i in range(1,a+1):
    k=l+i 
    for j in range(i):
        print(k,end="")
        l=k
        k=k-1
    print()
    l=l+j

# 1
# 32
# 654
# 10987
    
