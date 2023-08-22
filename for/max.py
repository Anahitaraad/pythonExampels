lst = input('enter ur numbers? ').split()
print(lst)
mx = 0
for i in range(0, len(lst)):
    lst[i] = int(lst[i])

for i in lst:
    if i > mx:
        mx = i
print(mx)



