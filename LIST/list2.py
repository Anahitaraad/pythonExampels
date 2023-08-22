list = ['alaa', 37, True , 'anna', 30.5]
list.append([3, 5, 8])
list.extend([6, 7, 8])
list.pop(2)
list.insert(3,'hi')
#list.remove('alaa')
#list.reverse()
#list.sort()
m = list.count('anna')
print(m)
print(list[0])
print(list)
print(list[0:2])
#list = 'hi'
#print(list)
list = []
list += 'hello'
print(list)

a = [1,2,3]
b = a.append(4)
print(a)
print(b)