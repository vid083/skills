# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))

# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# To join two or more tuples you can use the + operator:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# The tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#Tuple Methods

count() ----> Returns the number of times a specified value occurs in a tuple

index() ----> Searches the tuple for a specified value and returns the position of where it was found
