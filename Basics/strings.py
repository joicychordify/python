#String opertaions and Slicing
x = "//This 'is' a strinG"
y= 10000
print(x)
print(x[10]) #it takes the 10th position value
print("a" in x) #it checks the presence of the alphabet
print(len(x)) #it returns the length of the string
print(str(y)) #it converts integer into s string
a = (x.upper()) #it converts all characters into uppercase letters
print(a)
print(x.count("is",0,8)) #it returns the count of the string specified in the paranthesis
print(a.islower())
print(a.isupper())
print(x.split())#whitespaces considered as the separator
print(x.strip('/')) #it trims the strings and removes the char specified in the paranthesis
print(x.rstrip('/')) #it trims from the right side of the string
print(x.lstrip('/')) #it trims from the left side of the string
print(x.replace('is', 'was'))#it replaces the old string with new value
print(x.find('a'))# it find the spec char from the string and returns position.
print(x.index('a'))# find and index are same but index returns value error if str not found.
print(x[0:5])
print(x[0:4:2])
print(x[:])
print(x[5:])
print(x[:10])
print(x[-1])
print(x[-6:-1])
print(x[0: x.index('a')])
print(x)

#How to format Strings
