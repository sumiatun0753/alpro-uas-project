import pygame, sys, random, time
from pygame.locals import *

pygame.init()

#-lebar layar
displayWidth = 1080
displayHeight = 680

#-warna
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
tosca = (51,153,102)
blue = (0,0,255)
orange = (255,150,0)
bright_orange = (200,125,0)
bright_red = (200, 0, 0)
bright_blue = (0, 0, 200)

#-gambar
mainImg = pygame.image.load('Slime.png')
main1Img = pygame.image.load('Slime kanan.png')
main2Img = pygame.image.load('Slime kiri.png')
soapImg = pygame.image.load('sponge.png')
soapImg1 = pygame.image.load('SABUN COLEK.png')
foodImg = pygame.image.load('bakteri.png')
tileImg = pygame.image.load('BESI TUA.jpg')
start = pygame.image.load('bakteri2.png')
finish = pygame.image.load('bakteri3.png')
upArrow = pygame.image.load('panah atas.png')
downArrow = pygame.image.load('panah bawah.png')
leftArrow = pygame.image.load('panah kiri.png')
rightArrow = pygame.image.load('panah kanan.png')
bintang = pygame.image.load('bintang skor.png')
bintang1 = pygame.image.load('BINTANG1.png')
bintang2 = pygame.image.load('BINTANG2.png')
bintang3 = pygame.image.load('BINTANG3.png')

#-tampilan layar
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Junk Maze')
pygame.display.set_icon(mainImg)
clock = pygame.time.Clock()

pause = False

#-preview stage
level = ["XXXXXXXXXXXXXXXXXXXXXXXXXXX",
         "X X X         X       X   F",
         "X     X XXXXXXXXXXXXX X XXX",
         "X XXXXX X             X   X",
         "X     X X XXXXXXXXXXX XXX X",
         "XXXXX X X             X   X",
         "X     X   X X X XXXXX XXX X",
         "X X X   X X X X         X X",
         "X X X XXX X X X XXXXXXX   X",
         "X X X     X X X       XXX X",
         "X X X XXXXX XXX XXXX XX   X",
         "X   X X      X       X  XXX",
         "X XXX XXXXXXXX XX XXXX XXXX",
         "X   X   X   X        X    X", 
         "XXX XXX X X X XXXXXX XXXX X",
         "S   X     X        X      X",
         "XXXXXXXXXXXXXXXXXXXXXXXXXXX"]

#-function membuat dan hyperlink button play, how to play, quit, pause, continue, back to menu, dan play again?
def button(msg,x,y,width,height,color1,color2,action = None):
    global pause
    mouse = pygame.mouse.get_pos() #koordinat mouse
    click = pygame.mouse.get_pressed() #posisi klik atau tidak

    #-kondisi ketika mouse mengklik salah satu button
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, color1, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "play":
                gameLoop()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "unpause":
                unpause()
            elif action == "playAgain":
                gameLoop()
            elif action == "hint":
                pause = True
                gameHint()
            elif action == "menu":
                unpause()
            elif action == "home":
                pause=True
                gameMenu()
            elif action == "pause":
                pause = True
                gamePause()
    else:
        pygame.draw.rect(gameDisplay, color2, (x, y, width, height)) #ketika mouse berada di kotak button warna akan berubah

    #kondisi text dalam function button
    smallText = pygame.font.Font('Pokemon Solid.ttf', 20)
    textSurf, textRect = text(msg, smallText, black)
    textRect.center = ((x+(width/2)), (y+(height/2)))
    gameDisplay.blit(textSurf, textRect)

#-function mengatur warna tulisan    
def text(msg, font, color):
    textSurface = font.render(msg, True, color)
    return textSurface, textSurface.get_rect()

#-function unpause
def unpause():
    global pause
    pause = False

