h, m = map(int,input().split())
if m < 30:
    if h <= 0:
        h = 23
    else:
        h = h-1
    m = m+30
else:
    m = m-30
print(h,m)
