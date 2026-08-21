f1=open("2.txt","r")
s1=f1.readline().split(",")

start=int(s1[0])
end=int(s1[1])


print(type(start))
for j in range(start,end,1):
    filename=str(j)+".txt"
    f2=open(filename,"w")
    for i in range(1,11,1):
        table1=str(j)+"*"+str(i)+"="+str(j*i)
        f2.write(table1)
        f2.write("\n")
        print(table1)
    print()

    f2.write("\n")
f2.close()

