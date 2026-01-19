def Fibonacci(n):       #遞迴目的:計算第n項值
    if(n<=1):
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
num = int(input())
for i in range(num):
    print(Fibonacci(i),end = " ")
