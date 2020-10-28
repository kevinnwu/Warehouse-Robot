y = 0

map = open("Maps.txt", "r")
Height_Map = len(map.readlines())
path = [[] for i in range(Height_Map)]
map.close()

map = open("Maps.txt", "r")
for row in map.readlines():
    for column in row:
        if column == '\n':
            continue
        path[y].append(int(column))
    y += 1
Length_Map = len(path[0])
print("H x L = " + str(Height_Map) + " x " + str(Length_Map))
path.reverse()
map.close()

# cols = Length_Map,  rows = Height_Map
closed = []
opens = []
cost = []
fx = [[0 for x in range(Length_Map)] for y in range(Height_Map)]
gx = [[0 for x in range(Length_Map)] for y in range(Height_Map)]
hx = [[0 for x in range(Length_Map)] for y in range(Height_Map)]
parent = [[0 for x in range(Length_Map)] for y in range(Height_Map)]


for row in range(Height_Map):
    pass
    #print(path[Height_Map-row-1])

for row in range(Height_Map):
    for column in range(Length_Map):
        if path[row][column] == 1:
            fx[row][column] = Length_Map+Height_Map*3

"""Xs = int(input("X Coordinate of Start : "))
Ys = int(input("Y Coordinate of Start : "))
while Xs >= Length_Map or Ys >= Height_Map or path[int(Ys)][int(Xs)] == 1:
    print("Invalid coordinate, Try again")
    Xs = int(input("X Coordinate of Start : "))
    Ys = int(input("Y Coordinate of Start : "))
Xf = int(input("X Coordinate of Finish : "))
Yf = int(input("Y Coordinate of Finish : "))
while Xf >= Length_Map or Yf >= Height_Map or path[int(Yf)][int(Xf)] == 1:
    print("Invalid coordinate, Try again")
    Xf = int(input("X Coordinate of Finish : "))
    Yf = int(input("Y Coordinate of Finish : "))
"""
Xs = 0
Ys = 2
Xf = 8
Yf = 2
maximum_try = 100
#int(input("Maximum try : "))


def left(xl, yl):
    if xl - 1 == -1:
        print("1")
        return False
    elif path[yl][xl - 1] == 1:
        print(xl)
        print("2")
        return False
    elif closed.count((xl - 1) * 10 + yl) >= 1:
        print("3")
        return False
    elif opens.count((xl - 1) * 10 + yl) >= 1:
        print("4")
        return False
    else:
        return True


def right(xl, yl):
    if xl + 1 == Length_Map:
        return False
    elif path[yl][xl + 1] == 1:
        return False
    elif closed.count((xl + 1) * 10 + yl) >= 1:
        return False
    elif opens.count((xl - 1) * 10 + yl) >= 1:
        return False
    else:
        return True


def top(xl, yl):
    if yl + 1 == Height_Map:
        return False
    elif path[yl + 1][xl] == 1:
        return False
    elif closed.count(xl * 10 + (yl + 1)) >= 1:
        return False
    elif opens.count(xl * 10 + (yl + 1)) >= 1:
        return False
    else:
        return True


def bottom(xl, yl):
    if yl - 1 == -1:
        return False
    elif path[yl - 1][xl] == 1:
        return False
    elif closed.count(xl * 10 + (yl - 1)) >= 1:
        return False
    elif opens.count(xl * 10 + (yl - 1)) >= 1:
        return False
    else:
        return True


def count(xd, yd):
    gx[yd][xd] = gx[parent[yd][xd] % 10][int(parent[yd][xd] / 10)] + 1
    hx[yd][xd] = abs(xd - Xs) + abs(yd - Ys)
    fx[yd][xd] = gx[yd][xd] + hx[yd][xd]
    opens.append(xd * 10 + yd)
    cost.append(fx[yd][xd])


def bsort(n):
    for i in range(n):
        key = cost[i]
        key2 = opens[i]
        j = i - 1
        while j >= 0 and cost[j] < key:
            cost[j + 1] = cost[j]
            opens[j + 1] = opens[j]
            j -= 1
        cost[j + 1] = key
        opens[j + 1] = key2


def plan():
    Xl = Xf
    Yl = Yf
    c = 0
    closed.append((Xl * 10) + Yl)
    while Xl != Xs or Yl != Ys:
        c += 1
        l = left(Xl, Yl)
        r = right(Xl, Yl)
        t = top(Xl, Yl)
        b = bottom(Xl, Yl)
        if l:
            parent[Yl][Xl - 1] = (Xl * 10 + Yl)
            count(Xl - 1, Yl)
        if r:
            parent[Yl][Xl + 1] = (Xl * 10 + Yl)
            count(Xl + 1, Yl)
        if t:
            parent[Yl + 1][Xl] = (Xl * 10 + Yl)
            count(Xl, Yl + 1)
        if b:
            parent[Yl - 1][Xl] = (Xl * 10 + Yl)
            count(Xl, Yl - 1)
        bsort(len(opens))
        closed.append(opens[len(opens) - 1])
        opens.pop()
        cost.pop()
        Xl = int(closed[len(closed) - 1] / 10)
        Yl = int(closed[len(closed) - 1] % 10)
        if c > maximum_try:
            break
            print("Maximum Try Limited")
    print("Try : " + str(c))
    for l in closed:
        path[l % 10][int(l / 10)] = 99
    for row in range(Height_Map):
        print(path[Height_Map - row - 1])

plan()
for g in gx:
    print(g)