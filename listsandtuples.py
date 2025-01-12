#lists
"""marks=[ 90,67,78,98,99,34,72,90,84,76,]
name=["adil","fayaz","shakir","sameer","furqaan","fuzail","arif","raqqeb","lateef","shajaer"]
check=input("enter yes if u want to check marks of students")
if(check=="yes"):

    rollno=int(input("enter the  roll no  "))
    print(name[0])
#for el in name:
    idx=rollno-1
    print("name= ",name[idx])
    

#for m in marks:
idx1=rollno-1
print("marks= ",marks[idx1])"""
    
#wap check odd or even
num=int(input("enter the number to check odd or even "))
if(num%2==0):
   print("the number u entered is even")
else:
    print("oops u entered odd number")
#wap to find the greatest of 3 numbers
num1=int(input("enter num1 "))
num2=int(input("enter num2 "))
num3=int(input("enter num3 "))
if(num1>num2 and num1>num3):
    print(num1,"is greater")
elif(num2>num1 and num2>num3):
    print(num2,"is greater")
else:
    print(num3,"is greater")
#wap to check if number is multiple of 7
print("to check te number is multiple of 7")
number=int(input("enter the number "))
if(number%7==0):
    print(number,"is multiple of 7")
else:
    print(number,"is not multiple of 7")    
