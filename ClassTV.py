# Create Class named "TV"
class TV:
    def __init__(self, tv, channel, volume, power):
        # instance variables
        self.tv = tv
        self.channel = channel
        self.volume = volume
        self.power = power
    
    # Create Behaviors/Statements
    def turnOn(self):
        self.power = True
    def turnOff(self):
        self.power = False
    def getChannel(self):
        print(self.tv, "channel is", self.channel, end='')
    def getVolume(self):
        print(' and volume level is', self.volume)