num_lt = []
max_lt = [0,0,0]
for i in range(10):
    num = int(input())
    num_lt.append(num)
    for o in range(3):
        if(max_lt[o]<num):
            temp = max_lt[o]
            max_lt[o] = num
            num = temp
print(max_lt)

