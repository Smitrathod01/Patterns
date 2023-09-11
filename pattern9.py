a=int(input("Enter the number"))

for i in range(a):
    for j in range(i+1,0,-1):
        print(j,end="")
    print()

# 1
# 21
# 321