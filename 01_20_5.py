num_lt1 = []
num_lt2 = []
print('Create tuple1:')
while(1):
    num = int(input())
    if(num==(-9999)):
        break
    num_lt1.append(num)
tp1=tuple(num_lt1)
print('Create tuple2:')
while(1):
    num = int(input())
    if(num==(-9999)):
        break
    num_lt2.append(num)
tp2=tuple(num_lt2)
com_tp = tp1 + tp2
print(f"Combined tuple before sorting:{com_tp}")
com_lt = sorted(com_tp)
print(f"Combined list after sorting:{com_lt}")