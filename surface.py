
import pygame
import random
import pygame.camera
from pygame.locals import*
pygame.init()
 

black = [  0,  0,  0]
white = [255,255,255]
blue =  [  0,  0,255]
green = [  0,255,  0]
red =   [255,  0,  0]
 

 

size=[500,500]
screen=pygame.display.set_mode(size)
  

done=False
clock = pygame.time.Clock()
 
while done==False:
 
    clock.tick(10)
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True  
       
    screen.fill(white)
 
     
    
    pygame.draw.line(screen,black,[100,350],[140,200],5)
    pygame.draw.line(screen,black,[140,200],[300,200],5)
    pygame.draw.line(screen,black,[300,200],[400,300],5)
    pygame.draw.line(screen,black,[400,300],[300,400],5)
    pygame.draw.line(screen,black,[300,400],[100,350],5)
 
    pygame.display.flip()

    #surf3d = pygame.surfarray.pixel3d(screen)
   # surf3d[100][100]

    while done == False:
      x = random.randint(100, 350)
      y = random.randint(100, 350)
      #ed = random.randint(0, 255)
     # green = random.randint(0, 255)
      #blue = random.randint(0, 255)
      
      screen.set_at((x, y),red)    
 
      pygame.display.flip()


pygame.quit ()

