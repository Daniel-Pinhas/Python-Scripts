#!/usr/bin/python3
""""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lst=[]
for x in a:
    if int(x%2) == 0:
        lst.append(x)
print(lst)   
"""""


a = [5, 10, 15, 20, 25]
def firstlast(a):
    lst = []
    y = (len(a)-1)
    lst.append(a[0])
    lst.append(a[y])
    return(lst)

t = [5, 10, 15, 20, 25]

print(firstlast(t))