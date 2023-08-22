animals = ['cow','rabbit','rabbit', 'monkey']
print(animals)

animals.append('owl')
print(animals)

animals.insert(3,'dog')
print(animals)

animals.copy()
print(animals)

print(animals.index('monkey'))

print(animals.count('rabbit'))

animals.pop(1)
print(animals)

#print(animals.pop(1))
animals.remove('cow')
print(animals)

animals.reverse()
print(animals)
#sort works for a list with just integers or strings
animals.sort()
print(animals)

numbers = [1, 4, 5, 2, 3]
print(max(numbers))
print(min(numbers))
print(sum(numbers))