from mcpi.minecraft import Minecraft
from map import Fase
from Message import Message
import time
mc = Minecraft.create()
pos = {'x': 100, 'y': 100, 'z': 100}
platforms = 40
lstPlatforms = []

fase = Fase(20, 20, 20, mc)
message = Message(mc)
# fase.Clean(pos)
fase.LoadFloor(pos, 20, 20, 1)
fase.LoadUnderFloor(pos, 20, 20)
# fase.LoadCeilling(pos, 20, 10, 89)
fase.LoadWalls(pos, 20, 20, 120)
mc.player.setTilePos(pos['x']+4, pos['y']+5, pos['z']+10)
lstPlatforms = fase.LoadPlatforms(platforms)
fase.LoadTrap(pos, 20, 20)
message.WarningBeginning(30)
while(platforms > 0):
    message.WarningRemoveBlock()
    fase.CleanFloor(pos, lstPlatforms)
    lstPlatforms = fase.RemoveRandomPlatform(pos, lstPlatforms)
    platforms = platforms - 1
