
set1 = set(range(10))

set2 = {1, 2, 3, 5,  7, 11, 19, 23}

#union is the combonation of two or more sets.  Numbers in both sets are on;y added once not twice so resulting set will still have uqnuie values
#union returns a new set, rather than update which modifies exisitinf

print(set1.union(set2))
print(set1 | set2)


# difference finds everything in the first set, but not the second.
print(set1.difference(set2))

print(set2.difference(set1))

print(set1 - set2)

print(set2 - set1)
#sysmetric difference finds what is unquie to either set

print(set1.symmetric_difference(set2))
print(set1 ^ set2)
#intersection gives new set of items made of values found in both sets

print(set1.intersection(set2))
print(set1 & set2)