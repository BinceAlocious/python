#7 VOWELS
def countvow(str):
    set1=set()
    count=0
    set2={'a','e','i','o','u','A','E','I','O','U'}
    for i in str:
        if(i in set2):
            count+=1
            set1.add(i)
        else:
            pass
    if(count!=0):
        print("No of vowels=",count)
    else:
        print("No Vowels Exist")
str=input("Enter String: ")
countvow(str)