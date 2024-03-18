x = "Hello World"
y = "This is a sample Text"
print("Welcome to "+x+" And "+y)
print("Welcome to %s And %s" % (x, y))
print("Welcome to %s And %s" % ("Tutorial", y))
print("Welcome to {} And {}".format(x,y)) #arguments
print("Welcome to {0} And {1}".format(x,y))#index
print("Welcome to {a} And {b}".format(a=x,b=y)) #keywords