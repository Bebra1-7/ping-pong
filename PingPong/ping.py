from pygame import *




class Wall(sprite.Sprite):
    def __init__(self,  color_1, color_2, color_3, wall_width, wall_height, wall_x, wall_y):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color_1, self.color_2, self.color_3))
        self.rect = self.image.get_rect()
        self.rect.x= wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Players(Wall):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and  self.rect.y < 900:   
            self.rect.y += 5
        if keys[K_s] and  self.rect.y > 0:   
            self.rect.y -= 5

player_left = Players(0, 0, 200, 50, 150, 100, 450)

window = display.set_mode((1500, 900))
display.set_caption('PingPong')
pole = transform.scale(image.load('pole.png'), (1500, 900))

clock = time.Clock()
FPS = 60

'''mixer.music.load('space.ogg')
mixer.music.play()'''

'''fire = mixer.Sound('fire.ogg')
fire.play'''



'''font = font.SysFont('Arial', 45)
b_enemy = font.render(f'Счёт: {break_enemy}', True, (41, 0, 176))
s_enemy = font.render(f'Пропущено: {skipped_enemy}', True, (41, 0, 176))'''

game = True
finish = True

while game:
    
    for i in event.get():
            if i.type == QUIT:
                game = False

    if finish:
        window.blit(pole, (0, 0))
        player_left.update()


        clock.tick(FPS)
        display.update()