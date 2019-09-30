li=[1,42,21,311,1,2,2133]
asc=[]
while li:
    minimum = li[0]
    for x in li:
        if x < minimum:
            minimum = x
    asc.append(minimum)
    li.remove(minimum)
print asc