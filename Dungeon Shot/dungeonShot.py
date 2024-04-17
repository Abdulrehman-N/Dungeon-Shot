'''
Abdulrehman Nakhuda
2022-01-18
Description: This game is about where you control a bullet a hit the targets to get score and also to survive.
it also has coins to boost your score and also a powerup that slows down time for a limited time.
The user is controlled by holding the space bar.
'''


# I - IMPORT AND INITIALIZE
import pygame, dungeonShotSprites,random
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280,720))

# Create a list of Joystick objects.


def main(sound):
    '''This function defines the 'mainline logic' for the Dungeon Shot game.'''

    # DISPLAY
    pygame.display.set_caption("Dungeon Shot - Abdulrehman Nakhuda")
    programIcon = pygame.image.load("bullet6.png")

    pygame.display.set_icon(programIcon)

    # ENTITIES
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))
    screen.blit(background, (0, 0))

    # Sprites for: ScoreKeeper label, End Zones, Bullet, and Players, coins, powerups, targets, sprites
    flag=False
    flag3=True
    flag8=True
    score1=0
    score2=0
    counter=0
    timer=0
    value=random.randrange(100, screen.get_height()-152-100)
    speed=50
    rate=35
    flag2=False
    timerstart=False
    target=dungeonShotSprites.Targets(screen,1,speed,value)
    targets=pygame.sprite.Group(target)
    scoreSprite=dungeonShotSprites.Scoretext(screen,1)
    coin=dungeonShotSprites.Targets(screen,2,speed,value)
    coins=pygame.sprite.Group(target)
    endzone=dungeonShotSprites.EndZone(screen)
    bg=dungeonShotSprites.Bg(1,screen)
    topb=dungeonShotSprites.Bg(2,screen)
    bottomb=dungeonShotSprites.Bg(3,screen)
    barriers=pygame.sprite.Group(topb,bottomb)
    coinScoreKeep=dungeonShotSprites.ScoreKeeper(2)
    endcoinscore=dungeonShotSprites.ScoreKeeper(4)
    player1 = dungeonShotSprites.Player(screen, 1)
    bulletglow=dungeonShotSprites.Player(screen,2)
    score=dungeonShotSprites.ScoreKeeper(1)
    endscore=dungeonShotSprites.ScoreKeeper(3)
    coinscore=dungeonShotSprites.Scoretext(screen,2)
    overlay=dungeonShotSprites.Scoretext(screen,3)
    gameover=dungeonShotSprites.Scoretext(screen,4)
    totalScore=dungeonShotSprites.ScoreKeeper(5)
    retrytext=dungeonShotSprites.Scoretext(screen,5)
    powerup=dungeonShotSprites.Targets(screen,3,speed,value)
    powerups=pygame.sprite.Group(target)
    powerupglow=dungeonShotSprites.Targets(screen,4,speed,value)
    powerupglows=pygame.sprite.Group(target)
    allSprites = pygame.sprite.Group(bg,endzone,targets,coins,bulletglow,player1,barriers,score,scoreSprite,coinscore,coinScoreKeep)

    #Music entities
    pygame.mixer.music.load("ingamemusic.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    explode=pygame.mixer.Sound("explode2.mp3")
    hit=pygame.mixer.Sound("hitsound.mp3")
    hit.set_volume(0.2)
    coinsound=pygame.mixer.Sound("coin.mp3")
    rewind=pygame.mixer.Sound("rewind.mp3")
    speedup=pygame.mixer.Sound("speedup2.mp3")
    retrysound=pygame.mixer.Sound("retrysound.mp3")
    if sound==True:
        pygame.mixer.music.set_volume(0)
        explode.set_volume(0)
        hit.set_volume(0)
        coinsound.set_volume(0)
        rewind.set_volume(0)
        speedup.set_volume(0)
        retrysound.set_volume(0)
# ASSIGN
    clock = pygame.time.Clock()
    keepGoing = True

    # Hide the mouse pointer
    pygame.mouse.set_visible(False)

    # LOOP
    while keepGoing:

        # TIME
        clock.tick(30)

        # EVENT HANDLING: Player uses space to contol the bullet

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and flag:
                    retrysound.play(0)
                    main(sound)
                elif event.key==pygame.K_ESCAPE and flag:
                    menu()
                elif event.key == pygame.K_SPACE:
                    player1.change_direction((0, 1))
                    bulletglow.change_direction((0, 1))

            elif event.type==pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player1.change_direction((0, -0.5))
                    bulletglow.change_direction((0, -0.5))

        # Collision checking
        #Checking if the player has lost
        if score.lose(endzone,targets,player1,barriers,bulletglow) and flag8:
            pygame.mixer.music.load("retrybg.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.4)
            #checking if the user set the music off
            if sound==True:
                pygame.mixer.music.set_volume(0)
            explode.play(0)
            player1.death()
            counter=87
            bg.set_type()
            allSprites = pygame.sprite.Group(bg,endzone,targets,coins,player1,powerups,barriers,score,scoreSprite,coinscore,coinScoreKeep,overlay,gameover,endscore,endcoinscore,totalScore,retrytext)
            flag=True
            flag8=False
        #Checking if the the player got 10 points, it then speeds up the game slightly
        if score.get_score():
            flag4=True
            if flag4:
                speedup.play(0)
                speed+=1
            flag4=False
        counter+=1
        #These are the spawn rates for the coins and powerups
        rand=random.randint(1,15)
        rand2=random.randint(1,25)
        #Checking if the player has collided with any of the targets, If so sound plays and score is given.
        if pygame.sprite.spritecollide(player1,targets,True):
            hit.play(0)
            score.targetHit(1)
            endscore.targetHit(1)
            totalScore.targetHit(1)
        #Checking if the player has collided with any of the coins, If so sound plays and score is given.
        if pygame.sprite.spritecollide(player1,coins,True):
            coinsound.play(0)
            coinScoreKeep.targetHit(1)
            endcoinscore.targetHit(1)
            totalScore.targetHit(2)
        #Checking if the player has collided with any of the powerups, If so, it slows down time and starts the timer.
        if pygame.sprite.spritecollide(player1,powerups,True):
            rewind.play(0)
            powerupglow.change_sprite()
            timer=0
            timerstart=True

        #If the timer has started, it ticks until it is above 250 ticks, then it ends.
        #During the timer, it slows down the speeds of the targets, coins and powerups
        if timerstart:
            timer+=1
            if timer<=250:
                bg.bgset_speed(1)
                target.set_speed(1)
                coin.set_speed(1)
                powerup.set_speed(1)
                powerupglow.set_speed(1)
                rate=130
            elif timer>250:
                timerstart=False
                flag2=True
        #Once the timer is done, it returns the speed to its original value
        elif timerstart==False and flag2:
            bg.bgset_speed(2)
            target.set_speed(2)
            coin.set_speed(2)
            powerup.set_speed(2)
            powerupglow.set_speed(2)
            rate=35
            counter=0
            flag2=False

        #This is a value so that the powerup and its glow spawn together
        value=random.randrange(100, screen.get_height()-152-100)
        #This is checking the to see if any coins or powerups need to be spawned in
        #If so, it will spawn them in
        if counter==rate:
            if rand==1:
                coin=dungeonShotSprites.Targets(screen,2,speed,value)
                coins=pygame.sprite.Group(coin)
                target=dungeonShotSprites.Targets(screen,1,speed,value)
                targets=pygame.sprite.Group(target)
                allSprites = pygame.sprite.Group(bg,endzone,coins,targets,bulletglow,player1,barriers,score,scoreSprite,coinscore,coinScoreKeep)
            elif rand2==1:
                powerup=dungeonShotSprites.Targets(screen,3,speed,value)
                powerups=pygame.sprite.Group(powerup)
                powerupglow=dungeonShotSprites.Targets(screen,4,speed,value)
                powerupglows=pygame.sprite.Group(target)
                target=dungeonShotSprites.Targets(screen,1,speed,value)
                targets=pygame.sprite.Group(target)
                allSprites = pygame.sprite.Group(bg,endzone,coins,targets,bulletglow,player1,powerupglow,powerups,barriers,score,scoreSprite,coinscore,coinScoreKeep)
            #If no coins or powerups need to spawn in, it contninues on regurlarly
            else:
                target=dungeonShotSprites.Targets(screen,1,speed,value)
                targets=pygame.sprite.Group(target)
                allSprites = pygame.sprite.Group(bg,endzone,targets,bulletglow,player1,barriers,score,scoreSprite,coinscore,coinScoreKeep)
            counter=0

        # REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()

    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)


def menu():
    '''This function defines the menu for our pyPong game.'''

    # DISPLAY
    pygame.display.set_caption("Dungeon Shot - Abdulrehman Nakhuda")
    programIcon = pygame.image.load("bullet6.png")

    pygame.display.set_icon(programIcon)

    # ENTITIES
    background = pygame.image.load("backgroundpink.jpg")
    background = background.convert()
    screen.blit(background, (0, 0))

    # Sprites for: ScoreKeeper label, End Zones, Bullet, and other Sprites
    endzone=dungeonShotSprites.EndZone(screen)
    topb=dungeonShotSprites.Bg(2,screen)
    bottomb=dungeonShotSprites.Bg(3,screen)
    topbg=dungeonShotSprites.Bg(4,screen)
    bottombg=dungeonShotSprites.Bg(5,screen)
    barriers=pygame.sprite.Group(topb,bottomb)
    player1 = dungeonShotSprites.Player(screen, 1)
    bulletglow=dungeonShotSprites.Player(screen,2)
    spacebar=dungeonShotSprites.Bg(6,screen)
    flag=False
    flag2=False
    flag3=False
    counter=0
    allSprites = pygame.sprite.Group(endzone,barriers,bulletglow,player1,bottombg,topbg,spacebar)

    #Music entities
    pygame.mixer.music.load("gamemusic.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    move=pygame.mixer.Sound("openDoor.mp3")

# ASSIGN
    clock = pygame.time.Clock()
    keepGoing = True

    # Hide the mouse pointer
    pygame.mouse.set_visible(False)

    # LOOP
    while keepGoing:

        # TIME
        clock.tick(30)

        # EVENT HANDLING: Player 1 uses joystick, Player 2 uses arrow keys

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and flag2:#Checking if its okay to go to start the game, if so, do it.
                        main(flag3)
                elif event.key==pygame.K_SPACE:#Pressing space will move the walls out of the way
                    move.play(0)
                    flag=True
                    flag2=True
                elif event.key==pygame.K_m and not flag3:#Pressing the 'm' key will toggle between muting the sounds
                    pygame.mixer.music.set_volume(0)
                    move.set_volume(0)
                    flag3=True
                elif event.key==pygame.K_m and flag3:#This one will turn the sound back on.
                    pygame.mixer.music.set_volume(0.5)
                    move.set_volume(1)
                    flag3=False

        #Having a condition to move the walls when needed.
        if pygame.sprite.collide_rect(spacebar,bottombg) and flag2:
            spacebar.dismiss()
        # REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        #Moving the walls if the conditions are met.
        if flag==True:
            topbg.move(2)
            bottombg.move(1)
        allSprites.draw(screen)
        pygame.display.flip()

    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)

menu()
