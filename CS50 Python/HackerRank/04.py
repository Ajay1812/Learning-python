s=sorted(set(marks))
min=s[1]
records.sort()
for i,j in records:
    if(j==min):
        print(i)