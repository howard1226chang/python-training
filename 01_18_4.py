def compute(n1,n2):
    n3 = 1
    while(n2!=0):
        n3*=n1
        n2-=1
    print(n3)




a = int(input())
b = int(input())
compute(a,b)