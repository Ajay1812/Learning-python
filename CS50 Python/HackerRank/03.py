n = int(input())
arr = list(map(int, input().split()))

l = []
maxscore = max(arr) 
for i in arr:
    if i != maxscore:
        l.append(i)

runner_up = max(l)
print(runner_up)