f1=open("2.txt","r")
s1=f1.readline().split(",")
print(s1)

start=int(s1[0])
end=int(s1[1])

print(type(start))
print(type(end))

print(start)
print(end)


print(type(start))
for j in range(start,end,1):
    for i in range(1,11,1):
        table1=str(j)+"*"+str(i)+"="+str(j*i)
        print(table1)
    print()

