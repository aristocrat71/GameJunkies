import pygame as py
import random
import time
import math
#current_time = time.time()


##################################        DAY 4          #############################

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


#Sounds
eatSound = py.mixer.Sound("Resources/eat.mp3")
drinkSound = py.mixer.Sound("Resources/gulping.mp3")
eatSound.set_volume(1.0)
menuMusic = py.mixer.Sound("Resources/maintheme.mp3")
menuMusic.play()
ingameMusic = py.mixer.Sound("Resources/ingame.mp3")
ingameMusic.set_volume(0.3)


#SplashScreen
font_splash_title = py.font.Font('Resources/newfont.otf', 90)
font_splash_credit = py.font.Font('Resources/newfont.otf', 36)
def splash_screen():
    titlemsg1 = font_splash_title.render("Hydration Hero", True, (0, 255, 255))
    WIN.blit(titlemsg1, (50, 80 + 30*math.sin(time.time())))
    titlemsg2 = font_splash_credit.render("Made by GameJunkies", True, (255, 255, 255))
    WIN.blit(titlemsg2, (330, 300))
    titlemsg3 = font_splash_credit.render("Press Enter :)", True, (255, 255, 255))
    WIN.blit(titlemsg3, (250, 520 + 15*math.sin(time.time())))

#InfoScreen

font_info = py.font.Font('Resources/newfont.otf', 55)
font_info2 = py.font.Font('Resources/newfont.otf', 30)
water = py.image.load("Resources/water.png")
watermelon = py.image.load("Resources/watermelon.png")
burger = py.image.load("Resources/hamburger.png")
cola = py.image.load("Resources/cola.png")
def info_screen():
    infomesgstrings= ["You are roaming a desert", "You must survive as long as you can", "Press left right arrow to move", "Easy right ?!", "Collecting: ", "Helps you stay hydrated", "Will harm (dehydrate) your body", "Stay hydrated to prevent fainting !", "SAME AS IN REAL LIFE !!!"]
    howtoplay = font_info.render("How to play", True, (0, 255, 255))

    infomsg = [font_info2.render(infomesgstrings[0], True, (255, 255, 255)), font_info2.render(infomesgstrings[1], True, (255, 255, 255)), font_info2.render(infomesgstrings[2], True, (0, 255, 255)), font_info2.render(infomesgstrings[3], True, (255, 255, 255)), font_info2.render(infomesgstrings[4], True, (255, 255, 255)), font_info2.render(infomesgstrings[5], True, (255, 255, 255)), font_info2.render(infomesgstrings[6], True, (255, 255, 255)), font_info2.render(infomesgstrings[7], True, (0, 255, 255)), font_info2.render(infomesgstrings[8], True, (0, 255, 255)),font_splash_credit.render("Press Enter to Play :)", True, (255, 255, 255))]

    WIN.blit(howtoplay, (270, 10))
    WIN.blit(infomsg[0], (50, 90))
    WIN.blit(infomsg[1], (50, 120))
    WIN.blit(infomsg[2], (50, 180))
    WIN.blit(infomsg[4], (50, 240)) 
    WIN.blit(infomsg[5], (180, 290)) 
    WIN.blit(water, (80, 280))
    WIN.blit(watermelon, (130, 290))
    WIN.blit(infomsg[6], (180, 330))
    WIN.blit(cola, (80, 330))
    WIN.blit(burger, (130, 330))
    WIN.blit(infomsg[7], (50, 390))
    WIN.blit(infomsg[8], (200, 480))
    WIN.blit(infomsg[9], (210, 620 + 20*math.sin(time.time())))


