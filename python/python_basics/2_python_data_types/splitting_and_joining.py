#spilt method
print(list("hello"))
print("hello".split())
print("hello there students".split())
print("red:blue:green".split(":"))

#join method 
flavors = ["chocolate", "mint", "strawberry"]
print(', '.join(flavors))
print(flavors)
print("My favorite flavors are " + ', '.join(flavors))
print("My favorite flavors are {}".format(", ".join(flavors)))
# can only join string items