n = int(input("어디까지 계산할까요"))
sum = 0
for i in range(1,n+1):
    sum += i

print("1부터", n, "까지의 정수의 합 = ", sum)
