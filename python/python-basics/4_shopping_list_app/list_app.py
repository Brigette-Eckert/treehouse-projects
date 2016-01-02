#make a list that holds onto items
# print out instructions on how to use the app
#ask for new items and add to list

my_list = []
print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items")
def add_item():
	while True: 
		item = input("What would you like to add to your list? ")
		if item == "DONE":
			#be able to quit the app
			#print out the list 
			print("Your List: {}".format(my_list))
			print("goodbye!")
			break
		else:
			item = item.lower()
			my_list.append(item)
			(print(my_list))
			print("{} added to your list".format(item))
			continue
	

add_item()

