from ClassTV import TV

# Create Objects for created class
TV1 = TV("tv1's", '30', '3')
TV2 = TV("tv2's", '3', '2')


from art import *

# Call methods for output
Filename = tsave(TV1.getChannel(), TV1.getVolume(), '\n', TV2.getChannel(), TV2.getVolume(), "ClassTV.py")
print(Filename)