n = int(input('請輸入一個數字:'))
total = 0
for i in range(n+1):
    if(i%13==0):
        total+=i
print(f"從1到{n}的總和是:{total}")