first=float(input("enter the first number "))
op=(input("enter the operators +-*/% "))
second=float(input("enter the second element "))
if(op=="+"):
 print(first+second)
elif(op=="-"):
    print(first-second)
elif(op=="*"):
    print(first*second)
elif(op=="/"):
   print(first/second)
elif(op=="%"):
   print(first%second)
else:
    print("invalid operator try again!!")

