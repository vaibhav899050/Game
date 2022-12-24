import pygame
import os

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("First game")
white = (255, 255, 255)

fps = 60
spaceship1 = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
spaceship2 = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

def draw_window():
    WIN.fill(white)
    WIN.blit(spaceship1, (300, 100))
    pygame.display.update()



def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run  = False
        draw_window()
    pygame.quit

if __name__ == "__main__":
    main()
