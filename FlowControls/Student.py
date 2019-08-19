#Input marks and print Grade of Student
math=int(input("Enter Marks in maths "))
sc=int(input("Enter Marks in Science "))
comp=int(input("Enter Marks in Computer Science "))
sum=math+sc+comp
if(sum>140):
    print("Grade A+")
elif(sum>130&sum<=140):
    print("Grade A")
elif(sum>120&sum<=130):
    print("Grade B+")
elif(sum>110&sum<=120):
    print("Grade B")
elif(sum>100&sum<=110):
    print("Grade C+")
elif(sum>90&sum<=100):
    print("Grade C")
else:
    print("Grade F")
