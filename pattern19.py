a=int(input("Enter the number"))

for i in range(a):
    k=1
    for j in range((2*i)+1):
        print(k,end="")
        k*=2
    print()

# 1
# 124
# 124816
# 1248163264