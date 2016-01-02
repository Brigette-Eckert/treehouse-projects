#make a list that holds onto items
# print out instructions on how to use the app
#ask for new items and add to list

my_list = []
print("Enter 'SHOW' to show your current list, Enter 'DONE' to stop adding items and enter 'HELP' to dispaly these intsructions")

def add_item():
	while True: 
		item = input("What would you like to add to your list? ")
		if item == "DONE":
			#be able to quit the app
			#print out the list 
			print("Your List: {}".format(my_list))
			print("goodbye!")
			break
#be able to type HELP to show intsructions for DONE, SHOW and HELP
		elif  item == "HELP":
			print("Enter 'SHOW' to show your current list, Enter 'DONE' to stop adding items and enter 'HELP' to dispaly these intsructions")
			continue

#be able to type SHOW to show the list
		elif item == "SHOW":
			print("Your List: {}".format(my_list))
			continue
		else:
			item = item.lower()
			my_list.append(item)
			print("{} added to your list".format(item))
			continue
	

add_item()



