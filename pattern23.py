# a=int(input("Entera no"))
a=5

for i in range(1,a+1):
        print(" "* (a-i),end="")
        print("* "*i,end="")
        print(" " * (a-i))

#     *
#    * *  
#   * * *
#  * * * *
# * * * * *