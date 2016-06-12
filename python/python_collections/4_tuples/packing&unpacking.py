a, b = 1, 2
print(a)
print(b)
#can assign mutliple variables at once in py

c = 3,4 
print(c)

d,e = c

print(d)
print(e)

f= d,e

print(f)
print (f==c)
print(a,b)
a, b = b, c
print(a)


def my_func():
	print(1, 2, 3)
	return 1, 2, 3

my_func()

tup = my_func()

print(tup)

x, y, z = my_func()
print(x)
print(y)
print(z)