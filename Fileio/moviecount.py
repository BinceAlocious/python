f=open("moviesdata.txt","r")
dict={}
lst=[]
f.readline()
for i in f:
    lst.append(i[:-2].split(","))
for j in lst:
    if(j[2] not in dict):
        dict.update({j[2]:1})
    else:
        count=int(dict[j[2]])
        count+=1
        dict[j[2]]=count
print(dict)