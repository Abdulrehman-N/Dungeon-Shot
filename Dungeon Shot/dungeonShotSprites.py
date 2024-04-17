'''
Abdulrehman Nakhuda
2022-01-18
Description:These are classes requried in order to the Dungeon Shot game.
These classes give control to the player, allow movement in images, scorekeep and check for losing.
These classes control all the objects inside of this game.
'''
import pygame, random

class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for the Player'''
    def __init__(self, screen, player_num):
        '''This initializer takes a screen surface, and player number as
        parameters.  Depending on the player number it loads the appropriate
        image and positions it on the left or right end of the court'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # This is for the bullet itself.
        if player_num == 1:
            self.__num=1
            self.sprites=[]
            self.sprites.append(pygame.image.load("bullet6.png"))
            self.sprites.append(pygame.image.load("boom1.png"))
            self.sprites.append(pygame.image.load("boom2.png"))
            self.sprites.append(pygame.image.load("boom3.png"))
            self.sprites.append(pygame.image.load("boom4.png"))
            self.sprites.append(pygame.image.load("boom5.png"))
            self.sprites.append(pygame.image.load("boom6.png"))
            self.sprites.append(pygame.image.load("boom7.png"))
            self.sprites.append(pygame.image.load("boom8.png"))
            self.__current=0
            self.image=self.sprites[self.__current]

            self.rect=self.image.get_rect()
            self.rect.top = screen.get_height()/2 + 50
            self.rect.left= 100+50
            self.__screen = screen
            self.__dy = 0
        # This is for the the glow of the bullet
        elif player_num==2:
            self.__num=2
            self.image= pygame.image.load("glow3.png")
            self.rect=self.image.get_rect()
            self.rect.center = (screen.get_width()/2,screen.get_height()/2)
            self.rect.top = screen.get_height()/2 -100
            self.rect.left= -120+50
            self.__screen = screen
            self.__dy = 0
        #This is for the explosion that occurs when the player loses.
        elif self.__num==3:
            self.sprites=[]
            self.sprites.append(pygame.image.load("boom1.png"))
            self.sprites.append(pygame.image.load("boom2.png"))
            self.sprites.append(pygame.image.load("boom3.png"))
            self.sprites.append(pygame.image.load("boom4.png"))
            self.sprites.append(pygame.image.load("boom5.png"))
            self.sprites.append(pygame.image.load("boom6.png"))
            self.sprites.append(pygame.image.load("boom7.png"))
            self.sprites.append(pygame.image.load("boom8.png"))
            self.__current=0
            self.image=self.sprites[self.__current]
            self.rect=self.image.get_rect()

    def change_direction(self, xy_change):
        '''This method takes a (x,y) tuple as a parameter, extracts the
        y element from it, and uses this to set the players y direction.'''
        self.__dy = xy_change[1]

    def death(self):
        '''This method takes registers the player as dead which later allows for the death animation to play.'''
        self.__num=3

    def update(self):
        '''This method will be called automatically to reposition the
        player sprite on the screen.'''
        #This is checking if it is the bullet or the glow or if it is when the bullet has died.
        #Then it acts accordingly.
        if self.__num==1:
            if ((self.rect.top > 100) and (self.__dy > 0)) or ((self.rect.bottom < self.__screen.get_height()-95) and (self.__dy < 0)):
                self.rect.top -= (self.__dy*20)
        elif self.__num==2:
            if ((self.rect.top > -50) and (self.__dy > 0)) or ((self.rect.bottom < self.__screen.get_height()+45) and (self.__dy < 0)):
                self.rect.top -= (self.__dy*20)
        elif self.__num==3:
            self.__current+=0.7 # This is a float so that it slows down the animaition a bit.
            if self.__current>= len(self.sprites):
                self.__current=8
            self.image=self.sprites[int(self.__current)]
        # If yes, then we don't change the y position of the player at all.

class EndZone(pygame.sprite.Sprite):
    '''This class defines the sprite for the left zone'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as a parameter'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Our endzone sprite will be a 1 pixel wide black line.
        self.image = pygame.Surface((1, screen.get_height()))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))

        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.left = -50
        self.rect.top = 100

class Scoretext(pygame.sprite.Sprite):
    '''This class defines the sprites that are static or dynamic.'''
    def __init__(self,screen,num):
        '''This initializer has the parameters screen and num'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.__screen=screen
        #This is for the scoreboard image on the top left
        if num==1:
            self.__numb=1
            self.image=pygame.image.load("scoreboard.png")
            self.rect=self.image.get_rect()
            self.rect.top=15
            self.rect.left=screen.get_width()-500
        #This is for the coin sprites in the game
        elif num==2:
            self.__numb=2
            self.image=pygame.image.load("coin2.png")
            self.rect=self.image.get_rect()
            self.rect.top=20
            self.rect.left=70
        #This is for the dark overlay
        elif num==3:
            self.__numb=3
            self.image=pygame.image.load("dark.png")
            self.rect=self.image.get_rect()
        #This is for the retry menu screen
        elif num==4:
            self.__numb=4
            self.image=pygame.image.load("retryscreen2.png")
            self.rect=self.image.get_rect()
            self.rect.top=-screen.get_height()
        #This is for the blinking text that says press space to retry.
        elif num==5:
            self.__numb=5
            self.sprites=[]
            self.sprites.append(pygame.image.load("boom8.png"))
            self.sprites.append(pygame.image.load("retrytext.png"))
            self.__current=0
            self.image=self.sprites[self.__current]
            self.rect=self.image.get_rect()
            self.rect.top=500
            self.rect.left=550
    def update(self):
        '''This method updates regularly'''
        #This is to move the retry screen down
        if self.__numb==4:
            if self.rect.bottom<=self.__screen.get_height()-10:
                self.rect.top+=30
        #This is to make the text blink
        if self.__numb==5:
            self.__current+=0.045
            if self.__current>= len(self.sprites):
                self.__current=0
            self.image=self.sprites[int(self.__current)]
