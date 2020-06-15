# Program to sort alphabetically the words form a string provided by the user

my_str = "Hello this Is an Example With cased letters"

words = my_str.split()

# sort the list
words.sort()

print("The sorted words are:")
for word in words:
   print(word)

#output: 
#The sorted words are:
#Example
#Hello
#Is
#With
#an
#cased
#letters
#this 