# Create Class named "TV"
class TV:
    def __init__(self, channel, volume, channelTwo, volumeTwo):
        # instance variables
        self.channel = channel
        self.volume = volume
        self.channelTwo = channelTwo
        self.volumeTwo = volumeTwo
    
    # Create Behaviors/Statements
    def getChannel(self):
        print("TV1's channel is ", self.channel)
    def getVolume(self):
        print(' and volume level is ', self.volume)

    def getChannel2(self):
        print("TV2's channel is ", self.channelTwo)
    def getVolume2(self):
        print(' and volume level is ', self.volumeTwo)
        

# Create Objects for created class
TV1 = TV('30', '3', '0', '0')
# Call methods for output
TV1.getChannel, TV1.getVolume
# Create Objects for created class
TV2 = TV('0', '0', '3', '2')
# Call methods for output
TV2.getChannel2, TV2.getVolume2