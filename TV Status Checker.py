# Create Class named "TV"
class TV:
    def __init__(self, channel, volume, channelTwo, volumeTwo):
        # instance variables
        self.channel = channel
        self.volume = volume
        self.channelTwo = channelTwo
        self.volumeTwo = volumeTwo
    
    # Create Behaviors/Staements
    def getChannel(self):
        print("TV1's channel is ", self.channel)
    def getVolume(self):
        print(' and volume level is ', self.volumeTwo)

    def getChannel2(self):
        print("TV2's channel is ", self.channelTwo)
    def getVolume2(self):
        print(' and volume level is ', self.volumeTwo)
# Create Objects for created class
# Call methods for output