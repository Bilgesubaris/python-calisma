class TV:
  def __init__(self):
    self.channel=1
    self.volumeLevel=1
    self.on=False
  def turnOn(self):
    self.on=True

  def turnOff(self):
    self.on=False

  def getChannel(self):
    return self.channel

  def setChannel(self,channel):
    if self.on and 1 <= self.channel <= 120:
     self.channel = channel

  def getVolumeLevel(self):
    return self.volumeLevel
    
  def setVolumeLevel(self,volumeLevel):
    if self.on and 1 <= self.volumeLevel <= 7:
      self.volumeLevel = volumeLevel
