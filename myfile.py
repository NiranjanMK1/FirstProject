a = [1,3,4,5,3,7,7,6,4]
c = []
while a:
    b = a[0]
    for i in a:
        if i < b:
            b = i
    c.append(b)
    a.remove(b)
print(c)
