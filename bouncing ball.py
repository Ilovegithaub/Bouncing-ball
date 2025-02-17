import pygame

pygame.init()
width=800
height=400
speedx, speedy=0.5, 0.5
x,y=100,100

screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Pygame")
running=True


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill("blue")

    x += speedx
    y -= speedy

    if x + 20 > width or x-20 < 0:
        speedx=-speedx

    if y + 20 > height or y-20 < 0:
        speedy=-speedy

    pygame.draw.circle(screen, "Yellow", (x,y), 20)
    pygame.display.flip()
