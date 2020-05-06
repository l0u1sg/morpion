import pygame
(width, height) = (600, 700)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption('Morpion game')
screen.fill((0, 0, 0))
background = pygame.image.load('morpion.png')
screen.blit(background, (0, 0))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
