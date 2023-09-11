a=int(input("Enter the number"))

lastEvenNo=2*a
for i in range(a):
    for j in range(i+1):
        print(lastEvenNo,end="")
        lastEvenNo-=2
    print()
    lastEvenNo=2*a

# 10
# 108
# 1086
# 10864
# 108642


