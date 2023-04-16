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
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += self.speed
    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed

rocket1 = Player('refresher.png', 20, 100, 5, 50, 150)
rocket2 = Player('refresher.png', 630, 100, 5, 50, 150)

main_win = display.set_mode((700, 500))
main_win.fill((39, 10, 31))
clock = time.Clock()
ref_orb = Game_Sprate('refresher.png', 350, 200, 4, 75,75 )

font.init()
font = font.Font(None, 60)
lose_1_igrok = font.render('lose_1_igrok', True, (31,58, 61))
lose_2_igrok = font.render('lose_2_igrok', True, (31, 58, 61))

speed_x = 3
speed_y = 3

game = True
finish = False
while game:


    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        main_win.fill((39, 10, 31))

        rocket1.reset()
        rocket1.update_1()

        rocket2.reset()
        rocket2.update_2()

        ref_orb.rect.x += speed_x
        ref_orb.rect.y += speed_y

        if ref_orb.rect.y < 0 or ref_orb.rect.y >425:
            speed_y *= -1

        if ref_orb.rect.x < 0 :
            finish = True
            main_win.blit(lose_1_igrok, (325, 220))

        if ref_orb.rect.x > 625 :
            finish = True
            main_win.blit(lose_2_igrok, (325, 220))

        if sprite.collide_rect(ref_orb, rocket1) or  sprite.collide_rect(ref_orb, rocket2) :
            speed_x *=-1


        ref_orb.reset()
        ref_orb.update()

    display.update()
    clock.tick(40)
