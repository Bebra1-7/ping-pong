from pygame import *
from random import *

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

class Players(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and  self.rect.y > 0:   
            self.rect.y -= self.speed
        if keys[K_s] and  self.rect.y < 700:   
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and  self.rect.y > 0:   
            self.rect.y -= self.speed
        if keys[K_DOWN] and  self.rect.y < 700:   
            self.rect.y += self.speed


def randomchik():
    number = randint(200, 600)
    if number % 2 == 0:
        number += 1
    return number

player_left = Players('player_left.png', 10, 75, 450, 25, 200)

player_right = Players('player_right.png', 10, 1400, 450, 25, 200)

apple = GameSprite('black.png', 1, 550, randomchik(), 50, 50)

window = display.set_mode((1500, 900))
display.set_caption('PingPong')
pole = transform.scale(image.load('pole.png'), (1500, 900))

clock = time.Clock()
FPS = 60

'''mixer.music.load('space.ogg')
mixer.music.play()'''

'''fire = mixer.Sound('fire.ogg')
fire.play'''

'''sprite.collide_rect(player, enemy)'''

font = font.SysFont('Arial', 45)
b_enemy = font.render(f'Выйграно: 0', True, (41, 0, 176))
s_enemy = font.render(f'Выйграно: 0', True, (41, 0, 176))

speed_x = 3
speed_y =3

game = True
finish = True

while game:
    
    for i in event.get():
            if i.type == QUIT:
                game = False

    if finish:
        window.blit(pole, (0, 0))
        GameSprite.reset(player_left)
        GameSprite.reset(player_right)
        GameSprite.reset(apple)

        apple.rect.x += speed_x
        apple.rect.y += speed_y

        if apple.rect.y > 850 or apple.rect.y < 0:
            speed_y *= -1
        
        if apple.rect.x > 1450 or apple.rect.x < 0 or sprite.collide_rect(player_right, apple) or sprite.collide_rect(player_left, apple):
            speed_x *= -1

        player_left.update_left()
        player_right.update_right()

        clock.tick(FPS)
        display.update()