l = [[10,0],[3,5],[5,8]]
li = []
for i in l:
    for j in i:
        li.append(j)
print(li)
s= 0
d= 0
x=0
for i in li:
    if x % 2 == 0:
        print(f"i for sum is {i}")
        s = s + i
        x+=1
    else:
        print(f"i for diff is {i}")
        d = d + i
        x+=1
print(f"sum {s}, diff {d}")

count = s-d
print(count)