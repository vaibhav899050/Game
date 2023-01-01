import pygame
import os
pygame.font.init()


healthfont = pygame.font.SysFont('comicsans', 40)
WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("First game")
white = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

fps = 60
vel = 5
w1, h1 = 55, 40
yellowhit = pygame.USEREVENT+1
redhit = pygame.USEREVENT+2

maxbullets = 3
bullet_vel = 4

ybullets =[]
rbullets = []


BORDER = pygame.Rect(WIDTH//2-5, 0, 10, 500)
bg = pygame.image.load(os.path.join('Assets', 'space.png'))
bgnew = pygame.transform.scale(bg, (900, 500))
spaceship1 = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
spaceship2 = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
resizeship1 = pygame.transform.rotate(pygame.transform.scale(spaceship1, (w1, h1)), 90)
resizeship2 = pygame.transform.rotate(pygame.transform.scale(spaceship2, (w1, h1)), -90)
def draw_window(red, yellow, redbullets, yellowbullets, r_health, y_health):
    WIN.fill(white)
    
    WIN.blit(bgnew, (0, 0))
    rhealthtxt = healthfont.render("Health: "+ str(r_health), 1, white) 
    yhealthtxt = healthfont.render("Health: "+ str(y_health), 1, white) 
    WIN.blit(rhealthtxt, (WIDTH-rhealthtxt.get_width() -10, 10))
    WIN.blit(yhealthtxt, (10, 10))
    pygame.draw.rect(WIN, white, BORDER)
    WIN.blit(resizeship1, (yellow.x, yellow.y))
    WIN.blit(resizeship2, (red.x, red.y))


    for bullets in redbullets:
        pygame.draw.rect(WIN, RED, bullets)
    for bullets in yellowbullets:
        pygame.draw.rect(WIN, YELLOW, bullets)
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

def bullets(ybullets, rbullets, yellow, red):
    for bullet in ybullets:
        bullet.x+=bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(redhit))
            ybullets.remove(bullet)
    for bullet in rbullets:
        bullet.x-=bullet_vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellowhit))
            rbullets.remove(bullet)




def main():
    yhealth = 10
    rhealth = 10
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
                    bullet = pygame.Rect(yellow.x+yellow.width, yellow.y+yellow.height//2-2, 10, 5)
                    ybullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(rbullets)<maxbullets:
                    bullet = pygame.Rect(red.x, red.y+red.height//2-2, 10, 5)
                    rbullets.append(bullet)

            if event.type == redhit:
                rhealth-=1
            if event.type == yellowhit:
                yhealth-=1
            winnertext = ""
            if yhealth <= 0:
                winnertext = "Red Wins"
            if rhealth <= 0:
                winnertext = "Yellow Wins"
            if winnertext!="":
                pass
        


            



        keys_pressed = pygame.key.get_pressed()
        yellowmov(keys_pressed, yellow)
        redmov(keys_pressed, red)
        bullets(ybullets, rbullets, yellow, red)
        
        draw_window(red, yellow, rbullets, ybullets, rhealth, yhealth)
    pygame.quit

if __name__ == "__main__":
    main()
