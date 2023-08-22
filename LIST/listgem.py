row1 = ["??","??","??"]
row2 = ["??","??","??"]
row3 = ["??","??","??"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
pos = input("Where do you want to put the treasure? ")
vert = int(pos[0])-1
hori = int(pos[1])-1
map[vert][hori] = 'X'
print(f"{row1}\n{row2}\n{row3}")