import pygame
import os

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("First game")
white = (255, 255, 255)

fps = 60
vel = 5
w1, h1 = 55, 40

maxbullets = 3

ybullets =[]
rbullets = []

BORDER = pygame.Rect(WIDTH/2-5, 0, 10, 500)
bg = pygame.image.load(os.path.join('Assets', 'space.png'))
bgnew = pygame.transform.scale(bg, (900, 500))
spaceship1 = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
spaceship2 = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
resizeship1 = pygame.transform.rotate(pygame.transform.scale(spaceship1, (w1, h1)), 90)
resizeship2 = pygame.transform.rotate(pygame.transform.scale(spaceship2, (w1, h1)), -90)
def draw_window(red, yellow):
    WIN.fill(white)
    
    WIN.blit(bgnew, (0, 0))
    pygame.draw.rect(WIN, white, BORDER)
    WIN.blit(resizeship1, (yellow.x, yellow.y))
    WIN.blit(resizeship2, (red.x, red.y))
    pygame.display.update()
def yellowmov(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x>0: #left yellow
        yellow.x-= vel  
    if keys_pressed[pygame.K_d] and yellow.x<WIDTH/2-55: #right yellow
        yellow.x+= vel 
    if keys_pressed[pygame.K_w] and yellow.y>0: #up yellow
        yellow.y-= vel 
    if keys_pressed[pygame.K_s] and yellow.y<500-40: #down yellow
        yellow.y+= vel 
def redmov(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]: #left yellow
        red.x-= vel  
    if keys_pressed[pygame.K_RIGHT]: #right yellow
        red.x+= vel 
    if keys_pressed[pygame.K_UP]: #up yellow
        red.y-= vel 
    if keys_pressed[pygame.K_DOWN]: #down yellow
        red.y+= vel 




def main():
    clock = pygame.time.Clock()
    run = True
    red = pygame.Rect(700, 100, w1, h1)
    yellow = pygame.Rect(300, 100, w1, h1)
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run  = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(ybullets)<maxbullets:
                    bullet = pygame.Rect(yellow.x+yellow.width, yellow.y+yellow.height/2-2, 10, 5)
                    ybullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(rbullets)<maxbullets:
                    bullet = pygame.Rect(red.x, red.y+red.height/2-2, 10, 5)
                    rbullets.append(bullet)


        keys_pressed = pygame.key.get_pressed()
        yellowmov(keys_pressed, yellow)
        redmov(keys_pressed, red)
        
        draw_window(red, yellow)
    pygame.quit

if __name__ == "__main__":
    main()
