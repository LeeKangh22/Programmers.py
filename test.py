s='a b c'
s.split()
for i in range(0, len(s)):
    for j in range(0, len(s[i])):
        print(s[i][j].upper())
