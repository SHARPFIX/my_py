#lists
marks=[ 90,67,78,98,99,34,72,90,84,76,]
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
print("marks= ",marks[idx1])
    
