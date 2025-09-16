ori =  [2, 8, 9, 48, 8, 22,-12, 2]
ans = set()
for i in ori:
    i+=2
    if i > 5:
        ans.add(i)
print(ori)
print(ans)