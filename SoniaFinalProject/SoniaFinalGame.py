
# Sonia Tinaz
# Jan. 20, 2019 
# Frog run
# Detecting collisions with rect objects, controlling frog with user input, reading and writing to files  

import pygame
import sys
import pygame_textinput
import time
import random
pygame.init()

clock = pygame.time.Clock()
FPS = 70

screenWidth = 800
screenHeight = 640

sreenSize = (screenWidth,screenHeight)
screen = pygame.display.set_mode(sreenSize)
pygame.display.set_caption("Frog Run")


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
DARKGREEN = (24,160,24)
LIGHTGREEN = (99, 255, 115)
TURQUOISE = (33, 169, 158)

screen.fill(WHITE)
pygame.display.update()

# Declaring variables used later on in the program

go = True
titleScreen = True
introBackground = True
rulesBackground = True
nextLevelBackground = True
animation = True
enterUsername = True
levelOne = True
endScreen = False
switch = True
startGame = False 
collisionCheckLilypad1 = False
collisionCheckLilypad2 = False
collisionCheckLilypad3 = False
collisionCheckLilypad4 = False
totalTime = 240
levelTwo = False
numberOfCoins = 6
levelOneArrays = True
nextLevelScreen = False
timeRemaining = 1
score = 0
grassHeight = 60
jumpLength = int((screenHeight/10))
lives = 4
lilypadCollisionCount = 0
orderHighScores = True
dx = 0
speed = 4

#Function for creating and displaying image
#Takes an image, scales it to the specified width and height, then blits it to the screen at chosen x and y position 
def getImage(imageName,width,height,x,y):
    image = pygame.image.load(imageName).convert_alpha()
    image  = pygame.transform.scale(image, (width,height))
    newImage = image.get_rect()
    newImage.x = x
    newImage.y = y
    screen.blit(image, newImage)


#Function for creating and displaying a button
def button(buttonX, buttonY, buttonWidth, buttonHeight, inactive_colour, active_colour, text, textSize, textFont,textColour):
    mouseX,mouseY = pygame.mouse.get_pos()
    leftClick,scroll,rightClick = pygame.mouse.get_pressed()
              
    fontTitle = pygame.font.SysFont (textFont,textSize)
    textTitle = fontTitle.render (text, True,textColour)

    # If the mouse is hovered over the button, the button, with user's specified x, y, width and height is drawn with its 'active' colour
    # Else, the button is drawn with its 'inactive' colour 
    if (mouseX >= buttonX and mouseX <= buttonX + buttonWidth and mouseY >= buttonY and mouseY <= buttonY + buttonHeight):
        pygame.draw.rect(screen, active_colour,(buttonX,buttonY,buttonWidth,buttonHeight),0)
    else:
        pygame.draw.rect(screen, inactive_colour,(buttonX,buttonY,buttonWidth,buttonHeight),0)

    # Text that has the user's specified font, colour, and size is blitted inside the button
    screen.blit(textTitle, (buttonX + buttonWidth/2 - textTitle.get_width()/2,buttonY + buttonHeight/2- textTitle.get_height()/2))


    # If the user clicks the button with scroll, right click, or left click, 'True' is returned
    if leftClick == True:
        if (mouseX >= buttonX and mouseX <= buttonX + buttonWidth and mouseY >= buttonY and mouseY <= buttonY + buttonHeight):
            button = True
            return button

    elif scroll == True:
        if (mouseX >= buttonX and mouseX <= buttonX + buttonWidth and mouseY >= buttonY and mouseY <= buttonY + buttonHeight):
            button = True
            return button
  
    elif rightClick == True:
        if (mouseX >= buttonX and mouseX <= buttonX + buttonWidth and mouseY >= buttonY and mouseY <= buttonY + buttonHeight):
            button = True
            return button

    pygame.display.update()


# Code for frog leaping between lilypads animation
while animation == True:
    #Makes the background dark green 
    screen.fill(DARKGREEN)
    fontTitleFrogRun = pygame.font.SysFont("forte",110)
    textTitleFrogRun = fontTitleFrogRun.render("Frog Run", True,(99, 255, 115))
    # Displays light green 'Frog Run' title in forte font, horizontally in the middle of the screen, and at a y position equal to the title's height divided by 2
    screen.blit(textTitleFrogRun, (screenWidth/2 - textTitleFrogRun.get_width()/2,textTitleFrogRun.get_height()/2))


    # If it has been approximately 2 seconds since the application was opened, screen is 'erased' by making it dark green/filling it
    # The 'Frog Run' title is displayed again
    # An image of a lilypad is displayed on each side of the screen, by calling the 'getImage' function
    # The first image in the frog animation image sequence is displayed with the 'getImage' function

    #Process is repeated for the other images in the sequence, the images displaying approximentely 1 second a part
    # i.e. the next image displays if it has been approximately 3 seconds sine the application was opened, before clearing the screen, displaying the title and lilypads
    if int(time.perf_counter()) == 2:
        screen.fill(DARKGREEN)
        screen.blit(textTitleFrogRun, (screenWidth/2 - textTitleFrogRun.get_width()/2,textTitleFrogRun.get_height()/2))
        getImage("lilypad.png",200,100,90,screenHeight-100)
        getImage("flippedLilypad.png",200,100,screenWidth - 290,screenHeight-100)
        getImage("frogAnimation1.png",100,100,140,screenHeight-150)
    elif int(time.perf_counter()) == 3:
        screen.fill(DARKGREEN)
        screen.blit(textTitleFrogRun, (screenWidth/2 - textTitleFrogRun.get_width()/2,textTitleFrogRun.get_height()/2))
        getImage("lilypad.png",200,100,90,screenHeight-100)
        getImage("flippedLilypad.png",200,100,screenWidth - 290,screenHeight-100)
        getImage("frogAnimation2.png",100,100,220,screenHeight-180)
    elif int(time.perf_counter()) == 4:
        screen.fill(DARKGREEN)
        screen.blit(textTitleFrogRun, (screenWidth/2 - textTitleFrogRun.get_width()/2,textTitleFrogRun.get_height()/2))
        getImage("lilypad.png",200,100,90,screenHeight-100)
        getImage("flippedLilypad.png",200,100,screenWidth - 290,screenHeight-100)
        getImage("frogAnimation3.png",100,100,300,screenHeight-210)
    elif int(time.perf_counter()) == 5:
        screen.fill(DARKGREEN)
        screen.blit(textTitleFrogRun, (screenWidth/2 - textTitleFrogRun.get_width()/2,textTitleFrogRun.get_height()/2))
        getImage("lilypad.png",200,100,90,screenHeight-100)
        getImage("flippedLilypad.png",200,100,screenWidth - 290,screenHeight-100)
        getImage("frogAnimation4.png",100,100,380,screenHeight-210)
    elif int(time.perf_counter()) == 6:
        screen.fill(DARKGREEN)
        screen.blit(textTitleFrogRun, (screenWidth/2 - textTitleFrogRun.get_width()/2,textTitleFrogRun.get_height()/2))
        getImage("lilypad.png",200,100,90,screenHeight-100)
        getImage("flippedLilypad.png",200,100,screenWidth - 290,screenHeight-100)
        getImage("frogAnimation5.png",100,100,460,screenHeight-180)
    elif int(time.perf_counter()) == 7:
        screen.fill(DARKGREEN)
        screen.blit(textTitleFrogRun, (screenWidth/2 - textTitleFrogRun.get_width()/2,textTitleFrogRun.get_height()/2))
        getImage("lilypad.png",200,100,90,screenHeight-100)
        getImage("flippedLilypad.png",200,100,screenWidth - 290,screenHeight-100)
        getImage("frogAnimation6.png",100,100,540,screenHeight-150)
    elif int(time.perf_counter()) == 8:
        screen.fill(DARKGREEN)
        screen.blit(textTitleFrogRun, (screenWidth/2 - textTitleFrogRun.get_width()/2,textTitleFrogRun.get_height()/2))
        getImage("lilypad.png",200,100,90,screenHeight-100)
        getImage("flippedLilypad.png",200,100,screenWidth - 290,screenHeight-100)
        getImage("frogAnimation5.png",100,100,460,screenHeight-180)
    elif int(time.perf_counter()) == 9:
        screen.fill(DARKGREEN)
        screen.blit(textTitleFrogRun, (screenWidth/2 - textTitleFrogRun.get_width()/2,textTitleFrogRun.get_height()/2))
        getImage("lilypad.png",200,100,90,screenHeight-100)
        getImage("flippedLilypad.png",200,100,screenWidth - 290,screenHeight-100)
        getImage("frogAnimation4.png",100,100,380,screenHeight-210)
    elif int(time.perf_counter()) == 10:
        screen.fill(DARKGREEN)
        screen.blit(textTitleFrogRun, (screenWidth/2 - textTitleFrogRun.get_width()/2,textTitleFrogRun.get_height()/2))
        getImage("lilypad.png",200,100,90,screenHeight-100)
        getImage("flippedLilypad.png",200,100,screenWidth - 290,screenHeight-100)
        getImage("frogAnimation3.png",100,100,300,screenHeight-210)
    elif int(time.perf_counter()) == 11:
        screen.fill(DARKGREEN)
        screen.blit(textTitleFrogRun, (screenWidth/2 - textTitleFrogRun.get_width()/2,textTitleFrogRun.get_height()/2))
        getImage("lilypad.png",200,100,90,screenHeight-100)
        getImage("flippedLilypad.png",200,100,screenWidth - 290,screenHeight-100)
        getImage("frogAnimation2.png",100,100,220,screenHeight-180)
    elif int(time.perf_counter()) == 12:
        screen.fill(DARKGREEN)
        screen.blit(textTitleFrogRun, (screenWidth/2 - textTitleFrogRun.get_width()/2,textTitleFrogRun.get_height()/2))
        getImage("lilypad.png",200,100,90,screenHeight-100)
        getImage("flippedLilypad.png",200,100,screenWidth - 290,screenHeight-100)
        getImage("frogAnimation1.png",100,100,140,screenHeight-150)
        animation = False   
    pygame.display.update()

