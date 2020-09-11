a = int(input())
b = int(input())
c = int(input())
d = int(input())
for j in range (c,d+1):
    print(" ", j, sep="\t",end="")
for i in range(a,b + 1):
    print("\n",i,end="\t")
    for j in range (c,d+1):
        print(i * j, end="\t")

