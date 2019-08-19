# def cartesian(lst1,lst2):
#     tup=()
#     for i in lst1:
#         for j in lst2:
#             tup=(i,j)
#             print(tup)
#
# n1=int(input("Enter Size of List 1: "))
# n2=int(input("Enter Size of List 2: "))
# lst1=[]
# lst2=[]
# for i in range(0,n1):
#     el=int(input("Enter Element of List 1: "))
#     lst1.append(el)
# for j in range(0,n2):
#     elm=int(input("Enter Element of List 2: "))
#     lst2.append(elm)
# cartesian(lst1,lst2)

#OR
A=[1,2,3]
B=[4,5,6]
cartesianproduct=[(a,b) for a in A for b in B]
print(cartesianproduct)