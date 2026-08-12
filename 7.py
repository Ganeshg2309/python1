f1=open("1.txt","r")

start=int(f1.readline())
end=int(f1.readline())

print("value of start:",start)
print("value of end:",end)

print(type(start))
for j in range(start,end,1):
    for i in range(1,11,1):
        table1=str(j)+"*"+str(i)+"="+str(j*i)
        print(table1)
    print()

