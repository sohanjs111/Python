#    Question 6
#    The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the
#    sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'),
#    ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works
#    as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that.

def guest_list(guests):
	for i in guests:
		g_name = i[0]
		g_age = i[1]
		g_job = i[2]
		print("{} is {} years old and works as {}".format(g_name, g_age, g_job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
