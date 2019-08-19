file=open("file01.txt","w+")

file.write("Alapuzha-30 ")
file.write("Thrissur-40 ")
file.write("Ernakulam-45 ")
file.write("Idukki-22 ")
file.write("Alapuzha-35 ")
file.write("Thrissur-45 ")
file.write("Ernakulam-43 ")
file.write("Idukki-20")
file.close()

f=open("file01.txt","r")
data=f.readline()
dict={}
dat=data.split(" ")
for i in dat:
    dict.update({i[:-3]:int(i[-2:])})
for i in dat:
    key=int(i[-2:])
    if(i[:-3]=="Alapuzha"):
        if(dict["Alapuzha"]<key):
            dict["Alapuzha"]=key
    elif(i[:-3]=="Thrissur"):
        if(dict["Thrissur"]<key):
            dict["Thrissur"]=key
    elif(i[:-3]=="Ernakulam"):
        if(dict["Ernakulam"]<key):
            dict["Ernakulam"]=key
    elif(i[:-3]=="Idukki"):
        if(dict["Idukki"]<key):
            dict["Idukki"]=key
print(dict)