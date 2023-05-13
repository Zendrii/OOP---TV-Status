from ClassTV import TV

# Create Objects for created class
TV1 = TV("tv1's", '30', '3')
TV2 = TV("tv2's", '3', '2')

print('\033[92m='*158)

# Call methods for output
print('\n'), TV1.getChannel(), TV1.getVolume()
TV2.getChannel(), TV2.getVolume(), print('\n')

print('\033[92m='*158)