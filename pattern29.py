a=6

for i in range(a):
    print("  "*(a-i),end="")
    print("* " * i)
for i in range(a-2,0,-1):
    print("  "*(a-i),end="")
    print("* " * i)
