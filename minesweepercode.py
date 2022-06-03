import pygame, random, time
pygame.init()
win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("MineSweeper")
cubes = [pygame.image.load("pictures/Emptysqr.png"), pygame.image.load("pictures/1sqr.png"), pygame.image.load("pictures/2sqr.png"), pygame.image.load("pictures/3sqr.png"), pygame.image.load("pictures/4sqr.png"), pygame.image.load("pictures/5sqr.png"), pygame.image.load("pictures/6sqr.png"), pygame.image.load("pictures/7sqr.png"), pygame.image.load("pictures/8sqr.png")]
flag = pygame.image.load("pictures/flagsqr.png")
pressed = pygame.image.load("pictures/pressedsqr.png")
bomb = pygame.image.load("pictures/bombsqr.png")
clock = pygame.time.Clock()
minexandy = []
cubes2 = []
blank = []
run = True
lost = False
squaresdraw = True
randx = random.randrange(0, 400, 20)
randy = random.randrange(0, 400, 20)
width = 20
height = 20
yellow = (255, 255, 0)
count = 0
class squares:
    def __init__(self, x, y, mine):
        self.x = x
        self.y = y
        self.mine = mine
        self.counter = 0
        self.pressable = True
        self.blank = False
        self.checking = True
        self.flag = False
    def draw(self):
        if self.mine:
            if not(self.pressable):
                win.blit(bomb, (self.x, self.y))
            else:
                    win.blit(pressed, (self.x, self.y))
        else:
            if self.pressable:
                win.blit(pressed, (self.x, self.y))
            else:
                win.blit(cubes[self.counter], (self.x, self.y))

            for blank1 in blank:
                if blank1.pressable:
                    if not(blank1.flag):
                        win.blit(pressed, (blank1.x, blank1.y))
                else:
                    win.blit(cubes[0], (blank1.x, blank1.y))
                    blank.remove(blank1)

        if self.flag:
            win.blit(flag, (self.x, self.y))


    def move(self):
        if (self.x <= mpos[0] <= self.x + width) and (self.y <= mpos[1] <= self.y + height) and mpress == (1, 0, 0) and not(self.flag):
            if self.mine:
                lost()
            self.pressable = False

        elif (self.x <= mpos[0] <= self.x + width) and (self.y <= mpos[1] <= self.y + height) and mpress == (0, 0, 1) and self.pressable:
            if not(self.flag):
                self.flag = True
        elif (self.x <= mpos[0] <= self.x + width) and (self.y <= mpos[1] <= self.y + height) and mpress == (0, 1, 0):
            if self.flag:
                self.flag = False
                self.pressable = True


        if self.checking:
            for i in range(len(minexandy)):
                if minexandy[i][0] == self.x - width and minexandy[i][1] == self.y - height:
                    self.counter += 1
                if minexandy[i][0] == self.x + width and minexandy[i][1] == self.y + height:
                    self.counter += 1
                if minexandy[i][0] == self.x + width and minexandy[i][1] == self.y - height:
                    self.counter += 1
                if minexandy[i][0] == self.x - width and minexandy[i][1] == self.y + height:
                    self.counter += 1
                if minexandy[i][0] == self.x - width and minexandy[i][1] == self.y:
                    self.counter += 1
                if minexandy[i][0] == self.x + width and minexandy[i][1] == self.y:
                    self.counter += 1
                if minexandy[i][0] == self.x and minexandy[i][1] == self.y + height:
                    self.counter += 1
                if minexandy[i][0] == self.x and minexandy[i][1] == self.y - height:
                    self.counter += 1
            self.checking = False

        if self.counter == 0 and not(self.mine):
            if not(self.blank):
                    blank.append(self)
                    self.blank = True

        if not(self.pressable):
            if self.blank:
                for blank1 in blank:
                    if self.x == blank1.x and self.y == blank1.y + height:
                        blank1.pressable = False
                    if self.x == blank1.x - width and self.y == blank1.y:
                        blank1.pressable = False
                    if self.x == blank1.x + width and self.y == blank1.y:
                        blank1.pressable = False
                    if self.x == blank1.x and self.y == blank1.y - height:
                        blank1.pressable = False

def lost():
    global run
    for cube in cubes2:
        if cube.mine:
            cube.pressable = False
            cube.draw()
    run = False


while squaresdraw:
    if count < 80:
        if (randx, randy) not in minexandy:
            minexandy.append((randx, randy))
            cubes2.append(squares(randx, randy, True))
            randx = random.randrange(0, 400, 20)
            randy = random.randrange(0, 400, 20)
            count += 1
        else:
            randx = random.randrange(0, 400, 20)
            randy = random.randrange(0, 400, 20)
    else:
        for x in range(0, 400, 20):
            for y in range(0, 400, 20):
                    if (x, y) not in minexandy:
                        cubes2.append(squares(x, y, False))
                    if x == 380 and y == 380:
                        squaresdraw = False

def redrawGameWindow():
    for cube in cubes2:
        cube.move()
        cube.draw()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    mpos = pygame.mouse.get_pos()
    mpress = pygame.mouse.get_pressed()
    redrawGameWindow()
    pygame.display.update()
pygame.quit()