#!/usr/bin/python3

def no_c(my_string):
	string = ""
	for c in my_string:
		if (ord(c) != ord("c") and ord(c) != ord("C")):
			string += c
	return (string)