#End Screen
font_end = py.font.Font('Resources/newfont.otf', 90)
font_end2 = py.font.Font('Resources/newfont.otf', 48)
font_end3 = py.font.Font('Resources/newfont.otf', 36)
font_end4 = py.font.Font('Resources/newfont.otf', 22)
def end_screen():
    endmsg = font_end.render("You Fainted", True, (255, 255, 255))
    WIN.blit(endmsg, (50, 100 + 30*math.sin(time.time())))
    scoremsg = font_end2.render("Your score: "+str(final_score), True, (255, 255, 255))
    WIN.blit(scoremsg, (400, 250))
    endmsg=font_end4.render(end_Texts[end_Text_Index][0],True,(0,255,255))
    WIN.blit(endmsg,(20,370))
    if len(end_Texts[end_Text_Index])>1:
        endmsg=font_end4.render(end_Texts[end_Text_Index][1],True,(0,255,255))
        WIN.blit(endmsg,(20,403))
    retrymsg = font_end3.render("Press Enter to retry", True, (255, 255, 255))
    WIN.blit(retrymsg, (250, 550 + 15*math.sin(time.time()-0.5)))
    gamequitmsg = font_end3.render("Press Esc to quit", True, (255, 255, 255))
    WIN.blit(gamequitmsg, (250, 600 + 15*math.sin(time.time()-0.5)))

end_Texts = [["The human body is composed of approximately 60% water, making"," proper hydration essential for optimal health"],["Water helps regulate body temperature and maintain electrolyte"," balance"],["Dehydration can cause fatigue, headaches, and impaired cognitive ","function"],["Drinking enough water can help prevent constipation and promote ","regular bowel movements"],["Adequate hydration can help prevent kidney stones and urinary ","tract infections"],["Proper hydration can help prevent muscle cramps and improve ","physical performance"],["Drinking water can help control appetite and support weight loss ","efforts"],["Hydration can improve skin health and reduce the appearance of ","wrinkles"],["Drinking water can help reduce the risk of certain cancers, ","including colon and bladder cancer"], ["Proper hydration can help reduce the risk of heat stroke and ","other heat-related illnesses"],["Drinking water can help support immunesystem function and fight ","off infections"],["Hydration is important for heart health and can help reduce the ","risk of heart disease"],["Proper hydration can help improve sleep quality and duration"],["Drinking water can help alleviate symptoms of hangovers and ","prevent alcohol-related dehydration"],["Adequate hydration is important for athletes to maintain ","performance and prevent injury"],["Hydration can help improve mental clarity and concentration"],["Proper hydration can help reduce the risk of developing certain ","types of kidney disease"],["Drinking water can help reduce inflammation in the body, which ","is associated with various health issues"]]

ingame_Texts = ["Drink water !!", "Avoid cokes !!", "Say Nooo burgers", "Say Yesss watermelons", "Exercise Daily !"]
ingame_font = py.font.Font('Resources/newfont.otf', 30)
ingame_msg = ingame_font.render(ingame_Texts[random.randint(0,4)], True, (0, 255, 200))


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
        self.left_pressed=False
        self.right_pressed=False
        
    def update(self,picture_path):
        self.image = py.image.load(picture_path[1])
        self.rect = self.image.get_rect()
        self.vel = 0
        if self.left_pressed and not self.right_pressed:
            self.vel=-6
            self.playerstate=0
            self.image = py.image.load(picture_path[0])
        if self.right_pressed and not self.left_pressed:
            self.vel=6
            self.playerstate=2
            self.image = py.image.load(picture_path[2])
        self.pos_X += self.vel
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


#Velocity Capping
upper_cap = 3
lower_cap = 1

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
        
    def get_health(self, amount):
        if self.current_health <self.max_health:
            self.current_health +=amount
        if self.current_health >=self.max_health:
            self.current_health = 200

    def basic_health(self,warning_red):
        if warning_red:
            py.draw.rect(WIN, (240,0,0),(10,630,self.current_health/self.health_ratio, 38))
        else:
            py.draw.rect(WIN, (0,255,255),(10,630,self.current_health/self.health_ratio, 38))
            py.draw.rect(WIN, (0,0,0),(10,630,self.healthbar_length, 38), 4)

font_hydro = py.font.Font('Resources/newfont.otf', 32)
hydrodisplay = font_hydro.render("HYDRATION", True, (0,0,0))

hydrometer = health_bar()
warning_red = False

