my_list = []

def remove_item(idx): 
	index = idx -1
	item = my_list.pop(index)
	print("Removed {}".format(item))

def show_help():
	print("\nSeperate each item with a comma.")
	print("Type DONE to quit, SHOW to see the current list, REMOVE to remove and item and HELP to display this message")

def show_list():
	count = 1
	for item in my_list:
		print("{}: {}".format(count, item))
		count += 1

print("Give me a list of items to put on your list")
show_help()

while True:
	new_stuff = input("> ")

	if new_stuff.upper() == "DONE":
		print("\nHere's your list")
		show_list()
		break
	elif new_stuff.upper() == "HELP":
		show_help()
		continue
	elif new_stuff.upper() == "SHOW":
		show_list()
		continue
	elif new_stuff.upper() == "REMOVE":
		show_list()
		idx = input("Remove which item? Tell me the number ")
		remove_item(int(idx))
		continue
	else: 
		new_list = new_stuff.split(",")
		index = input("Add this at a certain spot? Press enter for the end of the list,"
			" or give me number. Currently {} items on the list ".format(len(my_list)))
		if index:
			print("item(s) added to spot {}".format(index))
			spot = int(index)-1 
			for item in new_list:
				my_list.insert(spot, item.strip())
				spot += 1
		else:
			print("item added to end of the list")
			for item in new_list:
				my_list.append(item.strip())

