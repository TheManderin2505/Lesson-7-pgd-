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

BORDER = pygame.draw.rect((WIDTH//2 - 5, 0,10,HEIGHT))

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
    pygame.draw.rect(screen,BLACK,BORDER)

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

    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
        yellow.x -= VEL
    
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #right
        yellow.x += VEL

    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
        yellow.y -= VEL

    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: #down
        yellow.y += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #left
        red.x -= VEL

    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #right
        red.x += VEL
    
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #UP
        red.y -= VEL

    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: #down
        red.y += VEL

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)

        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text,1,WHITE)
    screen.blit(draw_text,(WIDTH / 2 - draw_text.get_width()/2,HEIGHT / 2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
    