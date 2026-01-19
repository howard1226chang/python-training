n = []
total = 0
for i in range(5):
    num = input()
    n.append(num)
    if(n[i]=='J'):
        total += 11
    elif(n[i]=='Q'):
        total +=12
    elif(n[i]=='K'):
        total +=13
    elif(n[i]=='A'):
        total +=1
    else:
        total +=int(n[i])
print(total)
