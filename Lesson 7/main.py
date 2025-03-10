import pygame
import time
import os

pygame.font.init()

WIDTH = 900
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2 Player Space shoter")

WHITE = ( 255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (221, 232, 19)

border = pygame.draw.rect((WIDTH//2 - 5, 0,10,HEIGHT))

HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('comicsans',80)

FPS = 60                    #frames per second
VEL = 5                     #player velocity
BULLET_VEL = 7              #Bullet velocity

MAX_BULLETS = 3
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMG  = pygame.image.load(os.path.join('assets',"yellowship.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMG,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

RED_SPACESHIP_IMG = pygame.image.load(os.path.join('assets',"redship.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMG,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270) 

SPACE_IMG = pygame.image.load(os.path.join('assets',"spacebg.png"))
SPACE = pygame.transform.scale(SPACE_IMG,(WIDTH,HEIGHT))

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    screen.blit(SPACE,(0,0))
    pygame.draw.rect(screen,BLACK,border)

    red_health_text = HEALTH_FONT.render("Health: "+ str(red_health),1,RED)
    screen.blit(red_health_text,(700,10))
    screen.blit(RED_SPACESHIP, (red.x,red.y))
    for bullet in red_bullets:
        pygame.draw.rect(screen,RED,bullet)

    #yellow
    yellow_health_text = HEALTH_FONT.render("Health: "+ str(yellow_health),1,YELLOW)
    screen.blit(yellow_health_text, (20,10))
    screen.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,YELLOW,bullet)
