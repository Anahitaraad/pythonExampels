#list= ['koala','cat','fox','panda']
#for item in list:
   # print(item)

#list2 = ['alaa','fred','xia','anna','yasi']
#for name in list2:
    #print(f'hello, {name}')

str = 'sweden'
list3 = []
for letter in str:
    print(letter)
    list3.append(letter + ',')
    print(letter)
#print(''.join(list3))
#print(str + list3[0] , 'test')
#print(str + list3[5] , 'ok')

list4 =['Phill','Oz','Dre']
list_4 = []
for element in list4:
    list_4.append(f'Dr. {element}')
print(list_4)

lst1 = [3.14, 66, 'Teddy',True , [],{}]
lst2 = []
for items in lst1:
    lst2.append(type(items))
print(lst2)