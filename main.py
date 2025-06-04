# shooter.pygame

from pygame import *
from random import randint 
init()

ANCHO, ALTO = 753, 553
PANTALLA_IMG = 'galaxy.jpg'
PLAYER_IMG = 'nave1.png'
UFO_IMG  = 'ufo1.png'
BULLET_IMG ='bullet.png'
GAMER_OVER = 'gameover.jpg'
VICTORIA = 'victoria.jpg'
COLOR = (23 , 5, 135)
TEXTO = (250 , 230,245)
WT = (255, 255, 255)
BK = (0, 0, 0)
ASTEROIDES = 'meteorito.jpg'
# ¡Crea tu propio juego de disparos!

screen = display.set_mode((ANCHO, ALTO))
display.set_caption('Shooter') 
fondo = transform.scale(image.load(PANTALLA_IMG),(ANCHO , ALTO))

font.init()
font_1 = font.SysFont('arial', 40)
font_2 = font.SysFont('arial',30)

misses = 0
poins = 0
vidas = 5

# mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play ()

class GameSprite(sprite.Sprite):
    def __init__(self,img ,cor_x, cor_y, width, height , speed=0):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(img),(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.x = cor_x
        self.rect.y = cor_y
        self.speed = speed


    def reset(self):
        pantalla.blit(self.image, (self.rect.x , self.rect.y))

class Player(GameSprite):
    def update(self):
        llaves = key.get_pressed()
        if llaves[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed

        if llaves[K_d] and self.rect.x < ANCHO - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(BULLET_IMG, self.rect.centerx, self.rect.top , 20 , 35, 5 )
        balas.add(bullet)

class Enemigo(GameSprite):
    def update(self):
        global misses
        self.rect.y += self.speed 
        if self.rect.y >= ALTO :
            misses  +=1
            self.rect.y = -100
            self.rect.x = randint(0, ANCHO - 100)
            self.speed = randint(1, 4)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.x <= 0:
            self.kill()

            
pantalla = display.set_mode((ANCHO, ALTO))



player = Player(PLAYER_IMG, ANCHO//2, ALTO-100, 100, 100, 10)
balas = sprite.Group()

aliens = sprite.Group()
for i in range (1,7):
    enemy = Enemigo(UFO_IMG, randint(0,ANCHO - 100), -100 , 100 ,100 ,randint(1, 4))
    aliens.add(enemy)


asteroides = sprite.Group()
for i in range(4):
    asteroide = Enemigo(ASTEROIDES, randint(0,ANCHO - 100), -100 , 100 ,100 ,randint(1, 4))
    asteroides.add(asteroide)

clok = time.Clock()
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False 
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()

        if e.type == KEYDOWN and finish == True :
            if e.key == K_r:
                finish = False
                poins = 0 
                misses = 0
                vidas = 5

            
    if not finish:
        screen.fill(COLOR)
        screen.blit(fondo , (0,0))
        poins_tex = font_1.render(f'Poins: {poins}', True, TEXTO)
        screen.blit(poins_tex,(30 ,30))
        misses_tex = font_1.render(f'Misses: {misses}', True, TEXTO)
        screen.blit(misses_tex,(30 ,80))
        vidas_tex = font_2.render(f'Vidas: {vidas}', True, TEXTO)
        screen.blit(vidas_tex,(ANCHO - 100, 70 ))
        
        player.reset()
        player.update()
        aliens.draw(screen)
        aliens.update()
        balas.draw(screen)
        balas.update()
        asteroides.draw(screen)
        asteroides.update()

        eliminacion =  sprite.groupcollide(aliens, balas , True ,True)
        for colision in eliminacion:
            poins +=1
            enemy = Enemigo(UFO_IMG, randint(0,ANCHO - 100), -100 , 100 ,100 ,randint(1, 10))
            aliens.add(enemy)

        if sprite.spritecollide(player, aliens, True):
            enemy = Enemigo(UFO_IMG, randint(0,ANCHO - 100), -100 , 100 ,100 ,randint(1, 10))
            aliens.add(enemy)
            vidas -= 1


        if misses == 10 or  vidas == 0:
            finish = True   
            pantalla.fill(BK)
            gamer_over = transform.scale(image.load(GAMER_OVER), (ANCHO, ALTO))

            screen.blit(gamer_over, (0,0))

        
        if poins == 50:
            victoria = transform.scale(image.load(VICTORIA), (ANCHO, ALTO))
            screen.blit(victoria,(0,0))
            finish = True

    display.update()


      






    clok.tick(60)

quit()
