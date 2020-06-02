# MODULOS   
import sys, pygame
from  time import sleep
from pygame.locals import *

# Constantes 
WIDTH = 736
HEIGHT = 500
viruses = []
recorridoY = ["Down"]
recorridoX = ["Right"]
image_virus = "assets/coronavirus.png"
image_jabon = "assets/jabon.png"

# Clases  
#Clase del presonaje principal
class Gatell(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("assets/gatell.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2 
        self.rect.centery = ( HEIGHT ) - 100
    
    #Mover al personaje principal
    def actualizar(self, keys):               
        
        #Left     
        if self.rect.left  <= WIDTH and self.rect.left  >= 0   and keys[pygame.K_a]:
           self.rect.centerx  -= 3

        #Right       
        if self.rect.right >= 0 and self.rect.right <= WIDTH  and keys[pygame.K_d]:
            self.rect.centerx  += 3

        #UP       
        if self.rect.top >= 0 and keys[pygame.K_w]:
            self.rect.centery -= 3

        #Down
        if self.rect.bottom  <= HEIGHT and keys[pygame.K_s]:
            self.rect.centery += 3                

#Clase de los enemigos del personaje
class Coronavirus(pygame.sprite.Sprite):
    def __init__(self, image_virus, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image_virus, True)
        self.rect = self.image.get_rect()                 
        self.rect.centerx = x
        self.rect.centery = self.image.get_height()
               
    #Mover al enemigo    
    def mover_ememigo(self):
        if recorridoY[0] == "Down":  
            self.rect.centery += 2 
            if self.rect.bottom >= (HEIGHT - int(self.image.get_height()) +5) and self.rect.bottom <= (HEIGHT - int(self.image.get_height()) +5):                
                recorridoY.pop()
                recorridoY.append("Up")
        else:            
            self.rect.centery -= 2
            if self.rect.top >= -3 and self.rect.top <= 3:
                recorridoY.pop()
                recorridoY.append("Down")
        if recorridoX[0] == "Right":
            self.rect.centerx += 2
            if self.rect.right >= WIDTH -3 and self.rect.right <= WIDTH +3:
                recorridoX.pop()
                recorridoX.append("Left")
        else:
            self.rect.centerx -= 2
            if self.rect.left >= -3 and self.rect.left <= 3:
                recorridoX.pop()
                recorridoX.append("Right")

#Clase de las armas del personaje principal
class Jabon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image_jabon, True)
        self.rect = self.image.get_rect()                 
        self.rect.centerx = 100
        self.rect.centery = self.image.get_height()
                                  
# Funciones principales
#carga la imagen de fondo
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

    # Instanciamos las clases de los objetos en pantalla
    drGatell = Gatell()
    for i in range(0,1):    
        location = i * 80 + 100
        coronavirus  = Coronavirus(image_virus, location)
        viruses.append(coronavirus)   
    jabon  = Jabon()   
    clock = pygame.time.Clock()
    
    #Ciclo que mantiene abierta la ventana hasta que se decide cerrar
    while True:
        time = clock.tick(60)
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        
        #Se obtienen las teclas presionadas
        keys = pygame.key.get_pressed()        
        drGatell.actualizar(keys)
        coronavirus.mover_ememigo()
        #Se agregan los objetos a la pantalla
        screen.blit(background_image, (0, 0))
        screen.blit(drGatell.image, drGatell.rect)
        for virus in viruses:
            screen.blit(virus.image, virus.rect)
        screen.blit(jabon.image, jabon.rect)
      
               
        pygame.display.update()
    return 0
 
# Llamada a la funcion que inicia e programa
if __name__ == '__main__':
    pygame.init()
    main()