# Too many values to unpack

# a, b, c = [1, 2, 3, 4, 5]
# print(a,b,c)

# Youcan assign the value left to some var using *

a, b, *c = [1, 2, 3, 4, 5]
print(a, b, c)

# use *_ to ignore what left behid

d, e, *_ = (6, 7, 8, 9, 10)
print(d, e)