#Main while loop for the game 
while go:

    #If levelOneArrays is true, rect objects for level one get stored into arrays
    if levelOneArrays == True:
        numOfRivers = 3
        numOfRoads = 2
        #Defining arrays for river, roads, cars, logs, turtles, and watersplashes rect objects
        rivers = []
        roads = []
        carsLeft = []
        carsRight = []
        logs = []
        turtles = []
        waterSplashes = []

        # Creates 3 rect objects for the rivers, stores them in the 'rivers' array by appending each rect object to 'rivers'
        # Each river's y position changes so that the rivers are situated between the roads
        # Each river is as wide as the screen, and its' height is a 5th of the screen height 
        for i in range (numOfRivers):
            # The last river is 60 units shorter (vertically), to make room for the grass strip that the frog starts on
            if i ==  2:  
                river = pygame.Rect(0,2 * i * screenHeight/5 ,screenWidth,screenHeight/5 - 60)
            else:
                river = pygame.Rect(0,2 * i * screenHeight/5 ,screenWidth,screenHeight/5)
            rivers.append(river)
        # Creates 2 rect objects for the roads, stores them in 'roads' array
        # Y poisition changes as it runs through the for loop so that the roads display between the rivers
        # Each road is as wide as the screen, and its' height is a 5th of the screen height 
        for i in range (numOfRoads):
            road = pygame.Rect(0, (i * 2 + 1) * screenHeight/5, screenWidth, screenHeight/5)
            roads.append(road)

        lilypads = []
        lilypadX = 60
        # Creates 4 rect objects for the lilypads, stores them in 'lilypads' array
        for i in range(4):
            # Lilypad's x increments by 50 (the width of one lilypad) + 70 units each time
            # Makes the lilypads appear spaced out by 70 units 
            lilypadX = lilypadX + + 50 + 70
            # Makes lilypads appear as an image of a lilypad
            lilypadImage = pygame.image.load("lilypadEndPoint.png").convert_alpha()
            lilypadImage= pygame.transform.scale(lilypadImage, (50,int(screenHeight/10)))
            # Getting the rect object of the image/lilypad  
            lilypad = lilypadImage.get_rect()
            lilypad.x = lilypadX
            # Each lilypad has a y position of 0 
            lilypad.y = 0
            #Appends each rect object to the array 
            lilypads.append(lilypad)
        # lilypadsCopy becomes a copy of the array of lilypad rect objects 
        lilypadsCopy = lilypads.copy()

        
    
        carX = screenWidth - 50
        # For loop creates rect objects for as many 50 unit wide cars that can fit on the screen (horizontally) with 80 unit gap between them, appends them to 'carsLeft' array
        # 'carsLeft' is an array of rect objects for cars going left on the last road
        for i in range (int(screenWidth/(50+80))):
            # Each car is spaced out by 80 units 
            carX = carX + 50 + 80
            # Each car appears as an image of a green car 
            greenCarImage = pygame.image.load("greenCar.png").convert_alpha()
            # Each car has a height of 1/10th of the screen height, and a width of 50
            greenCarImage= pygame.transform.scale(greenCarImage, (50,int(screenHeight/10)))
            car = greenCarImage.get_rect()
            car.x = carX
            # Each car in the array has a y position of the screen height divided by 5
            car.y = screenHeight/5
            carsLeft.append(car)
            
        # Same process is used as before to create an array of rect objects for cars going right on the last road
        # Only difference is that each car/rect object in the array has a y position of the screen height divided by 5 plus 50
        # As well, each rect object is appended to 'carsRight' array, and each car appears as a image of a red car
        carX2 = 0
        for i in range (int(screenWidth/(50+80))):
            carX2 = carX2 + 50 + 80
            redCarImage = pygame.image.load("redCar.png").convert_alpha()
            redCarImage  = pygame.transform.scale(redCarImage, (50,int(screenHeight/10)))
            car = redCarImage.get_rect()
            car.x = carX2
            car.y = screenHeight/5 + 50
            carsRight.append(car)

        # Creating and appending as many 50 unit wide rect objects that can fit on the screen horizontally with a 80 unit gap between them to 'carsLeft2'
        # Rect objects are for the cars going left on the first road 
        carsLeft2 = []
        carX = screenWidth - 50
        for i in range (int(screenWidth/(50+80))):
            # Each car is spaced out by 80 units 
            carX = carX + 50 + 80
            # Each car appears as a image of a green car  
            greenCarImage = pygame.image.load("greenCar.png").convert_alpha()
            greenCarImage= pygame.transform.scale(greenCarImage, (50,int(screenHeight/10)))
            car = greenCarImage.get_rect()
            car.x = carX
            # Cars all have a y value of the screen height divided by 5 times 4, minus the screen height divided by 10
            car.y = (screenHeight/5 * 4) - int(screenHeight/10) 
            carsLeft2.append(car)


        logX = screenWidth - 200
        #Creating and appending as many 90 unit wide rect objects that can fit on the screen horizontally with 150 unit gap inbetween to 'logs' array
        # These rect objects are for logs moving left 
        for i in range (int(screenWidth/(90+150))):
            # Each log is spaced out by 150 units
            logX = logX + 90 + 150
            # Each log appears as a image of a log
            logImage = pygame.image.load("log.png").convert_alpha()
            # Each log has a width of 90 units, and a height of 1/10th of the screen 
            logImage  = pygame.transform.scale(logImage, (90,int(screenHeight/10)))
            log = logImage.get_rect()
            log.x = logX
            # Each log has a y position of the screen height divided by 5, times 2
            log.y = screenHeight/5 * 2
            logs.append(log)


    
        # Appending rect objects to 'logs2'
        # rect objects are for logs moving right 
        logs2 = []
        logX = 0
        for i in range (int(screenWidth/(90+150))):
            logX = logX + 90 + 150
            logImage = pygame.image.load("log.png").convert_alpha()
            logImage  = pygame.transform.scale(logImage, (90,int(screenHeight/10)))
            log = logImage.get_rect()
            log.x = logX
            # Each log in the array has a y position of the screen height divided by 5, times 2
            log.y = screenHeight/5 * 4
            logs2.append(log)


        # Creating as many 50 unit wide rect objects that can fit on the screen horizontally, spaced out by 70 units
        # Appending each rect object to 'turtles' array
        # 'turtles' is an array of rect objects for turtles on the 2nd river
        turtleX = -60
        for i in range (int(screenWidth/(50 + 70))):
            # each turtle is spaced out by 70 units
            turtleX = turtleX + 50 + 70
            # each turtle appears as a turtle image 
            turtleImage = pygame.image.load("turtle.png").convert_alpha()
            # each turtle is 50 units wide, and has a height of 1/10th of the screen height 
            turtleImage  = pygame.transform.scale(turtleImage, (50,int(screenHeight/10)))
            turtle = turtleImage.get_rect()
            turtle.x = turtleX
            # each turtle has a y position of the screen height divided by 5, times 2, plus 60 (makes turtles appear on the second river)
            turtle.y = screenHeight/5 * 2 + 60
            turtles.append(turtle)

        # Creating and appending just as many rect objects as turtles on the second river to 'waterSplashes' array
        # each rect object appears as image of water splash
        # Water splashes have the same x and y positions and dimensions of the turtles on the second river
        waterSplashX = -60
        for i in range (int(screenWidth/(50 + 70))):
            waterSplashX = waterSplashX + 50 + 70
            waterSplashImage = pygame.image.load("waterSplash.gif").convert_alpha()
            waterSplashImage  = pygame.transform.scale(waterSplashImage, (50,int(screenHeight/10)))
            waterSplash = waterSplashImage.get_rect()
            waterSplash.x = waterSplashX
            waterSplash.y = screenHeight/5 * 2 + 60
            waterSplashes.append(waterSplash)
 
        turtles2 = []
        turtleX = -60
        # Creating 6 rect objects
        # Each rect object appears as image of turtle
        # rect objects are for turtles on the last river
        for i in range (int(screenWidth/(50 + 70))):
            # turtles are spaced out by 70 units 
            turtleX = turtleX + 50 + 70
            turtleImage = pygame.image.load("turtle.png").convert_alpha()
            turtleImage  = pygame.transform.scale(turtleImage, (50,int(screenHeight/10)))
            turtle = turtleImage.get_rect()
            turtle.x = turtleX
            # each turtle has a y position of the screen height divided by 5, minus 65 (turtles appear on the last river, below the lilypads)
            turtle.y = screenHeight/5 - 65
            # each rect object is appended to 'turtles2' array
            turtles2.append(turtle)

        waterSplashes2 = []
        waterSplashX = -60
        # Creating 6 rect objects
        # Each rect object appears as image of water splash 
        # rect objects are for water splashes on the last river
        for i in range (int(screenWidth/(50 + 70))):
            # water splashes are spaced out by 70 units 
            waterSplashX = waterSplashX + 50 + 70
            waterSplashImage = pygame.image.load("waterSplash.gif").convert_alpha()
            # each rect object has the same x and y position, and dimensions of the turtles on the last river 
            waterSplashImage  = pygame.transform.scale(waterSplashImage, (50,int(screenHeight/10)))
            waterSplash = waterSplashImage.get_rect()
            waterSplash.x = waterSplashX
            waterSplash.y = screenHeight/5 - 65
            # each rect object is appended to 'waterSplashes2' array
            waterSplashes2.append(waterSplash)

        
        # creating array of 6 rect objects that represent coins
        coins = []
        for i in range (6):
            # 'coin' becomes a rect object that is 10 units wide, 10 units tall
            # 'coin' given a random x and y coordinate that lets the coin appear on the screen
            coin = pygame.Rect(random.randint(0,screenWidth - 10),random.randint(int(screenHeight/10),screenHeight-10 ),10,10)
            # If the coin's y position is where the water splashes on the last river are drawn
            # the coin appears in the middle of the water splash by setting the coin's x value to a random water splash's x value that appears on the last river,
            # then centering it by adding half of the water splash's width, and minusing half of the coin's width 
            #The coin also becomes centered in the water splash by making the y coordinate equal to 1/5th of the screen height  minus half of the water splashe's height
            if coin.y >= screenHeight/5 - 65 and coin.y <= screenHeight/5:
                coin.x = waterSplashes2[random.randint(0,len(waterSplashes2) -1 )].x + (50/2) - 5
                coin.y = screenHeight/5 - ((screenHeight/10)/2)
            # If the coin's  y coordinate is where the water splashes on the 2nd river are drawn/displayed,
            # the coin's x and y coordinate gets redefined so it appears in the middle of the water splash
            if coin.y >= screenHeight/5 * 2 + 60 and coin.y <= screenHeight/5 * 3:
                coin.x = waterSplashes[random.randint(0,len(waterSplashes)- 1)].x + (50/2) - 5
                coin.y = (screenHeight/5 * 3) - ((screenHeight/10)/2)
            # If the coin's y coordinate is where the logs on the second river are drawn,
            # the coin's y coordinate gets redefinied so that the coin appears in the middle of the log (vertically)
            if coin.y >= (screenHeight/5 * 2) and coin.y <= (screenHeight/5*3) - (screenHeight/10):
                coin.y = screenHeight/5 * 2 + ((screenHeight/10)/2)
            # If the coin's y coordinate is where the logs on the first river are drawn,
            # the coin's y coordinate gets redefined so that the coin appears in the middle of the log (vertically)
            if coin.y >= (screenHeight/5 * 4) and coin.y <= (screenHeight/5*5) - 60:
                coin.y = screenHeight/5 * 4 + ((screenHeight/10)/2)
            # If the coin's y coordinate is where the cars on the first road are drawn,
            # the coin's y coordinate gets redefined so that the coin appears in the middle of the cars (vertically)
            if coin.y >= (screenHeight/5 * 4 - (screenHeight/10)) and coin.y <= screenHeight/5*4:
                coin.y = screenHeight/5 * 4 - ((screenHeight/10)/2)
            #If the coin's y coordinate is where the green cars on the second road are drawn,
            # the coin's y coordinate gets redefined so that the coin appears in the middle of the green cars (vertically)
            if coin.y >= screenHeight/5  and coin.y <= screenHeight/5 + (screenHeight/10):
                coin.y = screenHeight/5 + ((screenHeight/10)/2)
            # If the coin's y coordinate is where the red cars on the second road are drawn,
            # the coin's y coordinate gets redefined so that the coin appears in the middle of the red cars (vertically)
            if coin.y >= screenHeight/5 * 2 - (screenHeight/10)  and coin.y <= screenHeight/5 * 2:
                coin.y = screenHeight/5 * 2 - ((screenHeight/10)/2)
            # Each rect object is then appended to 'coins' so 'coins' becomes an array of 6 rect objects, representing coins
            coins.append(coin)


        # Creating rect object for the player
        # Player appears as image of frog 
        playerImage = pygame.image.load("frogPlayer.png").convert_alpha()
        # player is 50 units wide, and 45 units tall
        playerImage  = pygame.transform.scale(playerImage, (50,45))
        # Getting rect object from image 
        player = playerImage.get_rect()
        # Player spawns in the middle of the screen (horzontally), and where y = the screen height minus a tenth of the screen height, minus 10
        player.x = screenWidth/2 - 50/2
        player.y = screenHeight - (int(screenHeight/10) - 10)

        levelOneArrays = False

    # title screen displays if titleScreen equals True
    if titleScreen == True:
        # background becomes dark green colour
        # if statement prevents filling the screen multiple times (only makes the background dark green once)
        if introBackground == True:
            screen.fill(DARKGREEN)
            introBackground = False
        # 'Frog Run' title is displayed 
        screen.blit(textTitleFrogRun, (screenWidth/2 - textTitleFrogRun.get_width()/2,textTitleFrogRun.get_height()/2))

        buttonWidth = 200
        buttonHeight = 80
        # creating 'Rules' button that goes to rules when clicked, using 'button' function 
        rulesButton = button(screenWidth/2 - buttonWidth/2 ,textTitleFrogRun.get_height() + 80,buttonWidth,buttonHeight,(54, 247, 173),(57, 219, 203),'Rules',50, 'broadway',(18, 141, 145))
        # creating 'Start' button that goes to screen where user can enter an username, when clicked 
        startButton = button(screenWidth/2 - buttonWidth + 100/2 ,textTitleFrogRun.get_height() + 180,buttonWidth + 100,buttonHeight,(54, 247, 173),(57, 219, 203),'Start',50, 'broadway',(18, 141, 145))

    # If user presses the rules button, the title screen stops displaying, background becomes light green, and rules are displayed 
    if rulesButton  == True:
        titleScreen = False
        # the background becomes light green
        # if statement prevents filling the screen multiple times (only makes the background light green once)
        if rulesBackground == True:
            screen.fill(LIGHTGREEN)
            rulesBackground = False
        # Setting up text for 'Welcome to Frog Run' header 
        fontTitleRulesHeader = pygame.font.SysFont("Broadway",60)
        textTitleRulesHeader = fontTitleRulesHeader.render("Welcome to Frog Run!", True,(16, 114, 42))

        # Setting up text for rules of the game 
        fontTitleRulesPart1 = pygame.font.SysFont("Elephant",30)
        textTitleRulesPart1 = fontTitleRulesPart1.render("Frog Run is similar to the concept of Frogger", True,(42, 170, 76))

        fontTitleRulesPart2 = pygame.font.SysFont("Elephant",23)
        textTitleRulesPart2 = fontTitleRulesPart2.render("Get a frog on each lilypad using the up, down, right and left arrow keys", True,(24,160,24))
        
        fontTitleRulesPart3 = pygame.font.SysFont("Elephant",28)
        textTitleRulesPart3 = fontTitleRulesPart3.render("If you get hit by a car, or touch water, you will lose a life", True,(24,160,24))

        fontTitleRulesPart4 = pygame.font.SysFont("Elephant",30)
        textTitleRulesPart4 = fontTitleRulesPart4.render("The game ends if you run out of time or lose all lives", True,(24,160,24))

        fontTitleRulesPart5 = pygame.font.SysFont("Elephant",30)
        textTitleRulesPart5 = fontTitleRulesPart5.render("Completing a level earns you 1000 points", True,(24,160,24))

        fontTitleRulesPart6 = pygame.font.SysFont("Elephant",30)
        textTitleRulesPart6 = fontTitleRulesPart6.render("More points can be earned by collecting gold coins", True,(24,160,24))

        fontTitleRulesPart7 = pygame.font.SysFont("Elephant",25)
        textTitleRulesPart7 = fontTitleRulesPart7.render("There will be 6 coins per level, and each one is worth 10 points", True,(24,160,24))

        rulesHeaderY = textTitleRulesHeader.get_height()/2
        # header is displayed as text
        screen.blit(textTitleRulesHeader, (screenWidth/2 - textTitleRulesHeader.get_width()/2,rulesHeaderY))
        # rules of the game is displayed as text
        # each line of the rules is displayed below one another 
        screen.blit(textTitleRulesPart1, (screenWidth/2 - textTitleRulesPart1.get_width()/2,rulesHeaderY + 80))
        screen.blit(textTitleRulesPart2, (screenWidth/2 - textTitleRulesPart2.get_width()/2,rulesHeaderY + 160))
        screen.blit(textTitleRulesPart3, (screenWidth/2 - textTitleRulesPart3.get_width()/2,rulesHeaderY + 210))
        screen.blit(textTitleRulesPart4, (screenWidth/2 - textTitleRulesPart4.get_width()/2,rulesHeaderY + 260))
        screen.blit(textTitleRulesPart5, (screenWidth/2 - textTitleRulesPart5.get_width()/2,rulesHeaderY + 310))
        screen.blit(textTitleRulesPart6, (screenWidth/2 - textTitleRulesPart6.get_width()/2,rulesHeaderY + 360))
        screen.blit(textTitleRulesPart7, (screenWidth/2 - textTitleRulesPart7.get_width()/2,rulesHeaderY + 410))       

        # 'Back' button is created with button function
        backButton = button(screenWidth/2 - buttonWidth/2,rulesHeaderY + 500,buttonWidth,buttonHeight,(54, 247, 173),(57, 219, 203),'Back',50, 'broadway',(18, 141, 145))
        pygame.display.update()

        # If back button is clicked, title screen is displayed, variables for the title and rule screen's background are reset
        if backButton == True:
            titleScreen = True
            introBackground = True
            rulesBackground = True

    # If the 'Start' button is clicked... 
    if startButton  == True:
        
        # Stops title screen from displaying 
        titleScreen = False
        
        # Storing directions for the user in 'enterUsernameTitle'
        enterUsernameTitle = "Enter an Username (Max 5 Characters)"
        # Text size of directions is stored in 'enterUsernameTitleSize'
        enterUsernameTitleSize = 40


        # Creating variable that allows user to type information 
        textInput = pygame_textinput.TextInput()
        clock = pygame.time.Clock()

        # While loop for displaying user text input 
        while enterUsername == True:
            events = pygame.event.get()
            # Background becomes turquoise 
            screen.fill(TURQUOISE)
            clock.tick(30)

            # Takes directions stored in 'enterUsernameTitle' and uses it to prepare text that says value of 'enterUsernameTitle'
            # Text size of directions is equal to value stored in 'enterUsernameTitleSize'
            inputFontTitle = pygame.font.SysFont('Forte',enterUsernameTitleSize)
            inputTextTitle = inputFontTitle.render(enterUsernameTitle,True,(0, 250, 255))

            # Draws turquoise rectangle underneath user's entered text 
            pygame.draw.rect(screen, (66, 244, 203),(screenWidth/2 - 100,250,230,30), 0)

            # Blits the directions
            screen.blit(inputTextTitle, (screenWidth/2 - inputTextTitle.get_width()/2,100))
            # Blits user's entered text 
            screen.blit(textInput.get_surface(), (screenWidth/2 - 100,250))
            
            if textInput.update(events) == True:
                # Whatever the user typed is stored in 'userInput'
                userInput = textInput.get_text()

                # if the user's input is more than 5 charaters... 
                if len(userInput) > 5:
                    # Directions become '"Must be less than 6 characters. Enter a new username"'
                    # text size of directions becomes 30
                    enterUsernameTitle = "Must be less than 6 characters. Enter a new username"
                    enterUsernameTitleSize = 30
                # if the user's input is 5 characters or less... 
                if len(userInput) <= 5:
                    # The while loop stops 
                    enterUsername = False
                    #the time the game was started at is stored in 'startTime'
                    startTime = time.perf_counter()
                    # the screen is cleared 
                    screen.fill(WHITE)
                    # startGame becomes true so that the game's map (rivers, roads, etc.) can be drawn
                    startGame = True 
            pygame.display.update()
            
    for event in pygame.event.get():
        # if user presses x, the application closes 
        if event.type == pygame.QUIT:
            go = False
        if event.type == pygame.KEYDOWN:
            # if the user presses the up arrow key, the user moves up as many units as 'jumpLength' is equal to 
            # Does this by subtracting 'jumpLength' from the user's y coordinate (makes the y coordinate lower)
            # If user presses the up arrow key, they're no longer clamped to a log (if on one)
            if event.key == pygame.K_UP:
                clamp = False
                player.y = player.y - jumpLength
            # if the user presses the down arrow key, the user moves down as many units as 'jumpLength' is equal to 
            # Does this by add 'jumpLength' to the user's y coordinate (makes the y coordinate higher)
            # If user presses the down arrow key, they're no longer clamped to a log (if on one)
            if event.key == pygame.K_DOWN:
                clamp = False
                player.y = player.y + jumpLength

            # If the user presses the left arrow key, the user moves left by making dx equal to speed times - 1
            # As dx is negative, the user moves left during the 'player.move_ip(dx, 0)' line, since the x position of the user is decreasing
            # If the user presses the left arrow key, they're no longer clamped to a log
            if event.key == pygame.K_LEFT:
                dx = -speed
                clamp = False
                #player.x = player.x - 50
            # If the user presses the right arrow key, the user moves right by making dx equal to speed 
            # As dx is positive, the user moves right during the 'player.move_ip(dx, 0)' line, since the x position of the user is increasing 
            # If the user presses the right arrow key, they're no longer clamped to a log
            if event.key == pygame.K_RIGHT:
                dx = speed
                clamp = False
                #player.x = player.x + 50

        # Stops the player from moving if no arrow keys are being pressed/ if all arrow keys are lifted by making dx equal to 0
        # If no arrow keys are being pressed/ if the user lets go of all arrow keys, the user is able to be clamped to a log (if they're on one)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                clamp = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0
                clamp = True
    clock.tick(FPS)

    # Changes the player's x coordinate by the value of dx 
    player.move_ip(dx, 0)

    logIndex = player.collidelist(logs)

    # If the user is colliding with log rect object in 'logs' array, and clamp is set to True, the user is clamped to the log the user is on
    if logIndex >= 0 and clamp == True:
        player.clamp_ip(logs[logIndex])

    
    logIndex2 = player.collidelist(logs2)
    # If the user is colliding with log rect object in 'logs2' array, and clamp is set to True, the user is clamped to the log the user is on
    if logIndex2 >= 0 and clamp == True:
        player.clamp_ip(logs2[logIndex2])


    #If it's the second level...
    if levelTwo == True:
        logIndex3 = player.collidelist(logsLeft2)

        # If the user is colliding with log rect object in 'logsLeft2' array, and clamp is set to True, the user is clamped to the log the user is on
        if logIndex3 >= 0 and clamp == True:
            player.clamp_ip(logsLeft2[logIndex3])
        
        
    coinIndex = player.collidelist(coins)

    # if user touches a coin, that coin disappears (is no longer drawn) and 10 points is added to their score
    if coinIndex >= 0:
        coins.pop(coinIndex)
        score = score + 10
        numberOfCoins = numberOfCoins - 1

    
    for i in range (len(carsLeft)):
        # Makes the cars in 'carsLeft' and 'carsLeft2' array go left by decreasing their x value by 2 
        carsLeft[i].move_ip(-2, 0)
        carsLeft2[i].move_ip(-2, 0)
        # If the back of a car in the 'carsLeft' or 'carsLeft2' array touches the left edge of the screen, the car respawns at the right edge of the screen
        if carsLeft[i].x + 50 == 0:
           carsLeft[i].x = screenWidth
        if carsLeft2[i].x + 50 == 0:
           carsLeft2[i].x = screenWidth
        # If it's the second level...
        if levelTwo == True:
            # Makes the cars in 'carsLeft3' array go left by decreasing their x value by 2 
            carsLeft3[i].move_ip(-2, 0)
            # If the back of a car in the 'carsLeft3' array touches the left edge of the screen, the car respawns at the right edge of the screen
            if carsLeft3[i].x + 50 == 0:
               carsLeft3[i].x = screenWidth
            
    
    for i in range (len(carsRight)):
        # Makes the cars in 'carsRight' array go right by increasing their x value by 2 
        carsRight[i].move_ip(2, 0)
        # If a car in the 'carsRight' array touches the right edge of the screen, the car respawns at the left edge of the screen
        if carsRight[i].x == screenWidth:
           carsRight[i].x = 0
        # If it's the second level...
        if levelTwo == True:
            # Makes the cars in 'carsRight2' array go right by increasing their x value by 2 
            carsRight2[i].move_ip(2, 0)
            # If a car in the 'carsRight2' array touches the right edge of the screen, the car respawns at the left edge of the screen
            if carsRight2[i].x == screenWidth:
               carsRight2[i].x = 0

    carLeftIndex =  player.collidelist(carsLeft)
    carLeftIndex2 = player.collidelist(carsLeft2)
    carRightIndex = player.collidelist(carsRight)

    # If it's the second level...
    if levelTwo == True:
        carLeftIndex3 = player.collidelist(carsLeft3)
        carRightIndex2 = player.collidelist(carsRight2)
        # If the player collides with a car in carsLeft3 or carsRight2 array, the player goes back to spawn point and they have 1 less life 
        if carLeftIndex3 >= 0 or carRightIndex2 >= 0:
            player.x = screenWidth/2 - 50/2
            player.y = screenHeight - (int(screenHeight/10) - 10)
            lives = lives - 1
    
    # If the player collides with a car in carsLeft or carsLeft2 or carsRight array, the player goes back to spawn point and they have 1 less life 
    if carLeftIndex >= 0 or carLeftIndex2 >= 0 or carRightIndex >= 0:
        player.x = screenWidth/2 - 50/2
        player.y = screenHeight - (int(screenHeight/10) - 10)
        lives = lives - 1

        
           
    for i in range (len(logs)):
        # Makes the logs in 'logs' array go left by decreasing their x value by 2 
        logs[i].move_ip(-2, 0)
        # If the back of a log in 'logs' array touches the left edge of the screen, the log respawns at the right edge of the screen  
        if logs[i].x + 90 == 0:
           logs[i].x = screenWidth
        if levelTwo == True:
            # Makes the logs in 'logsLeft2' array go left by decreasing their x value by 2
            logsLeft2[i].move_ip(-2, 0)
            # If the back of a log in 'logsLeft2' array touches the left edge of the screen, the log respawns at the right edge of the screen
            if logsLeft2[i].x + 90 == 0:
               logsLeft2[i].x = screenWidth
            
    # Makes the logs in 'logs2' array move right by increasing their x value by 2
    for i in range (len(logs2)):
        logs2[i].move_ip(2, 0)
        # if a log in 'logs2' array touches the right edge of the screen, the log respawns at the left edge of the screen
        if logs2[i].x == screenWidth:
           logs2[i].x = 0

           
    # Prevents user from leaving the screen
    # If the user's x position is less than 0, the user's x position gets set to 0 (prevents user from leaving left edge of screen)
    if player.x < 0:
        player.x = 0
    # If the user's x position + the user's width is more than the width of the screen, the user's x position gets set to the screen width minus 50
    # (prevents user from leaving the right edge of the screen)
    elif player.x + 50 > screenWidth:
        player.x  = screenWidth - 50
    # if the user's y position + the user's height is more than the screen's height, then the player's y position gets set to the screen height minus 1/10th of the screen height, minus 10
    # (prevents the user from leaving the bottom edge of the screen)
    if player.y + 45 > screenHeight:
        player.y = screenHeight - (int(screenHeight/10) - 10)
    # if the user's y position is less than 0, the user's y position gets set to 0
    # (prevents the user from leaving the top edge of the screen)
    elif player.y < 0:
        player.y = 0

    lilypadIndex = player.collidelist(lilypadsCopy)


    # If the user collides with the first lilypad in the 'lilypadsCopy' array, and the user has not collided with this lilypad before (collisionCheckLilypad1 equals False)...
    if lilypadIndex == 0 and collisionCheckLilypad1 == False:
        # lilypadX and lilypadY becomes the x and y position of the lilypad the user collided with
        # 'lilypadX' and 'lilypadY' will be used for drawing a lilypad with a frog on it later on  
        lilypadX = lilypadsCopy[0].x
        lilypadY = lilypadsCopy[0].y
        #the rect object of the lilypad the user collided with is removed from the 'lilypads' array, so this lilypad doesn't get drawn
        lilypads.remove(lilypadsCopy[0])
        #collisionCheckLilypad1 is set to True, allowing a frog on a lilypad to be drawn at lilypadX and lilypadY
        collisionCheckLilypad1 = True
        # 1 is added to lilypadCollisionCount
        # lilypadCollisionCount keeps track of the number of lilypads the user collided with 
        lilypadCollisionCount = lilypadCollisionCount + 1
        # the user respawns at spawn point
        player.x = screenWidth/2 - 50/2
        player.y = screenHeight - (int(screenHeight/10) - 10)
        
    # If the user collides with the second lilypad in the 'lilypadsCopy' array, and the user has not collided with this lilypad before...    
    if lilypadIndex == 1 and collisionCheckLilypad2 == False:
        # lilypadX2 and lilypadY2 becomes the x and y position of the lilypad the user collided with
        # 'lilypadX2' and 'lilypadY2' will be used for drawing a lilypad with a frog on it later on  
        lilypadX2 = lilypadsCopy[1].x
        lilypadY2 = lilypadsCopy[1].y
        #the rect object of the lilypad the user collided with is removed from the 'lilypads' array, so this lilypad doesn't get drawn
        lilypads.remove(lilypadsCopy[1])
        #collisionCheckLilypad2 is set to True, allowing a frog on a lilypad to be drawn at lilypadX2 and lilypadY2
        collisionCheckLilypad2 = True
        # 1 is added to lilypadCollisionCount
        lilypadCollisionCount = lilypadCollisionCount + 1
        # the user respawns at spawn point
        player.x = screenWidth/2 - 50/2
        player.y = screenHeight - (int(screenHeight/10) - 10)

    # If the user collides with the third lilypad in the 'lilypadsCopy' array, and the user has not collided with this lilypad before...        
    if lilypadIndex == 2 and collisionCheckLilypad3 == False:
        # lilypadX3 and lilypadY3 becomes the x and y position of the lilypad the user collided with
        lilypadX3 = lilypadsCopy[2].x
        lilypadY3 = lilypadsCopy[2].y
        #the rect object of the lilypad the user collided with is removed from the 'lilypads' array, so this lilypad doesn't get drawn
        lilypads.remove(lilypadsCopy[2])
        #collisionCheckLilypad3 is set to True, allowing a frog on a lilypad to be drawn at lilypadX3 and lilypadY3
        collisionCheckLilypad3 = True
        # 1 is added to lilypadCollisionCount
        lilypadCollisionCount = lilypadCollisionCount + 1
        # user respawns at spawn point
        player.x = screenWidth/2 - 50/2
        player.y = screenHeight - (int(screenHeight/10) - 10)

    # If the user collides with the fourth lilypad in the 'lilypadsCopy' array, and the user has not collided with this lilypad before...  
    if lilypadIndex == 3 and collisionCheckLilypad4 == False:
        # lilypadX4 and lilypadY4 becomes the x and y position of the lilypad the user collided with
        lilypadX4 = lilypadsCopy[3].x
        lilypadY4 = lilypadsCopy[3].y
        #the rect object of the lilypad the user collided with is removed from the 'lilypads' array
        lilypads.remove(lilypadsCopy[3])
        collisionCheckLilypad4 = True
        # 1 is added to lilypadCollisionCount
        lilypadCollisionCount = lilypadCollisionCount + 1
        # user respawns at spawn point
        player.x = screenWidth/2 - 50/2
        player.y = screenHeight - (int(screenHeight/10) - 10)

    # if it's the second level...
    if levelTwo == True:
        # If the user collides with the fifth lilypad in the 'lilypadsCopy' array, and the user has not collided with this lilypad before...  
        if lilypadIndex == 4 and collisionCheckLilypad5 == False:
            # lilypadX5 and lilypadY5 becomes the x and y position of the lilypad the user collided with
            lilypadX5 = lilypadsCopy[4].x
            lilypadY5 = lilypadsCopy[4].y
            #the rect object of the lilypad the user collided with is removed from the 'lilypads' array
            lilypads.remove(lilypadsCopy[4])
            collisionCheckLilypad5 = True
            # 1 is added to lilypadCollisionCount
            lilypadCollisionCount = lilypadCollisionCount + 1
            # user respawns at spawn point
            player.x = screenWidth/2 - 50/2
            player.y = screenHeight - (int(screenHeight/10) - 10)
    

    # Switch switches from 'True' to 'False' every 4 seconds
    # i.e. for 4 seconds of the game switch will be True, in the next 4 seconds switch will be False, in the next 4 seconds switch will be True again....

    # if the curret time divided by 8 has no remainders, switch will be false
    if int(time.perf_counter()%8) == 0:
        switch = False
    # else, if the current time divided by 4 has no remainders, switch will be true 
    elif int(time.perf_counter()%4) == 0:
        switch = True 

    if levelTwo == False:
        # if the user collided with all 4 lilypads in the first level...
        if lilypadCollisionCount == 4:
            # 1000 is added to their score 
            score = score + 1000
            # ' lilypadCollisionCount' is reset to 0 for level 2 
            lilypadCollisionCount = 0
            # 'nextLevelScreen' equals True, allowing the screen that displays button for starting level 2 to display
            nextLevelScreen = True
            #StartGame becomes false, preventing the map (roads, rivers, etc.) from being drawn over the 'next level screen'
            startGame = False
   
    # if startGame equals True...
    if startGame == True:
        # all the river rect objects in the 'rivers' array are drawn
        for i in range(len(rivers)):
            pygame.draw.rect(screen,BLUE,rivers[i],0)
        # all the road rect objects in the 'roads' array are drawn
        for i in range (len(roads)):
            pygame.draw.rect(screen, BLACK, roads[i],0)
        # image of strip of glass is displayed, by calling 'getImage' function
        getImage("grass.jpg",screenWidth,grassHeight,0,screenHeight - grassHeight)

        
        # blits every log rect object in 'logs' array
        for i in range (len(logs)):
            screen.blit(logImage, logs[i])
        # Blits every log rect object in 'logs2' array
        for i in range (len(logs2)):
            screen.blit(logImage, logs2[i])
            
        if levelTwo == True:
            #If it's the second level, blits every log rect object in 'logsLeft2' array
            for i in range (len(logsLeft2)):
                screen.blit(logImage, logsLeft2[i])

        # bluts every lilypad rect object in 'lilypads' array
        for i in range (len(lilypads)):
            screen.blit(lilypadImage, lilypads[i])

        # if user collided with the first lilypad in 'lilypadsCopy' array, image of frog on lilypad is displayed where the lilypad the user touched was
        if collisionCheckLilypad1 == True:
            getImage("frogOnEndPoint.png",50,50,lilypadX,lilypadY)
        # if user collided with the second lilypad in 'lilypadsCopy' array, image of frog on lilypad is displayed where the lilypad the user touched was
        if collisionCheckLilypad2 == True:
            getImage("frogOnEndPoint.png",50,50,lilypadX2,lilypadY2)
        # if user collided with the third lilypad in 'lilypadsCopy' array, image of frog on lilypad is displayed where the lilypad the user touched was
        if collisionCheckLilypad3 == True:
            getImage("frogOnEndPoint.png",50,50,lilypadX3,lilypadY3)
        # if user collided with the fourth lilypad in 'lilypadsCopy' array, image of frog on lilypad is displayed where the lilypad the user touched was
        if collisionCheckLilypad4 == True:
            getImage("frogOnEndPoint.png",50,50,lilypadX4,lilypadY4)
        if levelTwo == True:
             # if it's the 2nd level and user collided with the fifth lilypad in 'lilypadsCopy' array, image of frog on lilypad is displayed where the lilypad the user touched was
            if collisionCheckLilypad5 == True:
                getImage("frogOnEndPoint.png",50,50,lilypadX5,lilypadY5)

        #creating and emptying arrays for turtle rect objects that are currently being displayed 
        visibleTurtles = []
        visibleTurtles2 = []
        if switch == True:
            for i in range (len(turtles)):
                # if switch is true, every turtle rect object with an odd index number in 'turtles' array is displayed, and appended to 'visibleTurtles'
                if i%2 != 0:
                    screen.blit(turtleImage, turtles[i])
                    visibleTurtles.append(turtles[i])
                    #if switch is true, every water splash rect object with an odd index in 'waterSplashes2' array is displayed
                    screen.blit(waterSplashImage, waterSplashes2[i])
                    
            #if switch is true, every water splash rect object with an even index number in 'waterSplashes' array is displayed
            #if switch is true, every turtle rect object with an even index in 'turtles2' array is displayed, and appended to 'visibleTurtles2'     
            for i in range (len(waterSplashes)):
                if i%2 == 0:
                    screen.blit(waterSplashImage, waterSplashes[i])
                    
                    screen.blit(turtleImage,turtles2[i])
                    visibleTurtles2.append(turtles2[i])
                
        else:
            for i in range (len(turtles)):
                # if switch is False, every turtle rect object with an even index number in 'turtles' array is displayed, and appended to 'visibleTurtles'
                if i%2 == 0:
                    screen.blit(turtleImage, turtles[i])
                    visibleTurtles.append(turtles[i])
                    #if switch is False, every water splash rect object with an even index in 'waterSplashes2' array is displayed
                    screen.blit(waterSplashImage, waterSplashes2[i])

            #if switch is False, every water splash rect object with an odd index number in 'waterSplashes' array is displayed
            #if switch is False, every turtle rect object with an odd index in 'turtles2' array is displayed, and appended to 'visibleTurtles2'
            for i in range (len(waterSplashes)):
                if i%2 != 0:
                    screen.blit(waterSplashImage, waterSplashes[i])
                    
                    screen.blit(turtleImage, turtles2[i])
                    visibleTurtles2.append(turtles2[i])

        # draws the coins     
        for i in range (len(coins)):
            pygame.draw.rect(screen,(239, 229, 45),coins[i],0)

        # displays all the car rect objects in carsLeft and carsLeft2 array
        for i in range (len(carsLeft)):
            screen.blit(greenCarImage, carsLeft[i])
            screen.blit(greenCarImage, carsLeft2[i])
            if levelTwo == True:
                # If it's the 2nd level, displays all the car rect objects in carsLeft3 array
                screen.blit(greenCarImage, carsLeft3[i])

        # displays all the car rect objects in 'carsRight' array
        for i in range (len(carsRight)):
            screen.blit(redCarImage, carsRight[i])
            if levelTwo == True:
                # if it's level 2, displays all the car rect objects in 'carsRight2' array
                screen.blit(redCarImage, carsRight2[i])

        # displays the player 
        screen.blit(playerImage, player)

        
        riverIndex = player.collidelist(rivers)
        turtleIndex = player.collidelist(visibleTurtles)
        turtleIndex2 = player.collidelist(visibleTurtles2)


        # If user is colliding with a river...
        if riverIndex >= 0:
            # If it's level two...
            if levelTwo == True:
                # if the user isn't colliding with any of the logs in logIndex2, logIndex, and logIndex3, as well as any turtles in turtleIndex and turtleIndex2
                # player gets spawned at spawn point
                # player loses a life
                if logIndex2 < 0 and logIndex < 0 and logIndex3 < 0 and turtleIndex < 0 and turtleIndex2 < 0:
                    player.x = screenWidth/2 - 50/2
                    player.y = screenHeight - (int(screenHeight/10) - 10)
                    lives = lives - 1
            # if it isn't the 2nd level...
            # if player isn't touching any of the logs in logIndex2 and logIndex as well as any of the turtles in turtleIndex and turtleIndex2,
            # player gets spawned at spawn point
            # player loses a life
            elif logIndex2 < 0 and logIndex < 0 and turtleIndex < 0 and turtleIndex2 < 0:
                player.x = screenWidth/2 - 50/2
                player.y = screenHeight - (int(screenHeight/10) - 10)
                lives = lives - 1

            

        circleX = 0
        
        for i in range (lives):
            # draws a circle for each life the player has left
            # each circle is spaced out by 25 units 
            circleX = circleX + 25
            pygame.draw.circle(screen,(244, 170, 66),(circleX,screenHeight - (7*2) ),7,0)
        # Text that says 'Lives:' is displayed above circles
        fontTitleLivesRemaining = pygame.font.SysFont("elephant",30)
        textTitleLivesRemaining = fontTitleLivesRemaining.render("Lives:", True,(237, 237, 237))
        screen.blit(textTitleLivesRemaining,(25 - 7/2,screenHeight - 60))

        fontTitleTimeSurvived = pygame.font.SysFont("Broadway",65)

        
        if timeRemaining > 0:
            # 'timeRemaining' is a variable that holds the number of seconds remaining in the game
            # calculated by subtracting how much time the user spent in the game already from the number of seconds permitted in the level (totalTime)
            timeRemaining = totalTime - int((time.perf_counter() - startTime))
            fontTitleTimeRemaining = pygame.font.SysFont("elephant",40)
            # number of seconds remaining is displayed as text 
            textTitleTimeRemaining = fontTitleTimeRemaining.render(str(timeRemaining), True,(237, 237, 237))
            screen.blit(textTitleTimeRemaining, (screenWidth - textTitleTimeRemaining.get_width() - (25 - 7/2),screenHeight - textTitleTimeRemaining.get_height()))

    pygame.display.update()

    # if nextLevelScreen is True...
    if nextLevelScreen == True:
        # background becomes turquoise colour
        screen.fill((65, 242, 198))
        # text that says 'level 1 complete' is displayed 
        fontTitleCompletedLevel = pygame.font.SysFont("Goudy Stout",40)
        textTitleCompletedLevel = fontTitleCompletedLevel.render("Level 1 Complete!", True,(7, 79, 61))
        screen.blit(textTitleCompletedLevel,(screenWidth/2 - textTitleCompletedLevel.get_width()/2,textTitleCompletedLevel.get_height()/2))
        
        # button that begins the next level when clicked is created by calling the button function 
        levelTwoButton = button(screenWidth/2 - buttonWidth/2, textTitleCompletedLevel.get_height() + 100, buttonWidth, buttonHeight, (23, 183, 45),(19, 160, 78), "Next Level",35, 'broadway',(8, 82, 99))
        pygame.display.update()

        # if the 'Next Level' button is clicked...
        if levelTwoButton == True:
            #jumpLength is changed to 1/12th of the screen
            jumpLength = int(screenHeight/12)
            # player's x and y coordinates are reset to spawn point
            player.x = screenWidth/2 - 50/2
            player.y = screenHeight - (int(screenHeight/10) - 10)
            # number of lives is reset to 4
            lives = 4
            # reset variables for colliding with lilypads 
            collisionCheckLilypad1 = False
            collisionCheckLilypad2 = False
            collisionCheckLilypad3 = False
            collisionCheckLilypad4 = False
            collisionCheckLilypad5 = False
            lilypadCollisionCount = 0

            # The following is code for creating arrays of rect objects used in level 2
            lilypadX = 0
            # creates array (lilypads)of 5 lilypad rect objects, that appear as lilypad images at end of map 
            lilypads = []
            for i in range(5):
                lilypadX = lilypadX + + 50 + 70
                lilypadImage = pygame.image.load("lilypadEndPoint.png").convert_alpha()
                lilypadImage= pygame.transform.scale(lilypadImage, (50,int(screenHeight/12)))
                lilypad = lilypadImage.get_rect()
                lilypad.x = lilypadX
                lilypad.y = 0
                lilypads.append(lilypad)
            # lilypadsCopy becomes copy of lilypads array 
            lilypadsCopy = lilypads.copy()
 
            # changes each river rect object's in rivers array height to 1/6th of the screen height
            # changes the y coordinate of each river rect object so that rivers are shown in between roads
            for i in range (len(rivers)):
                rivers[i].h = screenHeight/6
                rivers[i].y = i * 2 * (screenHeight/6)

                
            for i in range (numOfRoads + 1):
                if i ==2:
                    # if i is equal to 2, creates new road rect object and appends it to roads array
                    road = pygame.Rect(0, (i * 2 + 1) * (screenHeight/6), screenWidth, screenHeight/6)
                    roads.append(road)
                else:
                    # changes the height of each road rect object in 'roads' array to 1/6th of the screen height
                    # changes the y position of each road rect object in 'roads' array so that the roads appear in between the new rivers
                    roads[i].h = screenHeight/6
                    roads[i].y = (i*2 + 1) * screenHeight/6
            #height of grass is changed to 50  
            grassHeight = 50


           
            
            # creates array of log rect objects ('logs') that are on the last river
            # each log has a height of 1/12th of the screen, and a width of 90 
            logs = []
            logX = screenWidth - 200 
            for i in range (int(screenWidth/(90+150))):
                logX = logX + 90 + 150
                logImage = pygame.image.load("log.png").convert_alpha()
                logImage  = pygame.transform.scale(logImage, (90,int(screenHeight/12)))
                log = logImage.get_rect()
                log.x = logX
                log.y = screenHeight/12
                logs.append(log)

            #creates array of log rect objects ('logs2') that are on the second river
            # each log has a height of 1/12th of the screen, and a width of 90 
            logs2 = []
            logX = 30
            for i in range (int(screenWidth/(90+150))):
                logX = logX + 90 + 150
                logImage = pygame.image.load("log.png").convert_alpha()
                logImage  = pygame.transform.scale(logImage, (90,int(screenHeight/12)))
                log = logImage.get_rect()
                log.x = logX
                log.y = screenHeight/6 * 2
                logs2.append(log)

            # creates array of log rect objects ('logsLeft2') that are on the first river
            # each log has a height of 1/12th of the screen, and a width of 90 
            logsLeft2 = []
            logX = screenWidth - 200 
            for i in range (int(screenWidth/(90+150))):
                logX = logX + 90 + 150
                logImage = pygame.image.load("log.png").convert_alpha()
                logImage  = pygame.transform.scale(logImage, (90,int(screenHeight/12)))
                log = logImage.get_rect()
                log.x = logX
                log.y = screenHeight/6 * 4
                logsLeft2.append(log)

            # creates array of turtle rect objects ('turtles') that are on the 2nd river
            # each turtle has a height of 1/12th of the screen, and a width of 50 
            turtles = []
            turtleX = -60
            for i in range (int(screenWidth/(50 + 70))):
                turtleX = turtleX + 50 + 70
                turtleImage = pygame.image.load("turtle.png").convert_alpha()
                turtleImage  = pygame.transform.scale(turtleImage, (50,int(screenHeight/12)))
                turtle = turtleImage.get_rect()
                turtle.x = turtleX
                turtle.y = (screenHeight/6 * 2) + (screenHeight/12)
                turtles.append(turtle)

            # creates array of water splash rect objects ('waterSplashes') that are on the 2nd river
            # each water splash has a height of 1/12th of the screen, and a width of 50 
            waterSplashes = []
            waterSplashX = -60
            for i in range (int(screenWidth/(50 + 70))):
                waterSplashX = waterSplashX + 50 + 70
                waterSplashImage = pygame.image.load("waterSplash.gif").convert_alpha()
                waterSplashImage  = pygame.transform.scale(waterSplashImage, (50,int(screenHeight/12)))
                waterSplash = waterSplashImage.get_rect()
                waterSplash.x = waterSplashX
                waterSplash.y = (screenHeight/6 * 2) + (screenHeight/12)
                waterSplashes.append(waterSplash)


            # creates array of turtle rect objects ('turtles2') that are on the 1st river
            # each turtle has a height of 1/12th of the screen, and a width of 50 
            turtles2 = []
            turtleX = -60
            for i in range (int(screenWidth/(50 + 70))):
                turtleX = turtleX + 50 + 70
                turtleImage = pygame.image.load("turtle.png").convert_alpha()
                turtleImage  = pygame.transform.scale(turtleImage, (50,int(screenHeight/12)))
                turtle = turtleImage.get_rect()
                turtle.x = turtleX
                turtle.y = (screenHeight/6) * 4 + (screenHeight/12)
                turtles2.append(turtle)

            # creates array of water splash rect objects ('waterSplashes2') that are on the 1st river
            # each water splash has a height of 1/12th of the screen, and a width of 50 
            waterSplashes2 = []
            waterSplashX = -60
            for i in range (int(screenWidth/(50 + 70))):
                waterSplashX = waterSplashX + 50 + 70
                waterSplashImage = pygame.image.load("waterSplash.gif").convert_alpha()
                waterSplashImage  = pygame.transform.scale(waterSplashImage, (50,int(screenHeight/12)))
                waterSplash = waterSplashImage.get_rect()
                waterSplash.x = waterSplashX
                waterSplash.y = (screenHeight/6) * 4 + (screenHeight/12)
                waterSplashes2.append(waterSplash)


            # creates array of car rect objects ('carsLeft') that are going left on the 3rd road
            # each car has a height of 1/12th of the screen, and a width of 50 
            carsLeft = []
            carX = screenWidth - 50
            for i in range (int(screenWidth/(50+80))):
                carX = carX + 50 + 80
                greenCarImage = pygame.image.load("greenCar.png").convert_alpha()
                greenCarImage= pygame.transform.scale(greenCarImage, (50,int(screenHeight/12)))
                car = greenCarImage.get_rect()
                car.x = carX
                car.y = screenHeight/6
                carsLeft.append(car)
            # creates array of car rect objects ('carsRight') that are going right on the 3rd road
            # each car has a height of 1/12th of the screen, and a width of 50 
            carsRight = []
            carX2 = 0
            for i in range (int(screenWidth/(50+110))):
                carX2 = carX2 + 50 + 110
                redCarImage = pygame.image.load("redCar.png").convert_alpha()
                redCarImage  = pygame.transform.scale(redCarImage, (50,int(screenHeight/12)))
                car = redCarImage.get_rect()
                car.x = carX2
                car.y = (screenHeight/6) + (screenHeight/12)
                carsRight.append(car)

            # creates array of car rect objects ('carsRight2') that are going right on the 2nd road
            # each car has a height of 1/12th of the screen, and a width of 50 
            carsRight2 = []
            carX2 = 0
            for i in range (int(screenWidth/(50+80))):
                carX2 = carX2 + 50 + 80
                redCarImage = pygame.image.load("redCar.png").convert_alpha()
                redCarImage  = pygame.transform.scale(redCarImage, (50,int(screenHeight/12)))
                car = redCarImage.get_rect()
                car.x = carX2
                car.y = screenHeight/6 * 3 + screenHeight/12
                carsRight2.append(car)     

            # creates array of car rect objects ('carsLeft2') that are going left on the 1st road
            # each car has a height of 1/12th of the screen, and a width of 50 
            carsLeft2 = []
            carX = screenWidth - 50
            for i in range (int(screenWidth/(50+80))):
                carX = carX + 50 + 80
                greenCarImage = pygame.image.load("greenCar.png").convert_alpha()
                greenCarImage= pygame.transform.scale(greenCarImage, (50,int(screenHeight/12)))
                car = greenCarImage.get_rect()
                car.x = carX
                car.y = (screenHeight/6 * 5)
                carsLeft2.append(car)

            # creates array of car rect objects ('carsLeft3') that are going left on the 2nd road
            # each car has a height of 1/12th of the screen, and a width of 50 
            carsLeft3 = []
            carX = screenWidth - 50
            for i in range (int(screenWidth/(50+80))):
                carX = carX + 50 + 80
                greenCarImage = pygame.image.load("greenCar.png").convert_alpha()
                greenCarImage= pygame.transform.scale(greenCarImage, (50,int(screenHeight/12)))
                car = greenCarImage.get_rect()
                car.x = carX
                car.y = screenHeight/6 * 3
                carsLeft3.append(car)
            
            # appends as many rect objects as the user removed from the 'coins' array last round to 'coins' so that 'coins' is an array of 6 rect objects 
            for i in range (6 - numberOfCoins):
                coin = pygame.Rect(random.randint(0,screenWidth - 10),random.randint(int(screenHeight/12),screenHeight-10 ),10,10)
                coins.append(coin)

            for i in range (len(coins)):
                # If the coin's y coordinate is where the logs on the last river are displayed, the coin's y coordinate gets redefined so that it spawns in the middle of the log (vertically)
                if coins[i].y >= 0 and coins[i].y <= screenHeight/6:
                    coins[i].y = (screenHeight/12) + ((screenHeight/12)/2)
                # If the coin's y coordinate is where the green cars on the last road are displayed, the coin spawns in the middle of the green cars (vertically),
                elif coins[i].y>= (screenHeight/6) and coins[i].y <= (screenHeight/6) + (screenHeight/12):
                    coins[i].y = (screenHeight/6) + ((screenHeight/12)/2)    
                # If the coin's y coordinate is where the red cars on the last road are displayed, the coin spawns in the middle of the red cars (vertically),
                elif coins[i].y >= (screenHeight/6) +  (screenHeight/12) and coins[i].y <= (screenHeight/6) * 2:
                    coins[i].y = ((screenHeight/6) + (screenHeight/12)) + ((screenHeight/12)/2)
                # If the coin's y coordinate is where the logs on the 2nd river are displayed, the coin spawns in the middle of the logs  (vertically)
                elif coins[i].y >= (screenHeight/6) * 2 and coins[i].y <= (screenHeight/6 * 2) + (screenHeight/12):
                    coins[i].y = (screenHeight/6 * 2) + ((screenHeight/12)/2)
                # If the coin's y coordinate is where the water splashes  on the 2nd river are displayed, the coin spawns in the middle of the water splashes
                # This happens by setting the x position of the coin to the x coordinate of a random water splash in the 'waterSplahes' array, plus half of the water splash's width and minus half of the coin's width to center it
                # Sets the coin's y coordinate to the middle of the water splash (vertically)
                elif coins[i].y >= (screenHeight/6 * 2) + (screenHeight/12) and coins[i].y <= (screenHeight/6) * 3:
                    coins[i].x = waterSplashes[random.randint(0,len(waterSplashes) -1 )].x + (50/2) - 5
                    coins[i].y = ((screenHeight/6 *2) + (screenHeight/12)) + ((screenHeight/12)/2)
                #If the coin's y coordinate is where the green cars on the 2nd road are displayed, the coin spawns in the middle of the green cars (vertically)
                elif coins[i].y >= (screenHeight/6 * 3) and coins[i].y <= (screenHeight/6 * 3) + (screenHeight/12) :
                    coins[i].x = waterSplashes[random.randint(0,len(waterSplashes) -1 )].x + (50/2) - 5
                    coins[i].y = (screenHeight/6 *3) + ((screenHeight/12)/2)
                #If the coin's y coordinate is where the red cars on the 2nd road are displayed, the coin spawns in the middle of the red cars (vertically)
                elif coins[i].y >= (screenHeight/6 * 3) + (screenHeight/12) and coins[i].y <= (screenHeight/6 * 4):
                    coins[i].y = ((screenHeight/6 *3) + (screenHeight/12)) + ((screenHeight/12)/2)
                #If the coin's y coordinate is where the logs on the 1st river are displayed, the coin spawns in the middle of the logs (vertically)
                elif coins[i].y >= (screenHeight/6 * 4) and coins[i].y <= (screenHeight/6 * 4) + (screenHeight/12) :
                    coins[i].y = (screenHeight/6 *4) + ((screenHeight/12)/2)
                #If the coin's y coordinate is where the turtles on the 1st river are displayed, the coin spawns in the middle of the turtles
                elif coins[i].y >= (screenHeight/6 * 4) + (screenHeight/12) and coins[i].y <= (screenHeight/6 * 5):
                    coins[i].x = waterSplashes2[random.randint(0,len(waterSplashes2) -1 )].x + (50/2) - 5
                    coins[i].y = ((screenHeight/6 *4) + (screenHeight/12)) + ((screenHeight/12)/2)
                #If the coin's y coordinate is where the cars on the 1st road are displayed, the coin spawns in the middle of the cars (vertically)
                elif coins[i].y >= (screenHeight/6 * 5) and coins[i].y <= (screenHeight/6 * 5) + (screenHeight/12) :
                    coins[i].y = (screenHeight/6 *5) + ((screenHeight/12)/2)

            # startTime is set to the number of seconds its been since the game was opened   
            startTime = time.perf_counter()
            # the user nows has 300 seconds to complete the 2nd level
            totalTime = 300

            # startGame becomes true, so that the map (roads, rivers, etc.) can be displayed, the next level screen stops displaying
            # levelTwo becomes true 
            startGame = True
            nextLevelScreen = False
            levelTwo = True
                        
        
    if lives == 0 or timeRemaining == 0 or lilypadCollisionCount == 5:
        #'endResult' is a variable that gets displayed as text on the end screen
        # If user ran out of lives, endResult becomes 'You ran out of lives'!
        if lives == 0:
            endResult = "You ran out of lives!"
        # Else if the user ran out of time, endResult becomes 'You ran out of time!'
        elif timeRemaining == 0:
            endResult = "You ran out of time!"
        # Else, if the user got to all 5 lilypads in level 2, end result becomes 'You beat the game!'
        # 1000 points is also added to the user's score
        # lilypadCollisionCount resets to 0 to avoid giving the user 1000 points each time program goes through main while loop
        elif lilypadCollisionCount == 5:
            endResult = "You beat the game!"
            score = score + 1000
            lilypadCollisionCount = 0
        # startGame becomes False to prevent the map (rivers, roads, etc.) from being drawn over the end screen
        # 'endScreen' becomes True to allow end screen information to be drawn
        startGame = False
        endScreen = True 
        
    # If the game has ended...
    if endScreen == True:

        # preparing text that says what endResult is equal 
        fontTitleEndResult = pygame.font.SysFont("Broadway",60)
        textTitleEndResult = fontTitleEndResult.render(endResult, True,(65, 242, 198))

        # preparing text that says the user's name, and score ([user]'s Score: [score]")
        fontTitleScore = pygame.font.SysFont("Forte",50)
        textTitleScore = fontTitleScore.render(userInput + "'s" + " Score:" + " " + str(score), True,(65, 242, 198))        

        #makes the background dark green
        screen.fill((7,79,61))
        #displays text that says what endResult is equal to
        # displays text that says the user's name and score 
        screen.blit(textTitleEndResult,(screenWidth/2 - textTitleEndResult.get_width()/2,40))
        screen.blit(textTitleScore,(screenWidth/2 - textTitleScore.get_width()/2, 40 + textTitleScore.get_height() + 10 ))


        # code for displaying top 5 high scores
        # code will on execute if orderHighScores is equal to True, to prevent program from writing user's name and score to highscores array multiple times in one game
        if orderHighScores == True:
            highScores = []
            orderedHighScores = []
            previousScores = ''


            #opens highscores.txt file for reading, if file isn't found program tells the user 'highscores.txt file not found'
            # highscores.txt contains all the previous scores 
            try:
                previousHighScoresReadingFile = open('highscores.txt', 'r')
            except:
                print("highscores.txt file not found")

            # The previous scores, along with who got each score is stored in 'previousScores'
            for line in previousHighScoresReadingFile:
                line = line.strip()
                previousScores = previousScores + line + '\n'

            previousHighScoresReadingFile.close()

            # opens highscores.txt for writing 
            try:
                highScoresWritingFile = open('highscores.txt', 'w')
            except:
                print("highscores.txt file not found")

            # the previous scores, along with the user's name and score is written to 'highscorex.txt'
            # each name and score appears on their own line 
            highScoresWritingFile.write(previousScores + str(score) + ',' + userInput + '\n')
                
            highScoresWritingFile.close()


            # highscores.txt is open for reading again 
            try:
                highScoresReadingFile = open('highscores.txt', 'r')
            except:
                print("highscores.txt file not found")

            #each line in the highscores.txt file is appended to highScores array
            for line in highScoresReadingFile:
                line = line.strip()
                highScores.append(line)

            # each score and name is stored in an array, and appended to 'orderedHighScores'
            # orderedHighScores becomes an array of arrays, each array containing a name and a score 
            for i in range(len(highScores)):
                userAndScore = highScores[i].split(',')
                orderedHighScores.append(userAndScore)
            print(orderedHighScores)


            unorderedScoreCount = 0
            organizing = True 

            # sorting scores from lowest to highest in 'orderedHighScores' array
            while organizing == True:
                for i in range (len(orderedHighScores) - 1):
                    #'nameAndScore' is equal to the name and score that's at the index of orderedHighScores equal to i
                    nameAndScore = orderedHighScores[i]
                    #'nextNameAndScore' is equal to the next name and score that's at the index of orderedHighScores equal to i + 1
                    nextNameAndScore = orderedHighScores[i + 1]

                    # currentScore is the score you're comparing to see if it needs to switch places in the orderedHighScores array
                    # nextScore is the score after currentScore in the orderedHighScores array
                    currentScore = int(nameAndScore[0])
                    nextScore = int(nextNameAndScore[0])

                    # if the currentScore is higher than the nextScore
                    # then the score and its' corresponding username, and the next score and its' corresponding username switch places in the orderedHighScores array
                    if currentScore > nextScore:
                        orderedHighScores[i] = nextNameAndScore
                        orderedHighScores[i + 1] = nameAndScore
                            
                unorderedScoreCount = 0
                for i in range (len(orderedHighScores) - 1):

                    nameAndScore = orderedHighScores[i]
                    nextNameAndScore = orderedHighScores[i + 1]

                    currentScore = int(nameAndScore[0])
                    nextScore = int(nextNameAndScore[0])

                    # going through array to make sure everything is in order
                    # if a score is higher than the next score in the array, 1 is added to 'unorderedScoreCount'
                    if currentScore > nextScore:
                        unorderedScoreCount = unorderedScoreCount + 1
                # if unorderedScoreCount is more than 1, then the organizing process repeats, else, organizing becomes False, so the array stops getting organized
                if unorderedScoreCount == 0:
                    organizing = False
  
            highScoresReadingFile.close()
            orderHighScores = False


        # the highest score, and the corresponding username is displayed as text
        # does this by displaying the first element of the last element in the orderedHighScores array (the highest score), and then the 2nd element of the last element (the corresponding username)
        fontTitleHighScore1 = pygame.font.SysFont("Elephant",40)
        textTitleHighScore1 = fontTitleHighScore1.render(str(orderedHighScores[-1][0]) + ',' + str(orderedHighScores[-1][1]), True,(66, 244, 158))
        # the 2nd highest score, and the corresponding username is displayed as text 
        fontTitleHighScore2 = pygame.font.SysFont("Elephant",40)
        textTitleHighScore2 = fontTitleHighScore2.render(str(orderedHighScores[-2][0]) + ',' + str(orderedHighScores[-2][1]), True,(66, 244, 158))
        # the 3rd highest score, and the corresponding username is displayed as text 
        fontTitleHighScore3 = pygame.font.SysFont("Elephant",40)
        textTitleHighScore3 = fontTitleHighScore3.render(str(orderedHighScores[-3][0]) + ',' + str(orderedHighScores[-3][1]), True,(66, 244, 158))
        # the 4th highest score, and the corresponding username is displayed as text 
        fontTitleHighScore4 = pygame.font.SysFont("Elephant",40)
        textTitleHighScore4 = fontTitleHighScore4.render(str(orderedHighScores[-4][0]) + ',' + str(orderedHighScores[-4][1]), True,(66, 244, 158))
        # the 5th highest score, and the corresponding username is displayed as text 
        fontTitleHighScore5 = pygame.font.SysFont("Elephant",40)
        textTitleHighScore5 = fontTitleHighScore1.render(str(orderedHighScores[-5][0]) + ',' + str(orderedHighScores[-5][1]), True,(66, 244, 158))

        


        
        screen.blit(textTitleHighScore1, (screenWidth/2 - textTitleHighScore1.get_width()/2, 200))
        screen.blit(textTitleHighScore2, (screenWidth/2 - textTitleHighScore2.get_width()/2, 240))
        screen.blit(textTitleHighScore3, (screenWidth/2 - textTitleHighScore3.get_width()/2, 280))
        screen.blit(textTitleHighScore4, (screenWidth/2 - textTitleHighScore4.get_width()/2, 320))
        screen.blit(textTitleHighScore5, (screenWidth/2 - textTitleHighScore5.get_width()/2, 360))
        


        


        

        # button for starting a new game is created with the button function 
        newGameButton = button(screenWidth/2 - 100, screenHeight - 100 ,200,80,(66, 215, 244),(65, 157, 244),"New Game", 30, "Impact", (0,0,0))

        if newGameButton == True:
            # If the new game button is clicked, all of the variables are resetted for a new game 
            titleScreen = True
            introBackground = True
            rulesBackground = True
            nextLevelBackground = True
            enterUsername = True
            levelOne = True
            levelTwo = False
            switch = True
            startGame = False 
            collisionCheckLilypad1 = False
            collisionCheckLilypad2 = False
            collisionCheckLilypad3 = False
            collisionCheckLilypad4 = False
            totalTime = 240
            numberOfCoins = 6
            levelOneArrays = True
            nextLevelScreen = False
            timeRemaining = 1
            score = 0
            grassHeight = 60
            jumpLength = int((screenHeight/10))
            lives = 4
            lilypadCollisionCount = 0
            orderHighScores = True
            # setting endScreen to false stops displaying the end screen
            endScreen = False
        
             

        
        pygame.display.update()
        

pygame.quit()
sys.exit()

