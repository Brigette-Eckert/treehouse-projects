print("cheese" in "cheeseshop")
cheeseshoop = []
print("cheese" in cheeseshoop)

days_open = ["Monday", "Tuesday", "Wednesday", "Thursday"]
today = "Tuesday"

if today in days_open:
	print("Come on in")
else:
	print("Sorry, we're closed!")

today= "Sunday"
if today not in days_open:
	print("Sorry, we're closed")