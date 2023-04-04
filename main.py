import pygame as py
import random
import time
#current_time = time.time()


##################################        DAY 2          #############################

py.init()

#Game Window
WIN = py.display.set_mode((800,700))
clock = py.time.Clock()
py.display.set_caption("Hydration Hero")
game_icon = py.image.load("Resources/water.png")
py.display.set_icon(game_icon)

#Game Screens
is_splashscreen = True
is_infoscreen = False
is_mainscreen = False
is_endscreen = False


#Backgrounds
background_image = py.image.load("Resources/desert2.jpg")
backgroud_start_image = py.image.load("Resources/desertmenu.jpg")
sun_image = py.image.load("Resources/sun.png")


#SplashScreen
font_splash_title = py.font.Font('Resources/newfont.otf', 90)
font_splash_credit = py.font.Font('Resources/newfont.otf', 35)
def splash_screen():
    titlemsg1 = font_splash_title.render("Hydration Hero", True, (255, 255, 255))
    WIN.blit(titlemsg1, (50, 100))
    titlemsg2 = font_splash_credit.render("Made by GameJunkies", True, (255, 255, 255))
    WIN.blit(titlemsg2, (330, 300))
    titlemsg3 = font_splash_credit.render("Press Enter :)", True, (255, 255, 255))
    WIN.blit(titlemsg3, (250, 520))

#InfoScreen
font_info = py.font.Font('Resources/newfont.otf', 36)
font_info2 = py.font.Font('Resources/newfont.otf', 28)
water = py.image.load("Resources/water.png")
watermelon = py.image.load("Resources/watermelon.png")
burger = py.image.load("Resources/hamburger.png")
cola = py.image.load("Resources/cola.png")
def info_screen():
    infomesgstrings= ["You are roaming a desert", "You must survive as long as you can", "Stay Hydrated to Stay Alive", ": Waterbottle", ": Coke", ": Burger", ": Watermelon"]
    infomsg = [font_info.render(infomesgstrings[0], True, (255, 255, 255)), font_info.render(infomesgstrings[1], True, (255, 255, 255)), font_info.render(infomesgstrings[2], True, (255, 255, 255)), font_info2.render(infomesgstrings[3], True, (255, 255, 255)), font_info2.render(infomesgstrings[4], True, (255, 255, 255)), font_info2.render(infomesgstrings[5], True, (255, 255, 255)), font_info2.render(infomesgstrings[6], True, (255, 255, 255)), font_splash_credit.render("Press Enter to Play :)", True, (255, 255, 255))]

    WIN.blit(infomsg[0], (50, 100))
    WIN.blit(infomsg[1], (50, 140))
    WIN.blit(infomsg[2], (50, 180))
    WIN.blit(water,(300, 300))
    WIN.blit(infomsg[3], (340, 300))
    WIN.blit(cola,(300, 350))
    WIN.blit(infomsg[4], (340, 350))
    WIN.blit(burger,(300, 400))
    WIN.blit(infomsg[5], (340, 400))
    WIN.blit(watermelon,(300, 450))
    WIN.blit(infomsg[6], (340, 450))
    WIN.blit(infomsg[7], (230, 550))


#End Screen
font_end = py.font.Font('Resources/newfont.otf', 90)
font_end2 = py.font.Font('Resources/newfont.otf', 48)
font_end3 = py.font.Font('Resources/newfont.otf', 36)
def end_screen():
    endmsg = font_end.render("Game Over", True, (255, 255, 255))
    WIN.blit(endmsg, (50, 100))
    scoremsg = font_end2.render("Your score: "+str(final_score), True, (255, 255, 255))
    WIN.blit(scoremsg, (400, 250))
    retrymsg = font_end3.render("Press Enter to retry", True, (255, 255, 255))
    WIN.blit(retrymsg, (250, 550))
    gamequitmsg = font_end3.render("Press Esc to quit", True, (255, 255, 255))
    WIN.blit(gamequitmsg, (250, 600))



#Time/Score
font_time = py.font.Font('Resources/newfont.otf', 52)
def show_time():
    score = font_time.render(str(int(time.time()-current_time)), True, (255, 255, 255))
    WIN.blit(score, (15, 15))


#Player
class Player(py.sprite.Sprite):
    def __init__(self, picturepath):
        super().__init__()
        self.pos_X = 375
        self.pos_Y = 510
        self.vel = 0
        self.image = py.image.load(picturepath)
        self.rect = self.image.get_rect()
        
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
PlayerCenter = Player("Resources/man.png")
Player_group = py.sprite.Group
Player_group.add(PlayerCenter)

#Helpers
class Helpers(py.sprite.Sprite):
    def __init__(self, picturepath):
        super().__init__()
        self.image = py.image.load(picturepath)
        self.pos_X = random.randint(10,726)
        self.pos_Y = random.randint(5,50)
        self.vel = random.randint(1, 3)
        self.rect = self.image.get_rect()
    
    def update(self):
        self.pos_Y += self.vel
        self.rect.center = [self.pos_X, self.pos_Y]
        WIN.blit(self.image, (self.pos_X, self.pos_Y))
        if self.pos_Y > 530:
            return True

    def collide(self, Playerrect):
        return self.rect.colliderect(Playerrect)

