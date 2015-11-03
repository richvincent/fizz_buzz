import sys

number_of_args = len(sys.argv)

def get_int():
	""" Function used to test user input as a valid integer. 
	If input is not a valid integer ask the user to try again"""
	integer = ""
	switch = False
	while switch == False:
		integer  = input("Please enter a positive integer!")
		try:
			integer = int(integer)
			switch = isinstance(integer,int)
		except ValueError:
			print("Please eneter a positive integer!!!!")
	else:
		return(integer)



if number_of_args > 2:
        print("The correct format is fizzbuzz.py <count as positive integer>")
        sys.exit()
elif number_of_args == 2:
	game_count = sys.argv[1]
	try:
		game_count = int(game_count)
	except ValueError:
		print("Please enter a positive integer!!!!")

else:
        game_count = get_int()


if game_count == 0:
        print("Please enter a positive integer!!!!")
        sys.exit()

for x in range(1, game_count+1):
	if x%3 == 0 and x%5 == 0:
		print ("fizzbuzz")
	elif x%3 == 0:
		print("fizz")
	elif x%5 == 0:
		print("buzz")
	else:
		print(x)

