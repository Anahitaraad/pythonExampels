height = input('list of students height, use space between them? ').split()
print(height)
lst = []
leng = 0
total = 0
#for x in height(0, len(height)):
#    height[x] = int( height[x])
for i in height:
    y = int(i)
    lst.append(y)
    print(y)
print(lst)

for y in lst:
    leng += 1
    total += y

print(round(total/leng))












