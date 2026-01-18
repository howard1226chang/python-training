
n = int(input('請輸入欲產生的個數:'))
lt = []
for i in range(n):
    a=int(input(f'請輸入第{i+1}個數字:'))
    lt.append(a)
#sort(bubble)
for x in range(n):
    mix = lt[x]
    temp = x
    for t in range(x,n):
        if(mix>lt[t]):
            mix = lt[t]
            temp = t
    #print("即將移除",lt[temp])
    lt.remove(lt[temp])
    #print(f"{mix}要擠{lt[x]}")
    lt.insert(x,mix)
print(lt)

tp = tuple(lt)
print(tp)
st = set(lt)
print(st)