count = 0
n = []
while(count<4):
    num = input()
    n.append(num)
    count+=1
    print('')   #換行
for i in range(count):
    if(i%2==0):
        print('|',end="")   #不換行
    print('%5s'%(n[i]),end="")  #靠右
    if(i%2==1):
        print('|')
    else:
        print(" ",end="")    
for t in range(count):
    if(t%2==0):
        print('|',end="")   #不換行
    print('%-5s'%(n[t]),end="")  #靠右
    if(t%2==1):
        print('|')
    else:
        print(" ",end="") 
