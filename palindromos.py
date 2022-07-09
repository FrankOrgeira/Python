def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for i in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if i != " ":
			#print (i)
			new_string += i.lower()
			print(new_string)
			#reverse_string += i[len(input_string)-1]
			prueba = "Hola que tal".strip()
			print(prueba)
			#print(input_string.rstrip())
			print(len(input_string)-len(new_string)+1)
			#print(reverse_string)
	# Compare the strings
	#if ___:
	#	return True
	return False

texto = "Hola que tal"
texto = texto.strip()
print (texto)
print(is_palindrome("Never Odd or Even")) # Should be True
#print(is_palindrome("abc")) # Should be False
#print(is_palindrome("kayak")) # Should be True