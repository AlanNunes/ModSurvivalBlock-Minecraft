import time
class Message:
    def __init__(self, mc):
        self.mc = mc
    def WarningBeginning(self, seconds = 10):
        for i in range(seconds, 0, -1):
            msg = "Beginning game in " + str(i) + " seconds"
            self.mc.postToChat(msg)
            time.sleep(1)
    def WarningRemoveBlock(self, seconds = 5):
        for i in range(seconds, 0, -1):
            msg = "Removing block in " + str(i) + " seconds"
            self.mc.postToChat(msg)
            time.sleep(1)
