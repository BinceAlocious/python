lst=[{"Name":"Samsung","Price":100},{"Name":"Nokia","Price":90},{"Name":"Asus","Price":2000},{"Name":"Mi","Price":500},{"Name":"Apple","Price":20000}]
# dict={}
# lst1=[]
# for i in lst:
#     j=i["Price"]
#     lst1.append(j)
# lst2=[]
# lst2.append=lst1.sort()
# print(lst2)
sortedlist=sorted(lst,key=lambda i: i["Price"])
print(sortedlist)