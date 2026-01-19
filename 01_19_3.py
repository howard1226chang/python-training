n = int(input())
for i in range(n):
    str = input()
    total = 0 
    for l in range(len(str)):
        total += int(str[l])
    print(f"Sum of all digits of {str} is {total}")