#-function game menu/tampilan awal game    
def gameMenu():
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        gameDisplay.fill(tosca)
        theText = pygame.font.Font('Minecrafter_3.ttf', 150)
        textSurf, textRect = text("JUNK", theText, black)
        textSurf2, textRect2 = text("MAZE", theText, black)
        textRect.center = ((290),(290))
        textRect2.center = ((340),(510))
        gameDisplay.blit(textSurf, textRect)
        gameDisplay.blit(textSurf2, textRect2)

        button("Play",810,150,150,75,bright_red,red,"play")
        button("How to play",810,320,150,75,bright_orange,orange,"hint")
        button("Quit",810,490,150,75,bright_blue,blue,"quit")
        
        
        pygame.display.update()
        clock.tick(15)

#-function untuk membuat keterangan pada how to play 
def hint(img,imgx,imgy,msg,textx,texty):
    gameDisplay.blit(img,(imgx,imgy))
    theText = pygame.font.Font('SF Slapstick Comic Shaded.ttf', 20)
    textSurf, textRect = text(msg, theText, black)  
    textRect.center = ((textx),(texty))
    gameDisplay.blit(textSurf, textRect)

#-function tampilan menu how to play       
def gameHint():
    
    while pause:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(tosca)
        theText = pygame.font.Font('blocked.ttf', 50)
        textSurf, textRect = text("Game Control", theText, black)
        textRect.center = ((displayWidth/2),(displayHeight-600))
        gameDisplay.blit(textSurf, textRect)
        
        hint(upArrow,(displayWidth-750),(displayHeight-520),"Up Arrow to Move Up",(displayWidth-530),(displayHeight-490))
        hint(leftArrow,(displayWidth-750),(displayHeight-440),"Left Arrow to Move Left",(displayWidth-510),(displayHeight-410))
        hint(rightArrow,(displayWidth-750),(displayHeight-360),"Right Arrow to Move Right",(displayWidth-500),(displayHeight-330))
        hint(leftArrow,(displayWidth-750),(displayHeight-280),"Down Arrow to Move Down",(displayWidth-505),(displayHeight-250))
        
        button("Back to menu",150,530,180,60,bright_orange,orange,"menu")

        pygame.display.update()
        clock.tick(15)
        
#-function ketika game win        
def gameWon():
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        gameDisplay.fill(tosca)
        theText = pygame.font.Font('blocked.ttf', 50)
        textSurf, textRect = text("Congratulation !", theText, black)
        textSurf1, textRect2 = text("You Got :", theText, black)
        textRect.center = ((displayWidth/2),(displayHeight/3-100))
        textRect2.center = ((displayWidth/2),(displayHeight/2-100))
        gameDisplay.blit(textSurf, textRect)
        gameDisplay.blit(textSurf1, textRect2)

        #-kondisi untuk menampilkan bintang
        if count<1000:
            gameDisplay.blit(bintang,(displayWidth/2-100,displayHeight/2-50))
        elif count>999 and count<2000:
            gameDisplay.blit(bintang1,(displayWidth/2-100,displayHeight/2-60))
        elif count>1999 and count<3000:
            gameDisplay.blit(bintang2,(displayWidth/2-100,displayHeight/2-60))
        elif count==3000:
            gameDisplay.blit(bintang2,(displayWidth/2-100,displayHeight/2-60))

        score(count,"", displayWidth/2-12, displayHeight/2+50, 20)
        
        button("Play Again?",150,530,180,60,bright_red,red,"playAgain")
        button("Back to menu",750,530,180,60,bright_blue,blue,"home")
        
        pygame.display.update()
        clock.tick(15)

#-function ketika game over
def gameOver():

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
              
        gameDisplay.fill(tosca)
        theText = pygame.font.Font('blocked.ttf', 100)
        textSurf, textRect = text("Game Over", theText, black)  
        textRect.center = ((displayWidth/2),(displayHeight/2))
        gameDisplay.blit(textSurf, textRect)

        button("Play Again?",150,530,180,60,bright_red,red,"playAgain")
        button("Back to menu",750,530,180,60,bright_blue,blue,"home")
        
        pygame.display.update()
        clock.tick(15)
        