helpers = [Helpers("Resources/water.png"), Helpers("Resources/watermelon.png")]

#Enemy
class Enemy(py.sprite.Sprite):
    def __init__(self, picturepath):
        super().__init__()
        self.image = py.image.load(picturepath)
        self.pos_X = random.randint(10,726)
        self.pos_Y = random.randint(5,50)
        self.vel = random.randint(1, 4)
        self.rect = self.image.get_rect()
    
    def update(self):
        self.pos_Y += self.vel
        self.rect.center = [self.pos_X, self.pos_Y]
        WIN.blit(self.image, (self.pos_X, self.pos_Y))
        if self.pos_Y > 530:
            return True

    def collide(self, Playerrect):
        return self.rect.colliderect(Playerrect)

enemies = [Enemy("Resources/cola.png"), Enemy("Resources/hamburger.png")]


#Health_Bar

hydro_key = 0
class health_bar(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.current_health = 200
        self.max_health = 200
        self.healthbar_length = 300
        self.health_ratio = self.max_health/self.healthbar_length
        
    def get_damage(self, amount):
        if self.current_health >0:
            self.current_health -=amount
        if self.current_health <=0:
            self.current_health =0
    
    def update(self):
        self.basic_health()
        
    def get_health(self, amount):
        if self.current_health <self.max_health:
            self.current_health +=amount
        if self.current_health >=self.max_health:
            self.current_health = 200

    def basic_health(self):
        py.draw.rect(WIN, (0,255,255),(10,650,self.current_health/self.health_ratio, 25))
        py.draw.rect(WIN, (0,0,0),(10,650,self.healthbar_length, 25), 4)

hydrometer = health_bar()


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

            if event.key == py.K_RETURN:
                if is_splashscreen == True:
                    is_splashscreen = False
                    is_infoscreen = True
                    break

                if is_infoscreen == True:
                    is_infoscreen = False
                    is_mainscreen = True
                    current_time = time.time()
                    break

                if is_endscreen == True:
                    is_endscreen = False
                    is_infoscreen = True
                    break
        
            if event.key == py.K_ESCAPE and is_endscreen == True:
                running = False
            
            if event.key == py.K_SPACE:
                hydro_key=1
            if event.key == py.K_BACKSPACE:
                hydro_key=2

        if event.type == py.KEYUP:
            if event.key == py.K_RIGHT or event.key == py.K_LEFT:
                Player_state = 1
                vel_Player = 0
            
            if event.key == py.K_BACKSPACE or event.key == py.K_SPACE: 
                hydro_key = 0
    
    py.display.flip()

    if is_splashscreen == True:
        WIN.blit(backgroud_start_image, (0,0))
        splash_screen()
    
    if is_infoscreen == True:
        WIN.blit(backgroud_start_image, (0,0))
        info_screen()
        

    if is_mainscreen == True:
        current_timestamp = int(time.time()-current_time)
        if current_timestamp >= 57:
            current_timestamp = 57

        WIN.blit(background_image,(0,0))
        WIN.blit(sun_image,(650, -80))
        hydrometer.basic_health() 
        hydrometer.get_damage(0.001*current_timestamp)
        if hydrometer.current_health <=0:
            is_mainscreen = False
            is_endscreen = True
            final_score = int(time.time()-current_time)
            hydrometer.current_health = 200
            continue
        if enemies[0].update() or enemies[0].collide(PlayerCenter.rect):
            if enemies[0].collide(PlayerCenter.rect):
                hydrometer.get_damage(5)
            enemies[0].pos_X = random.randint(10,726)
            enemies[0].pos_Y = random.randint(5,50)
            enemies[0].vel = random.randint(1, 3)

        if enemies[1].update() or enemies[1].collide(PlayerCenter.rect):
            if enemies[1].collide(PlayerCenter.rect):
                hydrometer.get_damage(5)
            enemies[1].pos_X = random.randint(10,726)
            enemies[1].pos_Y = random.randint(5,50)
            enemies[1].vel = random.randint(1, 3)

        if helpers[0].update() or helpers[0].collide(PlayerCenter.rect):
            if helpers[0].collide(PlayerCenter.rect):
                hydrometer.get_health(5)
            helpers[0].pos_X = random.randint(10,726)
            helpers[0].pos_Y = random.randint(5,50)
            helpers[0].vel = random.randint(1, 3)

        if helpers[1].update() or helpers[1].collide(PlayerCenter.rect):
            if helpers[1].collide(PlayerCenter.rect):
                hydrometer.get_health(5)
            helpers[1].pos_X = random.randint(10,726)
            helpers[1].pos_Y = random.randint(5,50)
            helpers[1].vel = random.randint(1, 3)
        
        PlayerCenter.update(vel_Player, Players_picmap[Player_state])
        show_time()

    if is_endscreen == True:
        WIN.blit(backgroud_start_image, (0,0))
        end_screen()
    
    clock.tick(120)

py.quit()
