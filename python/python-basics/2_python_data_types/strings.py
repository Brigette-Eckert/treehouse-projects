long_string = """Here's a new line!
	
	It's right there!"""
name = "Brigette"
status_message = "Hey, we have {} people using the site right now"
print("apple")
print('apple')
print("She's right")
print('She\'s right')
print("""She\'s right""")
print('''She\'s right''')
print(str(5))
print("Hello " + 'World!')
print(long_string)
name += "Eckert" 
print(name)
print("I love cats " * 20)
print(status_message.format(7))
print("Hey we have {} {} using the site right now".format(5, "dogs"))
# .format will automatically convert input to string for us 