import random

#rooms will be coordinates 
#put door, player and monster into random rooms
#let player move around but not go off map
#let player know if they find the door or the monster
#leave a breadcrumb trail so player doesn't backtrack

my_list = list(range(50))

print(my_list)

print(random.choice(my_list))

print(random.choice([(0, 1), (2,3), (4,5)]))