word={}
data=input("Enter String ")
dat=list(data)
for i in dat:
    if(i not in word):
        word.update({i:1})
    else:
        print("First Repeating Letter: ",i)
        break
print(word)