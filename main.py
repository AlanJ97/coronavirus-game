# MODULOS   
import sys, pygame
from pygame.locals import *

# Constantes 
WIDTH = 736
HEIGHT = 500

# Clases  
class Gatell(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("assets/gatell.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2 
        self.rect.centery = ( HEIGHT ) - 100
        self.speed = [0.5, -0.5]
       
    def actualizar(self, keys):               
        #UP
        if keys[pygame.K_a] and self.rect.centerx > 0:    
           self.rect.centerx  -= 2
        #DOWN
        if keys[pygame.K_d] and self.rect.centerx < HEIGHT:
            self.rect.centerx  += 2
        #LEFT
        if keys[pygame.K_w]:
            self.rect.centery -= 2
        #RIGHT
        if keys[pygame.K_s]:
            self.rect.centery += 2
        print("Posición es =  x: "+ str( self.rect.centerx) + " y: "+str( self.rect.centery ))
# Funciones
def load_image(filename, transparent=False):
    try: 
        image = pygame.image.load(filename)
    except pygame.error as message:
        print (message)
        raise SystemExit
               
    image = image.convert()
    if transparent:
            color = image.get_at((0,0))
            image.set_colorkey(color, RLEACCEL)
    return image

# Ejecutar el programa 

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Coronavirus Game. Starring: Dr. Gatell")
    
    background_image = load_image('assets/mexico.png', False)
    drGatell = Gatell()
    
    clock = pygame.time.Clock()
    while True:
        time = clock.tick(60)
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        keys = pygame.key.get_pressed()
        
        drGatell.actualizar(keys)
      
        screen.blit(background_image, (0, 0))
        screen.blit(drGatell.image, drGatell.rect)
        
       ## pygame.display.flip()
        pygame.display.update()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()