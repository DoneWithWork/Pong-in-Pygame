import random
import sys
import pygame

# Sounds
pygame.mixer.init()
pygame.mixer.music.load("Bonk.mp3")
pygame.mixer.music.set_volume(0.2)

# Default Pygame Window Setup
pygame.init()
width = 1050
height = 650
screen = pygame.display.set_mode((width, height))
icon = pygame.image.load("Art/IconPong.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Pong in Pygame")
clock = pygame.time.Clock()

# Colours
white = (250, 250, 250)
black = (0, 0, 0)

# Booleans
runMain = False
run = True

# Scores
score1 = 0
score2 = 0

# Setting Up fonts for texts
font = pygame.font.Font(None, 70)
MenuFont = pygame.font.Font(None, 100)

# Player 1
Player1 = pygame.image.load("Art/WhiteTile.png").convert_alpha()
Player1 = pygame.transform.scale(Player1, (30, 130))
Player1_rect = Player1.get_rect(center=(100, 325))

# Player 2
Player2 = pygame.image.load("Art/WhiteTile.png").convert_alpha()
Player2 = pygame.transform.scale(Player2, (30, 130))
Player2_rect = Player2.get_rect(center=(950, 325))

# Ball
Ball = pygame.image.load("Art/WhiteTile.png").convert_alpha()
Ball = pygame.transform.scale(Ball, (30, 30))
Ball_rect = Ball.get_rect()
Ball_rect.x = width / 2 - 10
Ball_rect.y = 325

# Objects
Line = pygame.image.load("Art/WhiteTile.png").convert_alpha()
Line = pygame.transform.scale(Line, (10, 700))
Line_rect = Ball.get_rect()
Line_rect.x = width / 2
Line_rect.y = 0

# Movement of Ball
y = -5
x = 5


# Resetting the positions of the ball and players. Also sending ball into another direction
def resetPos():
    global y, x
    posY = random.randint(1, 2)
    if posY == 1:
        y = -5
    if posY == 2:
        y = 5
    posX = random.randint(1, 2)
    if posX == 1:
        x = -5
    if posX == 2:
        x = 5
    Player1_rect.center = (100, 325)
    Player2_rect.center = (950, 325)
    Ball_rect.x = width / 2 - 10
    Ball_rect.y = 325


# Ball Movement and collisions
def MoveBall():
    global y
    global x
    global score1, score2

    Ball_rect.y += y
    Ball_rect.x += x
    if Ball_rect.top <= 0 or Ball_rect.bottom >= height:
        pygame.mixer.music.play()
        y *= -1
    if Ball_rect.left <= 0 or Ball_rect.right >= width:
        pygame.mixer.music.play()
        x *= -1
    if Ball_rect.colliderect(Player1_rect) or Ball_rect.colliderect(Player2_rect):
        pygame.mixer.music.play()
        x *= -1
    if Ball_rect.x <= 0:
        print("Player 2 Scored")
        score2 += 1

        resetPos()
    if Ball_rect.right >= width:
        print("Player 1 scored")

        score1 += 1

        resetPos()


# Putting all objects onto screen and calling the MoveBall() function
def main():
    screen.fill(black)
    screen.blit(Line, Line_rect)
    screen.blit(Ball, Ball_rect)
    screen.blit(Player1, Player1_rect)
    screen.blit(Player2, Player2_rect)
    text = font.render(f'{score1}', True, white)
    text2 = font.render(f"{score2}", True, white)
    screen.blit(text, (400, 50))
    screen.blit(text2, (630, 50))
    MoveBall()


# Simple menu UI
def menu():
    screen.fill(black)
    MenuText = MenuFont.render("Pong Made in Pygame", True, white)
    MenuText2 = font.render("Press the letter P to play", True, white)
    MenuText2_rect = MenuText2.get_rect(center=(width / 2, 250))
    MenuText_rect = MenuText.get_rect(center=(width / 2, 150))
    screen.blit(MenuText, MenuText_rect)
    screen.blit(MenuText2, MenuText2_rect)


def KeyInput():
    global runMain
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and Player1_rect.y >= 0:
        Player1_rect.y -= 5
    if keys[pygame.K_s] and Player1_rect.y <= 515:
        Player1_rect.y += 5
    if keys[pygame.K_UP] and Player2_rect.y >= 0:
        Player2_rect.y -= 5
    if keys[pygame.K_DOWN] and Player2_rect.y <= 515:
        Player2_rect.y += 5
    if keys[pygame.K_p]:
        runMain = True


# Simple while loop
while run:
    for event in pygame.event.get():  # Getting all user inputs
        if event.type == pygame.QUIT:  # If the user clicks the X button to exit the window
            run = False  # Run is set to False, which ends the while loop
            pygame.quit()  # Deactivates Pygame libraries and closes window
            sys.exit()  # Stops programme from running

    # Running main() function
    menu()

    # Checking for input from user
    KeyInput()

    # When runMain is true, run main()
    if runMain:
        main()

    clock.tick(60)
    pygame.display.update()
