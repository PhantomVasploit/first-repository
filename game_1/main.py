import pygame
import random
import math

# initialize the pygame
pygame.init()

# screen for the game
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background.png')

# Title and icon
pygame.display.set_caption("The Phenom")

# score value
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)
# player
playerImg = pygame.image.load('spaceship.png')
positionX = 370
positionY = 480
positionX_change = 0

# enemy
enemyImg = []
enemyPositionX = []
enemyPositionY = []
enemyPositionX_change = []
enemyPositionY_change = []
num_of_enemies = int(6)

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien-pixelated-shape-of-a-digital-game.png'))
    enemyPositionX.append(random.randint(0, 735))
    enemyPositionY.append(random.randint(50, 150))
    enemyPositionX_change.append(0.5)
    enemyPositionY_change.append(40)

# bullet
bulletImg = pygame.image.load('bullet (1).png')
bulletPositionX = 0
bulletPositionY = 480
bulletPositionX_change = 0
bulletPositionY_change = 1
bullet_state = 'ready'


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


def is_collision(enemyPositionX, enemyPositionY, bulletPositionX, bulletPositionY):
    distance = math.sqrt(
        (math.pow(enemyPositionX - bulletPositionX, 2)) + (math.pow(enemyPositionY - bulletPositionY, 2)))
    if distance < 27:
        return True
    else:
        return False


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# game loop
running = True
while running:
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check if left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                positionX_change -= 1
        # if keystroke is pressed check if right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                positionX_change = 1
            # fire bullet using spacebar key
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletPositionX = positionX
                    fire_bullet(bulletPositionX, bulletPositionY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                positionX_change = 0
    # spaceship movement and boundary
    positionX += positionX_change

    if positionX <= 0:
        positionX = 0
    elif positionX >= 736:
        positionX = 736
    # enemy movement and boundary
    for i in range(num_of_enemies):

        # game over
        if enemyPositionY[i] > 440:
            for j in range(num_of_enemies):
                enemyPositionY[j] = 2000
            game_over_text()
            break

        enemyPositionX[i] += enemyPositionX_change[i]

    if enemyPositionX[i] <= 0:
        enemyPositionX_change[i] = .5
        enemyPositionY[i] += enemyPositionY_change[i]
    elif enemyPositionX[i] >= 736:
        enemyPositionX_change[i] -= .5
        enemyPositionY[i] += enemyPositionY_change[i]
    # collision
    collision = is_collision(enemyPositionX[i], enemyPositionY[i], bulletPositionX, bulletPositionY)
    if collision:
        bulletPositionY = 480
        bullet_state = 'ready'
        score_value += 1
        enemyPositionX[i] = random.randint(0, 735)
        enemyPositionY[i] = random.randint(50, 150)
    enemy(enemyPositionX[i], enemyPositionY[i], i)

    # bullet movement
    if bulletPositionY <= 0:
        bulletPositionY = 480
        bullet_state = 'ready'
    if bullet_state == "fire":
        fire_bullet(bulletPositionX, bulletPositionY)
        bulletPositionY -= bulletPositionY_change

    player(positionX, positionY)
    show_score(textX, textY)
    pygame.display.update()