#-function ketika game pause   
def gamePause():
    
    while pause:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        gameDisplay.fill(tosca)
        theText = pygame.font.Font('blocked.ttf', 75)
        textSurf, textRect = text("Game Paused", theText, black)  
        textRect.center = ((displayWidth/2),(displayHeight/2))
        gameDisplay.blit(textSurf, textRect)

        button("Continue",150,530,180,60,bright_red,red,"unpause")
        button("Back to menu",750,530,180,60,bright_blue,blue,"home")
        
        pygame.display.update()
        clock.tick(15)

#-function score
def score(count,msg,x,y,size):
    font = pygame.font.Font('Minecrafter_3.ttf', size)
    textSurf, textRect = text(str(msg) + str(count), font, white)
    textRect.center = ((x),(y))
    gameDisplay.blit(textSurf, textRect)

#-function menampilkan bonus/makanan karakter utama   
def bonus(x,y):
    gameDisplay.blit(foodImg,(x,y))

#-function menampilkan sabun1
def enemy(x,y):
    gameDisplay.blit(soapImg,(x,y))

#-function menampilkan sabun2
def enemy1(x,y):
    gameDisplay.blit(soapImg1,(x,y))

#-function menampilkan tembok   
def stage(level):
    row = len(level)
    column = len(level[0])

    length = 40
    height = 40
    
    point={}#dict untuk menampung koordinat jalan, sekaligus pembatas tembok

    gameDisplay.fill(white)
    for j in range(row):
        for i in range(column):
            if level[j][i] == "X":
                gameDisplay.blit(tileImg, ( length * i, height * j))
            else:
                if level[j][i] == "S":
                    gameDisplay.blit(start, ( length * i, height * j))
                if level[j][i] == "F":
                    gameDisplay.blit(finish, ( length * i, height * j))
                point[j,i]=(length*i,height*j)
        
    return point

#-function menampilkan text ketika ditabrak oleh musuh
def text_display(msg):
    theText = pygame.font.Font('SF Slapstick Comic Shaded.ttf', 115)
    textSurf, textRect = text(msg, theText, red)
    textRect.center = ((displayWidth/2),(displayHeight/2))
    
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    
    time.sleep(1)
    gameOver()
    
