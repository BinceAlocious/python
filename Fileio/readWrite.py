f=open("append.txt",'r')
g=open("new.txt","a")
g.write(f.read())