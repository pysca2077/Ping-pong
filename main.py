from pygame import *

main_win = display.set_mode((700, 500))
main_win.fill((39, 10, 31))
clock = time.Clock()

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(40)
