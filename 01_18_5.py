
while(1):
    n = int(input())
    if(n%3!=0 and n%8!=0):
        print(f"{n}不是3也不是8的倍數")
    elif(n%3==0 and n%8==0):
        print(f"{n}是3及8的倍數")
    elif(n%8==0):
        print(f"{n}是8的倍數")
    else:
        print(f"{n}是3的倍數")