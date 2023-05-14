from ClassTV import TV

# Create Objects for created class
TV1 = TV('30', '3', '')
TV2 = TV('3', '2', '')

print('\033[92m='*158)

# Call methods for output
print('\n'),TV1.TV(), TV2.TV(), TV1.getChannel(), TV1.getVolume()
TV2.getChannel(), TV2.getVolume(), print('\n')

print('\033[92m='*158)