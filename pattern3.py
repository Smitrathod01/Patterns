a=int(input("Enter the no : \n"))

for i in range(a):
    print(" "*(a-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(a-i-1))

#    *
#   ***
#  ******