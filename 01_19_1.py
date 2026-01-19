def Valid(a,b,c):
    if(a<b+c):
        print(a+b+c)
    else:
        print("Invalid")
n1,n2,n3 = int(input()),int(input()),int(input())
max = n1
if(n1>n2 and n1>n3):
    Valid(n1,n2,n3)
elif(n2>n1 and n2>n3):
    Valid(n2,n1,n3)
else:
    Valid(n3,n1,n2)
