f=open("output.txt","a")
g=open("name.txt")
h=open("phone.txt")
for i in g:
    for j in h:
        f.write(i+j)
        break
