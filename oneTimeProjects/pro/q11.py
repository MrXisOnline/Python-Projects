def is_palindrome(string):
	rev_string = string[::-1]
	if string == rev_string:
		print("It is Palindrome")
	else:
		print("Not a Palindrome")

is_palindrome("nitin")