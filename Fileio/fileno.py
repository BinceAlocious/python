f=open("no.txt")
# print(f.read())
#f.read()
for i in f:
    if(int(i)%2==0):
        print(i)