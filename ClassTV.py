# Create Class named "TV"
class TV:
    def __init__(self, channel, volumeLevel, power):
        # instance variables
        self.channel = channel
        self.volume = volumeLevel
        self.power = power
    
    # Create Behaviors/Statements
    def TV(self):
        tv_num = input('TV number: ')
        self.tv = tv_num

    def turnOn(self):
        self.power = True

    def turnOff(self):
        self.power = False
        
    def getChannel(self):
        print(self.tv, "'s channel is", self.channel, end='')

    def setChannel(self):
        self.channel = input('Set the channel you want: ')
        print('You have set the channel to', self.channel)

    def getVolume(self):
        print(' and volume level is', self.volume)

    def setVolume(self):
        self.volume = input('Set the volume level you want: ')
        print('You have set the volume level to', self.volume)

    def channelUp(self):
        channel_change = self.channel + 1
        print('Channel:', channel_change)

    def channelDown(self):
        channel_change2 = self.channel - 1
        print('Channel:', channel_change2)

    def volumeUp(self):
        volume_change = self.volume + 1
        print('Volume:', volume_change)
    
    def volumeDown(self):
        volume_change2 = self.volume - 1
        print('volume:', volume_change2)