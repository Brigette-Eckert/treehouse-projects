# import pdb

#use n for next, line by line, and c for continue, run like normal, with pdb

my_list = [5, 2, 1, True, "abcdefg", 3, False, 4]

import pdb; pdb.set_trace() #more common way to use pdb rather than importing at top of file
del my_list[3] #[5, 2, 1,  "abcdefg", 3, False, 4]
del my_list[3] #[5, 2, 1, 3, False, 4]
del my_list[4] #[5, 2, 1, 3,  4]

print(my_list)
