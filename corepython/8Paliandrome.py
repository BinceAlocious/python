#8 PALINDROME
def check(no):
    n=no
    rev=0
    while(n!=0):
        digit=n%10
        rev=rev*10+digit
        n=n//10
    if(rev==no):
        print("TRUE:The Number is a Palindrome")
    else:
        print("FALSE:Not a Palindrome")

num=int(input("Enter the No to Check: "))
check(num)
