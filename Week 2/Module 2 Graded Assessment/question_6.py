#    Question 6
#    Complete the body of the format_name function. This function receives the first_name and last_name parameters and
#    then returns a properly formatted string.print(11%5)

def format_name(first_name, last_name):
	# code goes here
	string = print(first_name + ", " + last_name)
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
