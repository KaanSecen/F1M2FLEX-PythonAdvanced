import sys
import pygame
from pygame.locals import *

# Necessary setup before you can start using pygame functionalities:
pygame.init()


KEYS_DOWN = []

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN  = pygame.display.set_mode(SCREEN_SIZE)

CLOCK   = pygame.time.Clock()
FPS     = 30

BG_COLOUR = [246, 166, 247]
IS_RUNNING = True

class player :

    points = 0
    lives = 0
    Speed_Defualt = 5
    Image_Defualt = "../Art/spr_Player2.gif"

    playerSprite = None
    playerRect = None
    playerSpeed = 3

    def __init__(self, referentie = Image_Defualt):
        self.playerSprite = pygame.image.load(referentie)
        self.playerRect = self.playerSprite.get_rect()

    

    def Update(self):
        if (KEYS_DOWN[K_UP]):
            self.playerRect.y -= self.playerSpeed
        elif (KEYS_DOWN[K_DOWN]):
            self.playerRect.y += self.playerSpeed
        if (KEYS_DOWN[K_LEFT]):
            self.playerRect.x -= self.playerSpeed
        elif (KEYS_DOWN[K_RIGHT]):
            self.playerRect.x += self.playerSpeed
        

    
    def draw(self, screenSurface):
        screenSurface.blit(self.playerSprite, self.playerRect)




knightInstance = player()



while IS_RUNNING:


    # ------------------------------------------------
    # INPUT REGISTRATION:
    # ------------------------------------------------
    KEYS_DOWN = pygame.key.get_pressed()


    # ------------------------------------------------
    # EVENT HANDLING:
    # ------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_RUNNING = False


    # ------------------------------------------------
    # UPDATE GAME LOGIC:
    # ------------------------------------------------
    knightInstance.Update()

    # ------------------------------------------------
    # DRAWING INSTRUCTIONS
    # ------------------------------------------------
    # First clear the screen with a background color.
    # If you don't, you'll draw on top of what was previously drawn. See for yourself by removing/commenting this line... :)
    SCREEN.fill(BG_COLOUR)

    knightInstance.draw(SCREEN)


    # Then draw sprites on the current location:
    # Finally refresh the entire screen of this application window:
    pygame.display.flip()


    # Prevent the game from running way too fast by restricting the amount of update cycles made per second.
    # The program basically waits a certain amount of time before it continues.
    # This function converts the desired result, which is expressed in "frames per second", into the exact nanoseconds wait time.
    CLOCK.tick(FPS)


