# def toup(lst):
#     lst2=[]
#     for i in lst:
#         lst2.append(i.upper())
#     print(lst2)
# lst=["Sachin","Rahul","Vivek","Schwaz"]
# toup(lst)

def solve(s):
    lst=[]
    str=s.split(" ")
    for i in str:
        lst.append(i.capitalize())

s=input("Enter String ")
solve(s)