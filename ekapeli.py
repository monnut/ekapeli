import pygame
pygame.init()

ikkuna=pygame.display.set_mode((500,500))
pygame.display.set_caption("homejuusto")

x=444
y=243
leveys=40
korkeus=60
nopeus=5

run=True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= nopeus
    if keys[pygame.K_RIGHT]:
        x +=nopeus
    if keys[pygame.K_UP]:
        y -=nopeus
    if keys[pygame.K_DOWN]:
        y +=nopeus

        
    ikkuna.fill((0,0,0))
    pygame.draw.rect(ikkuna,(153,0,0),(x, y,leveys,korkeus))
    pygame.display.update()
    

pygame.quit()
            
        
