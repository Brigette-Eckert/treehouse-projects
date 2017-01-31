# Can make sets with or without set function.  Set function needed for older verisons
my_set = set([1.3,5])
print(my_set)

my_set2 = {1, 3, 5}
print(my_set2)

# empty curly braces creates a dict not a set.

# Sets don't have defined order or indexes

#use add to add one thing
low_primes = {1, 3, 5, 7, 11, 13}
low_primes.add(17)
print(low_primes)

#sets are mutable
#use update to add multiple sets

low_primes.update({19, 23}, {2, 29})
print(low_primes)

#use remove method to remove value from set
low_primes.remove(29)
print(low_primes)

#remove will throw error if value trying to remove doesn't exist
# low_primes.remove(100)
# print(low_primes)

#discard will not throw error if value doesn't exist - will just move on
low_primes.discard(100)
print(low_primes)

#can use pop on sets