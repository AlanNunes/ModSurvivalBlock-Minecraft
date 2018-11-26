import random
from BlockType import BlockType
class Fase:
    def __init__(self, width, height, length, mc):
        self.width = width
        self.length = length
        self.height = height
        self.mc = mc
    def Clean(self, pos):
        self.mc.setBlocks(pos['x'], pos['y'] - 10, pos['z'], pos['x'] + self.width, pos['y'] + self.height, pos['z'] + self.length, 0)
        self.mc.setBlocks(pos['x'], pos['y'] - 9, pos['z'], pos['x'] + self.width, pos['y'] + self.height, pos['z'] + self.length, 0)
        self.mc.setBlocks(pos['x'], pos['y'] - 8, pos['z'], pos['x'] + self.width, pos['y'] + self.height, pos['z'] + self.length, 0)
        self.mc.setBlocks(pos['x'], pos['y'] - 7, pos['z'], pos['x'] + self.width, pos['y'] + self.height, pos['z'] + self.length, 0)
        self.mc.setBlocks(pos['x'], pos['y'] - 6, pos['z'], pos['x'] + self.width, pos['y'] + self.height, pos['z'] + self.length, 0)
        self.mc.setBlocks(pos['x'], pos['y'] - 5, pos['z'], pos['x'] + self.width, pos['y'] + self.height, pos['z'] + self.length, 0)
        self.mc.setBlocks(pos['x'], pos['y'] - 4, pos['z'], pos['x'] + self.width, pos['y'] + self.height, pos['z'] + self.length, 0)
        self.mc.setBlocks(pos['x'], pos['y'] - 3, pos['z'], pos['x'] + self.width, pos['y'] + self.height, pos['z'] + self.length, 0)
        self.mc.setBlocks(pos['x'], pos['y'] - 2, pos['z'], pos['x'] + self.width, pos['y'] + self.height, pos['z'] + self.length, 0)
        self.mc.setBlocks(pos['x'], pos['y'] - 1, pos['z'], pos['x'] + self.width, pos['y'] + self.height, pos['z'] + self.length, 0)

    def CleanFloor(self, pos, platforms):
        for i in range(self.length):
            x = pos['x'] + 1 + i
            z = pos['z'] + 1
            for j in range(self.width):
                for k in range(len(platforms)):
                    if x != platforms[k][0] and z+j != platforms[k][1]:
                        self.mc.setBlock(x, 100, z + j, 0)
                    else:
                        self.mc.setBlock(platforms[k][0], 100, platforms[k][1], platforms[k][2])
    def LoadFloor(self, pos, width, length, blockType):
        self.mc.setBlocks(pos['x'], pos['y'], pos['z'], pos['x'] + width, pos['y'], pos['z'] + length, blockType)
    def LoadUnderFloor(self, pos, width, length, blockType = 20):
        self.mc.setBlocks(pos['x'], pos['y'] - 4, pos['z'], pos['x'] + width, pos['y'], pos['z'] + length, blockType)
    def LoadTrap(self, pos, width, length, blockType = 10):
        self.mc.setBlocks(pos['x'], pos['y'] - 1, pos['z'], pos['x'] + width, pos['y'] - 2, pos['z'] + length, blockType)
    def LoadCeilling(self, pos, height, length, blockType):
        self.mc.setBlocks(pos['x'], pos['y'] + height, pos['z'], pos['x'] + length, pos['y'], pos['z'] + length, blockType)
    def LoadWalls(self, pos, width, height, blockType):
        for i in range(height):
            y = pos['y'] + i
            for j in range(width):
                self.mc.setBlock(pos['x'] + j, y - 10, pos['z'], 45)
        for i in range(height):
            y = pos['y'] + i
            for j in range(width):
                self.mc.setBlock(pos['x'] + j, y - 10, pos['z'] + self.width, 45)
        for i in range(height):
            y = pos['y'] + i
            for j in range(width):
                self.mc.setBlock(pos['x'] + self.width, y - 10, pos['z'] + j, 45)
        for i in range(height):
            y = pos['y'] + i
            for j in range(width):
                self.mc.setBlock(pos['x'], y - 10, pos['z'] + j, 45)
    def LoadObstacles(self):
        x = random.randint(101, 119)
        y = random.randint(101, 119)
        z = random.randint(101, 119)
        self.mc.setBlock(x, y, z, 30)
    def LoadPlatforms(self, platforms):
        lstPlatforms = []
        for i in range(platforms):
            x = random.randint(101, 119)
            y = 100
            z = random.randint(101, 119)

            blockType = BlockType()
            i = random.randint(0, len(blockType.GetBlockTypes())-1)
            blockTypes = blockType.GetBlockTypes()
            blockType = blockTypes[i]
            lstPlatforms.append([x, z, blockType])
            self.mc.setBlock(x, y, z, blockType)
        return lstPlatforms
    def RemoveRandomPlatform(self, pos, lstPlatforms):
        size = len(lstPlatforms)
        i = random.randint(0, size-1)
        platform = lstPlatforms[i]
        self.mc.setBlock(platform[0], 100, platform[1], 0)
        lstPlatforms.pop(i)
        return lstPlatforms
