a, b, c= map(int, input().split())
if b >= c:
    print(-1)
else:
    profit = c - b
    i = int(a / profit)
    print(i + 1) 
        
            