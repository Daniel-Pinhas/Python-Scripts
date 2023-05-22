#!/usr/bin/python3
"""""
#Exercise 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

result = []
res = []
for x in range(len(a)-5):
        res.append(a[x])
print(res) 


z=int(input("enter a number "))
re = []
for x in range(len(a)-z):
        re.append(a[x])
print(re) 

#Exercise 2

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c= set(a)
d= set(b)
print(c.intersection(d))
"""""


#Exercise 3
def duplicatedel(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

lst1 = [1, 1, 2, 6, 6, 6, 6, 6, 6, 7, 7, 8, 13, 21, 34, 34, 55,89, 89]
lst2 = ["a","a","a","a","df","f","a","a"]
print(duplicatedel(lst1))
print(duplicatedel(lst2))










