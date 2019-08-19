def binarySearch(lst,el):
    lst.sort()
    low=0
    upper=len(lst)
    mid=(low+upper)//2 #Floor divi
    while(low<=upper):
            if(el<lst[mid]):
                upper=mid-1
            elif(el>lst[mid]):
                low=mid+1
            elif(el==lst[mid]):
                print("Element Found ")
                break
            mid=(low+upper)//2
lst=[]
no=int(input("Enter the Size of List "))
for i in range(0,no):
    e=int(input("Enter Element "))
    lst.append(e)
ele=int(input("Enter the Element to Search "))
binarySearch(lst,ele)
