my_str = "Hi, my name is {name} and I live in {state}"
print(my_str.format(name = "Brigette", state="Oregon"))
print(my_str.format(state = "Oregon", name="Brigette"))
my_dict ={"name": "Brigette", "state": "Oregon"}
print(my_str.format(**my_dict))