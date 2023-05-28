str = "hello world"
print(str) #prints the original String

str = str.capitalize() #Converts the first character to upper case
print(str) #Hello world

str = str.casefold() #Converts string into lower case
print(str)

print(str.count('o')) #count() returns the number of times a specified value occurs in a string

print(str.endswith('e')) #endswith() returns true if the string ends with the specified value
