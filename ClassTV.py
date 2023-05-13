# Create Class named "TV"
class TV:
    def __init__(self, tv, channel, volume):
        # instance variables
        self.tv = tv
        self.channel = channel
        self.volume = volume
    
    # Create Behaviors/Statements
    def getChannel(self):
        print(self.tv, "channel is", self.channel, end='')
    def getVolume(self):
        print(' and volume level is', self.volume)