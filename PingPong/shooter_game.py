#Создай собственный Шутер!
from pygame import *
from random import *

mixer.init()

font.init()


class GameSprite(sprite.Sprite):
    def __init__(self, file_image, sprite_speed, x, y, width_x, height_y):
        super().__init__()
        self.image = transform.scale(image.load(file_image), (width_x, height_y))
        self.speed = sprite_speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and  self.rect.x <945:   
            self.rect.x += self.speed
        if keys[K_a] and  self.rect.x > 0:   
            self.rect.x -= self.speed
    def fire(self):
        bullet = Bullet('bullet.png', 5, self.rect.centerx, self.rect.top, 15, 20)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        global skipped_enemy
        if self.rect.y <= 800:
            self.rect.y += self.speed

        if self.rect.y >= 800:
            self.rect.y = 0
            self.rect.x = randint(65, 910)
            self.speed = randint(2, 3)
            skipped_enemy += 1
            return skipped_enemy
        
class Asteroid(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= 1100:
            self.rect.x = 0
            self.rect.y = randint(150, 500)
            self.speed = randint(2,3)

class Bullet(GameSprite):
    def update(self):
        if self.rect.y <= 0:
            self.kill()
        self.rect.y -= self.speed


player = Player('rocket.png', 5, 500, 550, 50, 75)
bullets = sprite.Group()
monsters = sprite.Group()
for i in range(5):
    enemy = Enemy('ufo.png', randint(2,3), randint(65, 1000), 0, 65, 40)
    monsters.add(enemy)

asteroids = sprite.Group()
for i in range(3):
    asteroid = Asteroid('asteroid.png', randint(2,4), 0, randint(150, 500), randint(50, 70), randint(50, 70))
    asteroids.add(asteroid)


window = display.set_mode((1000, 700))
display.set_caption('Шутер')
galaxy = transform.scale(image.load('galaxy.jpg'), (1000, 700))

clock = time.Clock()
FPS = 60

mixer.music.load('space.ogg')
mixer.music.play()

fire = mixer.Sound('fire.ogg')
'''fire.play'''

break_enemy = 0
skipped_enemy = 0

font = font.SysFont('Arial', 45)
'''b_enemy = font.render(f'Счёт: {break_enemy}', True, (41, 0, 176))
s_enemy = font.render(f'Пропущено: {skipped_enemy}', True, (41, 0, 176))'''

game = True
finish = True
win = font.render('YOU WIN', True, (0, 255, 0))
lose = font.render('YOU LOSE', True, (0, 255, 0))

while game:
    
    for i in event.get():
            if i.type == QUIT:
                game = False
            elif i.type == KEYDOWN:
                if i.key == K_SPACE:
                    player.fire()

    if finish:

        sprites_list = sprite.groupcollide(monsters, bullets, True, True)
        for i in sprites_list:
            break_enemy += 1
            enemy = Enemy('ufo.png', randint(2,3), randint(65, 1000), 0, 65, 40)
            monsters.add(enemy)

        sprite_list = sprite.groupcollide(asteroids, bullets, True, True)
        for i in sprite_list:
            asteroid = Asteroid('asteroid.png', randint(2,4), 0, randint(150, 500), randint(50, 70), randint(50, 70))
            asteroids.add(asteroid)

        ufo_list = sprite.groupcollide(monsters, asteroids, True, True)
        for i in ufo_list:
            enemy = Enemy('ufo.png', randint(2,3), randint(65, 1000), 0, 65, 40)
            monsters.add(enemy)

            asteroid = Asteroid('asteroid.png', randint(2,4), 0, randint(150, 500), randint(50, 70), randint(50, 70))
            asteroids.add(asteroid)
         

        b_enemy = font.render(f'Счёт: {break_enemy}', True, (41, 0, 176))
        s_enemy = font.render(f'Пропущено: {skipped_enemy}', True, (41, 0, 176))

        player.update()
        monsters.update()
        bullets.update()
        asteroids.update()

        window.blit(galaxy, (0,0))
        window.blit(b_enemy, (0,0))
        window.blit(s_enemy, (0,30))

        GameSprite.reset(player)
        
        monsters.draw(window)
        bullets.draw(window)
        asteroids.draw(window)


        if break_enemy >= 10:
            window.blit(win, (500, 350))
            finish = False
        elif skipped_enemy > 3 or sprite.spritecollide(player, monsters, False):
            window.blit(lose, (500, 350))
            finish = False


    clock.tick(FPS)
    display.update()