#function skenario, dan aturan game              
def gameLoop():
    global count, pause
    gameExit = False

    #-ukuran, dan koordinat karakter utama
    mainImg=pygame.image.load('Slime.png')
    mainWidth,mainHeight=40,40
    mainx, mainy= 0,600

    #-koordinat sabun1, kecepatan
    enemy_startx = random.randrange(0, displayWidth)
    enemy_starty = -600
    
    enemy_speed = 5

    #-koordinat sabun2, kecepatan
    enemy_startx1 = -600
    enemy_starty1 = random.randrange(0, displayHeight)
    
    enemy_speed1 = 5

    #-ukuran musuh
    enemyWidth = 58
    enemyHeight = 58
    
    #-koordinat bonus/makanan karakter utama
    food_startx,  food_starty =  40, 40
    food_startx1, food_starty1 = 80, 240
    food_startx2, food_starty2 = 40, 520
    food_startx3, food_starty3 = 280, 280
    food_startx4, food_starty4 = 360, 360
    food_startx5, food_starty5 = 280, 440
    food_startx7, food_starty7 = 200, 600
    food_startx8, food_starty8 = 200, 200
    food_startx11,food_starty11= 200, 80
    food_startx9, food_starty9 = 520, 120
    food_startx12,food_starty12= 440, 520
    food_startx13,food_starty13= 440, 200
    food_startx14,food_starty14= 440, 320
    food_startx16,food_starty16= 440, 40
    food_startx17,food_starty17= 480, 440
    food_startx10,food_starty10= 520, 360
    food_startx6, food_starty6 = 560, 200
    food_startx24,food_starty24= 680, 280
    food_startx25,food_starty25= 600, 400
    food_startx26,food_starty26= 600, 40
    food_startx27,food_starty27= 600, 600
    food_startx18,food_starty18= 800, 360
    food_startx20,food_starty20= 720, 440
    food_startx22,food_starty22= 800, 520
    food_startx23,food_starty23= 800, 200
    food_startx21,food_starty21= 840, 80
    food_startx19,food_starty19= 840, 160
    food_startx28,food_starty28= 1000, 600
    food_startx29,food_starty29= 1000, 160
    food_startx15,food_starty15= 1000, 400

    #-ukuran makanan karakter utama
    foodWidth=40
    foodHeight=40

    #-variabel penampung score
    count = 0

    while not gameExit:
        point=stage(level)#-menampung nilai dari function stage(level)

        #-memasukkan key untuk permain
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_UP:
                    mainImg=pygame.image.load('Slime.png')
                    if (mainx,mainy-mainHeight) in point.values():
                        mainy -= 40
                if event.key == K_DOWN:
                    mainImg=pygame.image.load('Slime.png')
                    if (mainx,mainy+mainHeight) in point.values():
                        mainy += 40
                if event.key == K_RIGHT:
                    mainImg=pygame.image.load('Slime kanan.png')
                    if (mainx+mainWidth,mainy) in point.values():
                        mainx += 40
                if event.key == K_LEFT:
                    mainImg=pygame.image.load('Slime kiri.png')
                    if (mainx-mainWidth,mainy) in point.values():
                        mainx -= 40
                        
        #-menampilkan mainImg
        gameDisplay.blit(mainImg, (mainx,mainy))

        #-enemy sabun1    
        enemy(enemy_startx, enemy_starty)
        enemy_starty += enemy_speed
        
        if enemy_starty > displayHeight:
            enemy_starty = 0 - enemyHeight
            enemy_startx = random.randrange(0, displayWidth)
            enemy_speed += 0.3
            
        #-kondisi ketika sabun1 menabrak karakter utama
        if mainy > enemy_starty and mainy < enemy_starty + enemyHeight:
            if mainx > enemy_startx and mainx < enemy_startx + enemyWidth or mainx + mainWidth > enemy_startx and mainx + mainWidth < enemy_startx + enemyWidth:
                text_display("Aww!")

        #-enemy sabun2
        enemy1(enemy_startx1,enemy_starty1)
        enemy_startx1 +=enemy_speed
        
        if enemy_startx1>displayWidth:
            enemy_startx1=0-enemyWidth
            enemy_starty1=random.randrange(0,displayHeight)
            enemy_speed += 0.3

        #-kondisi ketika sabun2 menabrak karakter utama  
        if mainy > enemy_starty1 and mainy < enemy_starty1 + enemyHeight:
            if mainx > enemy_startx1 and mainx < enemy_startx1 + enemyWidth or mainx + mainWidth > enemy_startx1 and mainx + mainWidth < enemy_startx1 + enemyWidth:
                text_display("Aww!")

        #-menampilkan, dan kondisi ketika menabrak bonus       
        bonus(food_startx,food_starty)
        if mainx == food_startx and mainy == food_starty and mainWidth == foodWidth and mainHeight == foodHeight:
            #menambah score 100 ketika menabrak bonus/makanan
            count += 100
            #menghilangkan bonus/makanan ketika ditabrak
            food_startx = -800
            food_starty = -600
        bonus(food_startx1,food_starty1)
        if mainx == food_startx1 and mainy == food_starty1 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx1 = -800
            food_starty1 = -600
        bonus(food_startx2,food_starty2)
        if mainx == food_startx2 and mainy == food_starty2 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx2 = -800
            food_starty2 = -600
        bonus(food_startx3,food_starty3)
        if mainx == food_startx3 and mainy == food_starty3 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx3 = -800
            food_starty3 = -800
        bonus(food_startx4,food_starty4)
        if mainx == food_startx4 and mainy == food_starty4 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx4 = -800
            food_starty4 = -600
        bonus(food_startx5,food_starty5)
        if mainx == food_startx5 and mainy == food_starty5 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx5 = -800
            food_starty5 = -600
        bonus(food_startx6,food_starty6)
        if mainx == food_startx6 and mainy == food_starty6 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx6 = -800
            food_starty6 = -600
        bonus(food_startx7,food_starty7)
        if mainx == food_startx7 and mainy == food_starty7 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx7 = -800
            food_starty7 = -600
        bonus(food_startx8,food_starty8)
        if mainx == food_startx8 and mainy == food_starty8 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx8 = -800
            food_starty8 = -800
        bonus(food_startx9,food_starty9)
        if mainx == food_startx9 and mainy == food_starty9 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx9 = -800
            food_starty9 = -600
        bonus(food_startx10,food_starty10)
        if mainx == food_startx10 and mainy == food_starty10 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx10 = -800
            food_starty10 = -600
        bonus(food_startx11,food_starty11)
        if mainx == food_startx11 and mainy == food_starty11 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx11 = -800
            food_starty11= -600
        bonus(food_startx12,food_starty12)
        if mainx == food_startx12 and mainy == food_starty12 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx12 = -800
            food_starty12 = -600
        bonus(food_startx13,food_starty13)
        if mainx == food_startx13 and mainy == food_starty13 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx13 = -800
            food_starty13 = -800
        bonus(food_startx14,food_starty14)
        if mainx == food_startx14 and mainy == food_starty14 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx14 = -800
            food_starty14 = -600
        bonus(food_startx15,food_starty15)
        if mainx == food_startx15 and mainy == food_starty15 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx15 = -800
            food_starty15 = -600
        bonus(food_startx16,food_starty16)
        if mainx == food_startx16 and mainy == food_starty16 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx16 = -800
            food_starty16 = -600
        bonus(food_startx17,food_starty17)
        if mainx == food_startx17 and mainy == food_starty17 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx17 = -800
            food_starty17 = -600
        bonus(food_startx18,food_starty18)
        if mainx == food_startx18 and mainy == food_starty18 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx18 = -800
            food_starty18 = -800
        bonus(food_startx19,food_starty19)
        if mainx == food_startx19 and mainy == food_starty19 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx19 = -800
            food_starty19 = -600
        bonus(food_startx20,food_starty20)
        if mainx == food_startx20 and mainy == food_starty20 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx20 = -800
            food_starty20 = -600
        bonus(food_startx21,food_starty21)
        if mainx == food_startx21 and mainy == food_starty21 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx21 = -800
            food_starty21 = -600
        bonus(food_startx22,food_starty22)
        if mainx == food_startx22 and mainy == food_starty22 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx22 = -800
            food_starty22 = -600
        bonus(food_startx23,food_starty23)
        if mainx == food_startx23 and mainy == food_starty23 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx23 = -800
            food_starty23 = -800
        bonus(food_startx24,food_starty24)
        if mainx == food_startx24 and mainy == food_starty24 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx24 = -800
            food_starty24 = -600
        bonus(food_startx25,food_starty25)
        if mainx == food_startx25 and mainy == food_starty25 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx25 = -800
            food_starty25 = -600
        bonus(food_startx26,food_starty26)
        if mainx == food_startx26 and mainy == food_starty26 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx26 = -800
            food_starty26 = -600
        bonus(food_startx27,food_starty27)
        if mainx == food_startx27 and mainy == food_starty27 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx27 = -800
            food_starty27 = -600
        bonus(food_startx28,food_starty28)
        if mainx == food_startx28 and mainy == food_starty28 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx28 = -800
            food_starty28 = -800
        bonus(food_startx29,food_starty29)
        if mainx == food_startx29 and mainy == food_starty29 and mainWidth == foodWidth and mainHeight == foodHeight:
            count += 100
            food_startx29 = -800
            food_starty29 = -600

        #-memanggil function score sekaligus penghitung score pada saat permainan berlangsung
        score(count,"Score: ", 100, 20, 20)

        #-button pause
        button("Pause",980,0,100,30,bright_orange,orange,"pause")

        #-kondisi mencapai finish
        main_row = int(mainy / mainWidth)
        main_column = int(mainx / mainWidth)
        if level[main_row][main_column] == "F":
            gameWon()
            
        pygame.display.update()
        clock.tick(60)

        
gameMenu()
pygame.quit()
quit()
