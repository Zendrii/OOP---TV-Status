# Create Class named "TV"
class TV:
    def __init__(self, tv, channel, volume):
        # instance variables
        self.tv = tv
        self.channel = channel
        self.volume = volume
    
    # Create Behaviors/Statements
    def getChannel(self):
        print(self.tv, "'s channel is ", self.channel, end='')
    def getVolume(self):
        print(' and volume level is ', self.volume)

# Create Objects for created class
TV1 = TV('tv1', '30', '3')
TV2 = TV('tv2', '3', '2')

# Call methods for output
TV1.getChannel(), TV1.getVolume()
TV2.getChannel(), TV2.getVolume()