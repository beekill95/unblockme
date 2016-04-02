import pygame, sys, time, copy, os
from pygame.locals import *
from os.path import dirname, realpath, abspath


class Map:
    def __init__(self):
        self.mapnum = 1
        self.mapname = 'map1.txt'
        self.mapp = []
        self.player = None
        self.move = 1

        pygame.init()

        # set up the window
        self.display = pygame.display.set_mode((570, 510))
        pygame.display.set_caption('Unblock me solver')
        (self.bx,self.by) = (220,100)

        # set color
        self.WHITE = (255, 255, 255)
        self.LIGHTBROWN = (183,91,0)
        self.BROWN = (102,51,0)

        # load images
        resourceDir = "resources"
        self.br = pygame.image.load(os.path.join(resourceDir, "map.jpg"))
        self.br2 = pygame.image.load(os.path.join(resourceDir, "map2.jpg"))
        self.br3 = pygame.image.load(os.path.join(resourceDir, "map2.jpg"))
        self.header = pygame.image.load(os.path.join(resourceDir, "header.jpg"))
        self.header2 = pygame.image.load(os.path.join(resourceDir, "header2.jpg"))
        self.lar = pygame.image.load(os.path.join(resourceDir,"lar.jpg"))
        self.rar = pygame.image.load(os.path.join(resourceDir,"rar.jpg"))
        self.state = pygame.image.load(os.path.join(resourceDir,"state.jpg"))
        self.bbut = pygame.image.load(os.path.join(resourceDir,"but.jpg"))
        self.dbut = pygame.image.load(os.path.join(resourceDir,"but.jpg"))
        self.hbut = pygame.image.load(os.path.join(resourceDir,"but.jpg"))
        self.rbut = pygame.image.load(os.path.join(resourceDir,"rbut.jpg"))
        self.block2n = pygame.image.load(os.path.join(resourceDir,"block_2_hor_110x55.jpg"))
        self.block3n = pygame.image.load(os.path.join(resourceDir,"block_3_hor_165x55.jpg"))
        self.block2d = pygame.image.load(os.path.join(resourceDir,"block_2_ver_55x110.jpg"))
        self.block3d = pygame.image.load(os.path.join(resourceDir,"block_3_ver_55x165.jpg"))
        self.blockmain = pygame.image.load(os.path.join(resourceDir,"main_block_110x55.jpg"))

        # set background image
        self.display.fill(self.LIGHTBROWN)
        self.display.blit(self.header, (200, 0))
        self.display.blit(self.br, (200, 80))
        self.display.blit(self.lar, (230, 28))
        self.display.blit(self.rar, (500, 28))
        self.display.blit(self.bbut, (220, 450))
        self.display.blit(self.dbut, (300, 450))
        self.display.blit(self.hbut, (380, 450))
        self.display.blit(self.rbut, (460, 450))

        return

    def loadWord(self, word,size,x,y):
        fontObj = pygame.font.Font('freesansbold.ttf', size)

        textSurfaceObj = fontObj.render(word , True, self.WHITE , self.BROWN)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (x, y)
        self.display.blit(textSurfaceObj, textRectObj)

    def loadTitle(self):
        self.display.blit(self.header2, (0, 0))
        self.display.blit(self.br2, (0, 80))
        self.display.blit(self.br3, (0, 80+175))
        self.display.blit(self.state, (20, 450))

        self.loadWord('Time to solve',18,108,112)
        self.loadWord('Number of moves',18,108,287)
        self.loadWord('BFS',22,250,470)
        self.loadWord('DFS',22,330,470)
        self.loadWord('A*',22,410,470)
        self.loadWord('RESET',22,505,470)

    def readMapFile(self):
        # DISPLAY MAP NAME
        self.display.blit(self.header, (200, 0))
        self.display.blit(self.lar, (230, 28))
        self.display.blit(self.rar, (500, 28))
        self.loadWord('PUZZLE ' + str(self.mapnum),32,388,50)
        # LOAD MAP FROM FILE
        mapDir = "maps"
        self.mapname = 'map' + str(self.mapnum) + '.txt'
        self.mapp = map(str.split, open(os.path.join(mapDir, self.mapname)))

    def loadTime(self,start):
        self.display.blit(self.br2, (0, 80))
        self.loadWord('Time to solve',18,108,112)
        end = round(float(time.time()),2)
        elapsed = round(end -start,2)
        self.loadWord(str(elapsed) + "s",42,108,182)

    def loadMove(self):
        self.display.blit(self.br3, (0, 80+175))
        self.loadWord('Number of moves',18,108,287)
        self.loadWord(str(self.move),42,108,357)

    def loadInfo(self, statee):
        self.display.blit(self.state, (20, 450))

        if statee == 'solving': self.loadWord('Solving',18,110,470)
        elif statee == 'found': self.loadWord('Solution found',18,110,470)
        else: self.loadWord('No solution',18,110,470)

        pygame.display.update()

    def getMapState(self):
        return self.mapp

    def moveBlock(self, mapState):
        self.updateMapState(mapState)
        self.move += 1
        pygame.time.wait(50)

    def setPlayer(self, player):
        self.player = player

    def updateMapState(self, mapp3):
        self.display.blit(self.br, (200, 80))

        # DISPLAY IMAGE OF BLOCKS
        for i in range(0, 6):
            for j in range(0, 6):
                if mapp3[i][j] == '1' :
                    if mapp3[i][j+1] == '2':
                        self.display.blit(self.block2n, (self.bx + j*55, self.by + i*55))
                    elif mapp3[i][j+1] == '3':
                        self.display.blit(self.block3n, (self.bx + j*55, self.by + i*55))
                elif mapp3[i][j] == '4' :
                    if mapp3[i+1][j] == '5':
                        self.display.blit(self.block2d, (self.bx + j*55, self.by + i*55))
                    elif mapp3[i+1][j] == '6':
                        self.display.blit(self.block3d, (self.bx + j*55, self.by + i*55))
                elif mapp3[i][j] == '8' : self.display.blit(self.blockmain, (self.bx + j*55, self.by + i*55))

        pygame.display.update()

    def mapLoop(self):
        self.loadTitle()
        self.readMapFile()
        self.updateMapState(self.mapp)

        while True: # the main game loop
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mx,my = pygame.mouse.get_pos()
                    if mx in range(230,270) and my in range(28,68):
                        self.loadTitle()
                        if self.mapnum > 1:
                            self.mapnum -= 1
                            self.readMapFile()
                            self.updateMapState(self.mapp)
                        elif self.mapnum == 1:
                            self.mapnum = 10
                            self.readMapFile()
                            self.updateMapState(self.mapp)
                    elif mx in range(500,540) and my in range(28,68):
                        self.loadTitle()
                        if self.mapnum < 10:
                            self.mapnum += 1
                            self.readMapFile()
                            self.updateMapState(self.mapp)
                        elif self.mapnum == 10:
                            self.mapnum = 1
                            self.readMapFile()
                            self.updateMapState(self.mapp)
                    elif mx in range(220,280) and my in range(450,480):
                        # perform breadth-first search
                        self.player.setSearchAlgorithm("bfs")
                        self.player.searchAlgorithm.description()
                        self.player.play()
                    elif mx in range(300,360) and my in range(450,480):
                        # perform depth-first search
                        self.player.setSearchAlgorithm("dfs")
                        self.player.searchAlgorithm.description()
                        self.player.play()
                    elif mx in range(380,440) and my in range(450,480):
                        self.player.setSearchAlgorithm("astar")
                        self.player.searchAlgorithm.description()
                        self.player.play()
                    elif mx in range(440,550) and my in range(450,480):
                        print('Reset map.\n')
                        self.loadTitle()
                        self.updateMapState(self.mapp)
