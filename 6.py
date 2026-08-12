start=int(input("enter your start value:"))
end=int(input("enter your end value:"))
for j in range(start,end,1):
    for i in range(1,11,1):
        table1=str(j)+"*"+str(i)+"="+str(j*i)
        print(table1)
    print()

