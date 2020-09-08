import random
import pygame
import math
import  time
from pygame import mixer
pygame.init()
# background music
mixer.music.load('background.wav')
mixer.music.play(-1)

gun= mixer.Sound("bullet.wav")
blust = mixer.Sound("blust.wav")

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 40)

textX = 20
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("SCORE : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 55, 55))
    screen.blit(over_text, (200, 250))
    score = font.render("SCORE : " + str(score_value), True, (255, 55, 55))
    screen.blit(score, (280, 380))
    blust.play()
    pygame.display.update()
    time.sleep(3)
    return  False



screen = pygame.display.set_mode((800, 600))
sky = pygame.image.load("sky.png")
cloud1 = pygame.image.load("cloud1.png")
cloud2 = pygame.image.load("cloud2.png")
cloud3 = pygame.image.load("cloud3.png")

cloud1y = random.randint(40,540)
cloud2y = random.randint(40,540)
cloud3y = random.randint(40,540)
cloud1x = 800
cloud2x = 600
cloud3x = 200
cloudxchange = 1

playerimg = pygame.image.load("plane.png")
playerX= 20
playerY= 300
playerYchange = 0

enemy1img = pygame.image.load("bird1.png")
enemy2img = pygame.image.load("bird2.png")
enemy3img = pygame.image.load("bird3.png")
enemy1x=800
enemy2x=1000
enemy3x=1200
enemy1y = random.randint(50,550)
enemy2y = random.randint(50,550)
enemy3y = random.randint(50,550)
enemyxchange = 1




def showcloud(cloud,x,y):
    screen.blit(cloud,(x,y))

def player(playerX , playerY):
    screen.blit(playerimg, (playerX, playerY))

def showenemy(enemy , x,y):
    screen.blit(enemy,(x,y))

bulletImg = pygame.image.load('bullet.png')
bulletX = 20
bulletY = 300
bulletX_change = 10
bulletY_change = 0
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 150, y+20))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

running=True
while (running):
    screen.blit(sky,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerYchange = -1
            if event.key == pygame.K_DOWN:
                playerYchange = 1
            if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        gun.play()
                # Get the current x cordinate of the spaceship
                        bulletY = playerY
                        fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerYchange = 0

    cloud1x-=cloudxchange
    if cloud1x==-200:
        cloud1x=800
        cloud1y=random.randint(40,540)
    showcloud(cloud1,cloud1x,cloud1y)

    cloud2x-=cloudxchange
    if cloud2x==-200:
        cloud2x=800
        cloud2y=random.randint(40,540)
    showcloud(cloud2,cloud2x,cloud2y)

    cloud3x-=cloudxchange
    if cloud3x==-200:
        cloud3x=800
        cloud3y=random.randint(40,540)
    showcloud(cloud3,cloud3x,cloud3y)

    playerY += playerYchange
    if playerY <= 10:
        playerY = 10
    elif playerY >= 550:
        playerY = 550
    player(playerX, playerY)

    enemy1x -= enemyxchange
    if enemy1x<0:
        enemy1x = 800
        enemy1y= random.randint(50,550)
    showenemy(enemy1img,enemy1x,enemy1y)


    enemy2x -= enemyxchange
    if enemy2x<0:
        enemy2x = 800
        enemy2y= random.randint(50,550)
    showenemy(enemy2img,enemy2x,enemy2y)


    enemy3x -= enemyxchange
    if enemy3x<0:
        enemy3x = 800
        enemy3y= random.randint(50,550)
    showenemy(enemy3img,enemy3x,enemy3y)

    # Bullet Movement
    if bulletX > 800:
        bulletX = 20
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletX += bulletX_change

    collision = isCollision(enemy1x, enemy1y, bulletX, bulletY)
    if collision:
        score_value += 1
        enemy1y = random.randint(50, 550)
        enemy1x=850

    collision = isCollision(enemy2x, enemy2y, bulletX, bulletY)
    if collision:
        score_value += 1
        enemy2y= random.randint(50,550)
        enemy2x = 850

    collision = isCollision(enemy3x, enemy3y, bulletX, bulletY)
    if collision:
        score_value += 1
        enemy3y= random.randint(50,550)
        enemy3x = 850

    collision = isCollision(enemy1x-50, enemy1y, playerX+50, playerY)
    if collision:
        running=game_over_text()


    collision = isCollision(enemy2x-50, enemy2y, playerX+50, playerY)
    if collision:
        running=game_over_text()

    collision = isCollision(enemy3x-50, enemy3y, playerX+50, playerY)
    if collision:
        running=game_over_text()


    show_score(textX, testY)
    pygame.display.update()