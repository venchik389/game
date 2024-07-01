from pygame import*


window = display.set_mode((700,500))

display.set_caption('скидывание жира')

background = image.load('green background.jpg')
background = transform.scale(background,(700,500))

black = transform.scale(image.load('blackpow.png'),(50,50))
red = transform.scale(image.load('fly.png'),(75,75))

black_x,black_y = 100,200
fly_x,fly_y = 500,200

end = 0

game = True

while game:

    window.blit(background,(0,0))
    window.blit(black,(black_x,black_y))
    window.blit(red,(fly_x,fly_y))

    for game_event in event.get():
        print(game_event)
        if game_event.type == QUIT:
                game = False
    keys = key.get_pressed()
    if keys[K_w]:
        fly_y -= 7
    if keys[K_s]:
        fly_y -= -7
    if keys[K_d]:
        fly_x -= -7
    if keys[K_a]:
        fly_x -= 7

    if fly_x < black_x:
        black_x -= 4
    else:
        black_x += 4

    if fly_y < black_y:
        black_y -= 4
    else:
        black_y += 4

    end += 20
    if end > 10000:
        print('тебя не съел black man!')
        game = False

    time.delay(20) 
    display.update()