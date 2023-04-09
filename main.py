from pygame import *

class Game_Sprate(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height ):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(wight, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

class Player(Game_Sprate):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 630:
            self.rect.x += self.speed

main_win = display.set_mode((700, 500))
main_win.fill((39, 10, 31))
clock = time.Clock()
ref_orb = Game_Sprate('refresher.png', 350, 200, 4, 100,100 )

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        ref_orb.reset()
        ref_orb.update()

    display.update()
    clock.tick(40)