class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self,num):
        '''This initializer loads the font "pixeboy", and
        sets the starting score to 0'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.__counter=0
        # Load our custom font, and initialize the starting score.
        #This is for the score to view in game
        if num==1:
            self.__font = pygame.font.Font("pixeboy.ttf", 120)
            self.__player1_score = 0
            self.__num=1
        #This if for the coin score
        elif num==2:
            self.__font = pygame.font.Font("pixeboy.ttf", 80)
            self.__player1_score = 0
            self.__num=2
        #This is for the end score
        elif num==3:
            self.__font = pygame.font.Font("pixeboy.ttf", 100)
            self.__player1_score = 0
            self.__num=3
            self.__message = str(self.__player1_score)
            self.image = self.__font.render(self.__message, 1, (219, 212, 11))
            self.rect = self.image.get_rect()
            self.rect.center = (750, -490)
        #This is for the end coin score
        elif num==4:
            self.__font = pygame.font.Font("pixeboy.ttf", 100)
            self.__player1_score = 0
            self.__num=4
            self.__message = str(self.__player1_score)
            self.image = self.__font.render(self.__message, 1, (219, 212, 11))
            self.rect = self.image.get_rect()
            self.rect.center = (750, -420)
        #This is for the end total score
        elif num==5:
            self.__font = pygame.font.Font("pixeboy.ttf", 120)
            self.__player1_score = 0
            self.__num=5
            self.__message = str(self.__player1_score)
            self.image = self.__font.render(self.__message, 1, (219, 212, 11))
            self.rect = self.image.get_rect()
            self.rect.center = (750, -300)

    def targetHit(self,types):
        '''This method adds one to the score for player 1'''
        if types==1:# If its a target, it adds 1 point
            self.__player1_score += 1
            self.__counter+=1
        if types==2:#If its a coin, it adds 3 points
            self.__player1_score += 3

    def lose(self,endzone,targets,player1,barriers,glow):
        '''This checks if the player has lost yet'''
        glows=pygame.sprite.Group(glow)
        if pygame.sprite.spritecollide(endzone,targets,False) and pygame.sprite.spritecollide(player1,glows,True) or pygame.sprite.spritecollide(player1,barriers,False) and pygame.sprite.spritecollide(player1,glows,True):
            return 1
        else:
            return 0
    def get_score(self):
        '''This runs every 10th score the player gets'''
        if self.__counter==10:
            self.__counter=0
            return 1

        else:
            return 0
    def update(self):
        '''This method will be called automatically to display
        the current score at the top of the game window.'''
        #This is for scoreboards
        if self.__num==1:
            self.__message = str(self.__player1_score)
            self.image = self.__font.render(self.__message, 1, (219, 212, 11))
            self.rect = self.image.get_rect()
            self.rect.center = (1150, 50)
        #This is for coin scoreboards
        elif self.__num==2:
            self.__message = str(self.__player1_score)
            self.image = self.__font.render(self.__message, 1, (219, 212, 11))
            self.rect = self.image.get_rect()
            self.rect.center = (150, 45)
        #This is for scoreboards at the end
        elif self.__num==3:
            self.__message = str(self.__player1_score)
            self.image = self.__font.render(self.__message, 1, (219, 212, 11))
            if self.rect.top<210:
                self.rect.top+=30
                if self.rect.top==232:
                    self.rect.top-=36
        #This is for scoreboard for coins at the end.
        elif self.__num==4:
            self.__message = str(self.__player1_score)
            self.image = self.__font.render(self.__message, 1, (219, 212, 11))
            if self.rect.top<280:
                self.rect.top+=30
                if self.rect.top==302:
                    self.rect.top-=10
        #This is total scoreboard displayed at the end
        elif self.__num==5:
            self.__message = str(self.__player1_score)
            self.image = self.__font.render(self.__message, 1, (255,255,255))
            if self.rect.top<400:
                self.rect.top+=30
                if self.rect.top==416:
                    self.rect.top-=45
class Bg(pygame.sprite.Sprite):
    '''This class defines the sprites for the moving background and other dynamic parts related to it'''
    def __init__(self,types,screen):
        '''This initializer requires the type it is and the screen'''
        pygame.sprite.Sprite.__init__(self)
        self.__speed=25
        self.__clock=49
        self.__flag=False
        self.__screen=screen
        #This checks if it is the long wall
        if types==1:
            self.__types=1
            self.image=pygame.image.load("longwall.jpg")
            self.rect=self.image.get_rect()
        #This checks if it is the top barrier
        elif types==2:
            self.__types=2
            self.image=pygame.image.load("topb.png")
            self.image.convert()
            self.rect=self.image.get_rect()
        #This checks if it is the bottom barrier
        elif types==3:
            self.__types=3
            self.image=pygame.image.load("bottomb.png")
            self.image.convert()
            self.rect=self.image.get_rect()
            self.rect.top=screen.get_height()-88
        #This checks for the menu, the top half
        elif types==4:
            self.__types=4
            self.image=pygame.image.load("tophalf.jpg")
            self.image.convert()
            self.rect=self.image.get_rect()
        #This checks for the menu, the bottom half
        elif types==5:
            self.__types=5
            self.image=pygame.image.load("bottomhalf3.png")
            self.image.convert()
            self.rect=self.image.get_rect()
            self.rect.top=360
        #This checks for the blinking space key symbol in the menu
        elif types==6:
            self.__types=6
            self.sprites=[]
            self.sprites.append(pygame.image.load("spacebaron.png"))
            self.sprites.append(pygame.image.load("spacebaroff.png"))
            self.__current=0
            self.image=self.sprites[self.__current]
            self.image.convert()
            self.rect=self.image.get_rect()
            self.rect.top=380
            self.rect.left=500
    def move(self,types):
        '''This method moves the walls in the menu out of the way.'''
        if types==1:
            self.rect.top+=15
        if types==2:
            self.rect.top-=15

    def bgset_speed(self,num):
        '''This method adjust the walls in the game.'''
        #This is if the time has slowed down
        if num==1:
            self.__speed=2
            self.__clock=49
        #This is regular speed
        elif num==2:
            self.__speed=25
            self.__clock=49
    def update(self):
        '''This method occurs regularly and updates the bg.'''
        #This checks if it is a top half
        if self.__types==4:
            self.rect.left=0
        #This checks if it is the top barrier
        elif self.__types==1:
            if self.rect.centerx<self.__clock:
                self.rect.left=-8 #It moves it with this speed.
            else:
                self.rect.left-=self.__speed
        #This is for the blinking space key symbol
        elif self.__types==6 and self.__flag:
            self.image=pygame.image.load("starttext2.png")
            self.rect=self.image.get_rect()
            self.rect.top=350
            self.rect.left=350
        #This is for the blinking space key symbol at its rate between appearing and disappearing.
        elif self.__types==6:
            self.__current+=0.045#Float value to slow down animation
            if self.__current>= len(self.sprites):
                self.__current=0
            self.image=self.sprites[int(self.__current)]
    def dismiss(self):
        '''This removes the spacebar and replaces it with the tip'''
        self.__flag=True
    def set_type(self):
        '''This method sets the type to 4 meaning that it will now refer to the the top half'''
        self.__types=4
class Targets(pygame.sprite.Sprite):
    '''This class creates the targets such as the targets themselves, coins and powerups'''
    def __init__(self,screen,types,speed,value):
        pygame.sprite.Sprite.__init__(self)
        self.__speed=speed
        self.__count=50
        self.__value=value
        self.__range=450
        #This is for the creation of the targets
        if types==1:
            self.image = pygame.image.load("target.png")
            self.rect = self.image.get_rect()
            self.rect.centerx = screen.get_width()+self.__range
            self.rect.top = random.randrange(100, screen.get_height()-152-100)
        #This is for the creation of the coins, They are spawned at a different place than the targets
        elif types==2:
            self.image = pygame.image.load("coin2.png")
            self.rect = self.image.get_rect()
            self.rect.centerx = screen.get_width()+10
            self.rect.top = random.randrange(100, screen.get_height()-152-100)
        #This is for the powerups and how they are created.
        elif types==3:
            self.image = pygame.image.load("powerup4.png")
            self.rect = self.image.get_rect()
            self.rect.centerx = screen.get_width()+2
            self.rect.top = self.__value
        #This is for the glow effect on the powerup.
        elif types==4:
            self.sprites=[]
            self.sprites.append(pygame.image.load("powerupglow.png"))
            self.sprites.append(pygame.image.load("boom8.png"))
            self.__current=0
            self.image=self.sprites[self.__current]
            self.rect = self.image.get_rect()
            self.rect.centerx = screen.get_width()+2
            self.rect.top = self.__value-50

    def change_sprite(self):
        '''This method changes the sprite and causes the glow to dissapear'''
        self.__current=1
        self.image=self.sprites[self.__current]
    def set_speed(self,num):
        '''This method sets the speed of which the targets, coins and powerups come at'''
        #This is when the power up is activated
        if num==1:
            self.__speed=10
        #This is when the powerup ends
        elif num==2:
            self.__speed=self.__count

    def update(self):
        '''This method occurs regularly and contstantly moves the targets'''
        #This causes the targets to move at the desired speed.
        self.rect.left-=self.__speed




