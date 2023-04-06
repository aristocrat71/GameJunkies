import pygame as py
import random
class Water(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("Resources/water.png")
        self.pos_X = random.randint(10,726)
        self.pos_Y = random.randint(5,100)
        self.vel = 2
        
    def update(self,vel):
        
        self.rect = self.image.get_rect()
        self.pos_Y += vel
        self.rect.center = [self.pos_X, self.pos_Y]
        if self.pos_Y >= 545:
            self.pos_Y = random.randint(5,100)
            self.pos_X = random.randint(10,726)
        #WIN.blit(self.image,(self.pos_X, self.pos_Y))




Bottle = Water()
Water_group = py.sprite.Group
Water_group.add(Bottle)

class Cola(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("Resources/cola.png")
        self.pos_X = random.randint(10,726)
        self.pos_Y = random.randint(5,100)
        self.vel = 2
        
    def update(self,vel):
        
        self.rect = self.image.get_rect()
        self.pos_Y += vel
        if self.pos_Y >= 545:
            self.pos_Y = random.randint(5,100)
            self.pos_X = random.randint(10,726)
        self.rect.center = [self.pos_X, self.pos_Y]
        #WIN.blit(self.image,(self.pos_X, self.pos_Y))




Soda = Cola()
Cola_group = py.sprite.Group
Cola_group.add(Soda)

class Watermelon(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("Resources/watermelon.png")
        self.pos_X = random.randint(10,726)
        self.pos_Y = random.randint(5,100)
        self.vel = 2
        
    def update(self,vel):
        
        self.rect = self.image.get_rect()
        self.pos_Y += vel
        if self.pos_Y >= 545:
            self.pos_Y = random.randint(5,100)
            self.pos_X = random.randint(10,726)
        self.rect.center = [self.pos_X, self.pos_Y]
        #WIN.blit(self.image,(self.pos_X, self.pos_Y))



Fruit = Watermelon()
Watermelon_group = py.sprite.Group
Watermelon_group.add(Fruit)

class Hamburger(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("Resources/Hamburger.png")
        self.pos_X = random.randint(10,726)
        self.pos_Y = random.randint(5,100)
        self.vel = 2
        
    def update(self,vel):
        
        self.rect = self.image.get_rect()
        self.pos_Y += vel
        if self.pos_Y >= 545:
            self.pos_Y = random.randint(5,100)
            self.pos_X = random.randint(10,726)
        self.rect.center = [self.pos_X, self.pos_Y]
        #WIN.blit(self.image,(self.pos_X, self.pos_Y))




Burger = Hamburger()
Hamburger_group = py.sprite.Group
Hamburger_group.add(Burger)