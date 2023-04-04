import pygame as py
import random
import time
import items
current_time = time.time()

py.init()

#Game Window
WIN = py.display.set_mode((800,700))
clock = py.time.Clock()

#Background
background_image = py.image.load("Resources/desert2.jpg")
sun_image = py.image.load("Resources/sun.png")


#Time/Score
font_time = py.font.Font('freesansbold.ttf', 48)
def show_time():
    score = font_time.render(str(int(time.time()-current_time)), True, (255, 255, 255))
    WIN.blit(score, (15, 15))


##########################################################################
Item_List=[items.Bottle,items.Fruit,items.Burger,items.Soda]

Item_set=[]



#Items
def Items(j):
    #for k in range():
    for i in range(5):
        Item_set.append(Item_List[random.randint(0,3)])
    
    Item_set[j].update(Item_set[j].vel)
    WIN.blit(Item_set[j].image,(Item_set[j].pos_X, Item_set[j].pos_Y))
    list.clear(Item_set)    

##########################################################################




#Player
class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos_X = 375
        self.pos_Y = 510
        self.vel = 0
        
    def update(self,vel,picture_path):
        self.image = py.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.pos_X += vel
        if self.pos_X >= 730:
            self.pos_X = 730
        if self.pos_X <= 6:
            self.pos_X = 6
        self.rect.center = [self.pos_X, self.pos_Y]
        WIN.blit(self.image,(self.pos_X, self.pos_Y))

vel_Player = 0
Player_state = 1
Players_picmap = ["Resources/manleft.png","Resources/man.png", "Resources/manright.png"]
PlayerCenter = Player()
Player_group = py.sprite.Group
Player_group.add(PlayerCenter)

#Game Looping
running = True
while running:
    for event in py.event.get():
        if event.type is py.QUIT:
            running = False

        if event.type == py.KEYDOWN:
            if event.key == py.K_RIGHT:
                Player_state = 2
                vel_Player = 6.9
            
            if event.key == py.K_LEFT:
                Player_state = 0
                vel_Player = -6.9
        
        if event.type == py.KEYUP:
            if event.key == py.K_RIGHT or event.key == py.K_LEFT:
                Player_state = 1
                vel_Player = 0
    
    py.display.flip()
    WIN.blit(background_image,(0,0))
    WIN.blit(sun_image,(650, -80))
##################################   
    for j in range(5):
        Items(j)
##################################
    PlayerCenter.update(vel_Player, Players_picmap[Player_state])
    show_time()
    clock.tick(60)

py.quit()
