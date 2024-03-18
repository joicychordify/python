cities = ["Delhi", "Mumbai", "kolkata", "Hyderabad"]
print(cities)
cities.append("Lucknow")
print(cities)
cities.insert(1, "Raipur") #add value at the index of 1
print(cities)
cities.remove("Mumbai") # remove the item from the list
print(cities)
cities.pop(3) #removes from the index 3
print(cities)
print(cities.index("Raipur"))# it takes the index of the value
print(cities.count("Mumbai"))
print(cities.count("Delhi")) # count the given string
cities.sort() # it sorts the values
print(cities)
cities.reverse() # it reverses the values
print(cities)
new_cities = cities.copy() # it copies the existing list values
print(new_cities)




