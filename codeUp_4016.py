a, b, c = map(int,input().split())
arr = []
for i in range(1,a+1):
    if a % i == 0 and b % i == 0 and c % i == 0:
        arr.append(i)
print(max(arr))
