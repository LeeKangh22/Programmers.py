a, b = map(int, input().strip().split(' '))
s = ''
for i in range(0, b):
    for i in range(0, a):
        s += '*'
    print(s)
    s = ''