#Game Looping
running = True
while running:
    for event in py.event.get():
        if event.type is py.QUIT:
            running = False

        if event.type == py.KEYDOWN:
            if event.key == py.K_RIGHT:
                PlayerCenter.right_pressed=True
            
            if event.key == py.K_LEFT:
                PlayerCenter.left_pressed=True

            if event.key == py.K_RETURN:
                if is_splashscreen == True:
                    is_splashscreen = False
                    is_infoscreen = True
                    break

                if is_infoscreen == True:
                    is_infoscreen = False
                    menuMusic.stop()
                    ingameMusic.play(loops=1000)
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
            if event.key == py.K_RIGHT: 
                PlayerCenter.right_pressed = False
            if event.key == py.K_LEFT:
                PlayerCenter.left_pressed = False
            
            if event.key == py.K_BACKSPACE or event.key == py.K_SPACE: 
                hydro_key = 0
    
    py.display.flip()

    if is_splashscreen == True:
        WIN.blit(backgroud_start_image, (0,0))
        splash_screen()
    
    if is_infoscreen == True:
        WIN.blit(backgroud_start_image, (0,0))
        end_Text_Index=random.randint(0,17)
        info_screen()
        

    if is_mainscreen == True:
        timestamp_sun = int(time.time()-current_time)
        if timestamp_sun >= 60:
            timestamp_sun = 55

        timestamp_main = int(time.time()-current_time)

        WIN.blit(background_image,(0,0))
        WIN.blit(sun_image,(650, -80))
        hydrometer.basic_health(warning_red) 
        hydrometer.get_damage(0.001*timestamp_sun)

        if hydrometer.current_health <= 75:
            warning_red = True
        else:
            warning_red = False

        if hydrometer.current_health <=0:
            is_mainscreen = False
            is_endscreen = True
            final_score = int(time.time()-current_time)
            warning_red = False
            hydrometer.current_health = 200
            continue
        
        if 60 < timestamp_main:
            upper_cap = 5
            lower_cap = 3

        if timestamp_main%10 == 0:
            ingame_msg = ingame_font.render(ingame_Texts[random.randint(0,4)], True, (0, 255, 255))
        WIN.blit(ingame_msg, (260, 180+ + 15*math.sin(time.time())))
            

        if enemies[0].update() or enemies[0].collide(PlayerCenter.rect):
            if enemies[0].collide(PlayerCenter.rect):
                drinkSound.play()
                hydrometer.get_damage(5)
            enemies[0].pos_X = random.randint(10,726)
            enemies[0].pos_Y = random.randint(5,50)
            enemies[0].vel = random.randint(lower_cap, upper_cap)

        if enemies[1].update() or enemies[1].collide(PlayerCenter.rect):
            if enemies[1].collide(PlayerCenter.rect):
                eatSound.play()
                hydrometer.get_damage(5)
            enemies[1].pos_X = random.randint(10,726)
            enemies[1].pos_Y = random.randint(5,50)
            enemies[1].vel = random.randint(lower_cap, upper_cap)

        if helpers[0].update() or helpers[0].collide(PlayerCenter.rect):
            if helpers[0].collide(PlayerCenter.rect):
                drinkSound.play()
                hydrometer.get_health(5)
            helpers[0].pos_X = random.randint(10,726)
            helpers[0].pos_Y = random.randint(5,50)
            helpers[0].vel = random.randint(lower_cap, upper_cap)

        if helpers[1].update() or helpers[1].collide(PlayerCenter.rect):
            if helpers[1].collide(PlayerCenter.rect):
                eatSound.play()
                hydrometer.get_health(5)
            helpers[1].pos_X = random.randint(10,726)
            helpers[1].pos_Y = random.randint(5,50)
            helpers[1].vel = random.randint(lower_cap, upper_cap)
        
        #ALSO PLAYER MOVEMENT SPEED
        WIN.blit(hydrodisplay, (67, 630))

        PlayerCenter.update(Players_picmap)
        show_time()

    if is_endscreen == True:
        WIN.blit(backgroud_start_image, (0,0))
        end_screen()
    
    clock.tick(120)

py.quit()
