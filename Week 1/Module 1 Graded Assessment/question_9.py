# Question 9
#    Use Python to calculate how many different passwords can be formed with 6 lower case English letters. For a 1 letter
#    password, there would be 26 possibilities. For a 2 letter password, each letter is independent of the other, so there would
#    be 26 times 26 possibilities. Using this information, print the amount of possible passwords that can be formed with 6
#    letters.

password_len = 6
possibilities = 26
print(possibilities ** password_len)
