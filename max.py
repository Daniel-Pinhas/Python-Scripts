
#!/usr/bin/python3

def max3(x, y ,z):
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    else:
        return z
    
print(max3(-5, 1 ,-19))
