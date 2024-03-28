import pygame as pygame

def MoveBall():
    global ballSpeedx, ballSpeedy, ballLocation, ball, scoreA,scoreB
    
    if ballLocation[0] > screenWidth:
        ballSpeedx = -ballSpeedx
        scoreA = scoreA + 1
    if ballLocation[0] <= 0:
        ballSpeedx = -ballSpeedx
        scoreB = scoreB + 1
    
    if ballLocation[0]< 0:
        ballSpeedx = -ballSpeedx
        
    if ballLocation[1] < 0:
        ballSpeedy = -ballSpeedy
    
    if ballLocation [1] > screenHeight:
        ballSpeedy = -ballSpeedy
            
        
    ballLocation[0] = ballLocation[0] + ballSpeedx
    ballLocation[1] = ballLocation[1] + ballSpeedy
    ball=pygame.draw.circle(window, hotpink, ballLocation, radius, 0)
    #print(ball)

def MovePaddle():
    global PadASpeed, PadA, PadB, PadBSpeed, ball
    if PadA.top <= 0:
        print("top of screen")
        PadA = PadA.move(0,2)
        PadASpeed=0
    if PadB.top <= 0:
        print("top of screen")
        PadB = PadB.move(0,2)
        PadBSpeed=0
    PadA = PadA.move(0,PadASpeed)
    PadB = PadB.move(0,PadBSpeed)
    pygame.draw.rect(window, pinkpurple, PadA)
    pygame.draw.rect(window, pinkpurple, PadB)
def drawCenterLine():
    global screenWidth, screenHeight
    pygame.draw.line(window,cyan,(screenWidth//2,0),(screenWidth//2,screenHeight))


def drawScore(font):
    global scoreA, scoreB
    
    text = font.render(str(scoreA),True, blue)
    window.blit(text,(200,30))
    text = font.render(str(scoreB),True,blue)
    window.blit(text,(700,30))
    
def Win(font):
    global scoreA, scoreB
    if scoreA >=20:
        text = font.render(("PlayerAwins"),True, blue)
        window.blit(text,(500,30))

    if scoreB >=20:
        text = font.render(("PlayerBwins"),True, blue)
        window.blit(text,(500,30))
        
def Ballchangesize(size):
    global radius
    radius = size
    
def ScreenWidthsize(sizeW, sizeH):
    global screenWidth, screenHeight 
    screenWidth = sizeW
    screenHeight = sizeH
    pygame.display.set_mode((sizeW, sizeH))

timer = pygame.time.Clock()

screenWidth = 1000
screenHeight = 600

window = pygame.display.set_mode([screenWidth, screenHeight])
ballSpeedx = 1
ballSpeedy = -1
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
cyan = (66, 214, 142)
pinkpurple = (214, 34, 214)
hotpink = (214,34,85)
radius = 20
ballLocation=[500,300]
ball = pygame.Rect(ballLocation, (radius, radius))

PadA = pygame.Rect((0,150),(10,300))
PadASpeed = 0
PadB = pygame.Rect((990,150),(10,300))
PadBSpeed = 0

scoreA=0
scoreB=0

pygame.font.init()
print (pygame.font.get_fonts())
font=pygame.font.SysFont("cambria", 24)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                PadASpeed = -2
            if event.key == pygame.K_DOWN:
                PadASpeed = 2
            if event.key == pygame.K_w:
                PadBSpeed = -2
            if event.key == pygame.K_s:
                PadBSpeed = 2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                PadASpeed = 0
            if event.key == pygame.K_DOWN:
                PadASpeed = 0
            if event.key == pygame.K_w:
                PadBSpeed = 0
            if event.key == pygame.K_s:
                PadBSpeed = 0
            if event.key == pygame.K_a:
                radius = 30
            if event.key == pygame.K_z:
                radius = 10
            if event.key == pygame.K_x:
                radius = 20
            if event.key == pygame.K_e:
                sizeW = 2000
                sizeH = 900
                ScreenWidthsize(sizeW, sizeH)
                
            if event.key == pygame.K_r:
                sizeW = 900
                sizeH = 750
                print("r")
                ScreenWidthsize(sizeW, sizeH)
            
            
                                
    if PadA.colliderect(ball):
        ballSpeedx = -ballSpeedx
        ballSpeedx = ballSpeedx +1
        ballSpeedy = ballSpeedy +1
    if PadB.colliderect(ball):
        ballSpeedx = -ballSpeedx
        ballSpeedx = ballSpeedx +0.5
        ballSpeedy = ballSpeedy +0.5
        #print(hit)
    
    timer.tick(60)
    window.fill(black) 
    MoveBall()
    MovePaddle()
    drawCenterLine()
    drawScore(font)
    Win(font)
    
    pygame.display.flip()
    #check quit event
    #check up, down, spacebar event