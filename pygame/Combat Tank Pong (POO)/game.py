from arena import draw_arena
from tank import *
from config import *

pygame.init()

# font
font = pygame.font.Font('assets/PressStart2P.ttf', 45)

# hud
hud1_text = font.render("3", True, green)
hud2_text = font.render("3", True, red)
hud1_text_rect = hud1_text.get_rect()
hud2_text_rect = hud2_text.get_rect()
hud1_text_rect.center = (250, 50)
hud2_text_rect.center = (650, 50)
score1 = 3
score2 = 3

# sounds
shoot_sound = pygame.mixer.Sound("assets/tiger.wav")
tank_explode = pygame.mixer.Sound("assets/tank_explode.wav")
bounce_ball = pygame.mixer.Sound("assets/bounce_ball.wav")
tank_walk = pygame.mixer.Sound("assets/tank_walk.wav")
time_sound = tank_walk.get_length()
time_stop = 0

# screen
size = (900, 650)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("combat tank")

# projectile speed
speed_ball_x = 0
speed_ball_y = 0

tank = tank_player(pygame.image.load("assets/tank1.png"), 1, spawn_x_tank_1, spawn_y_tank_1)


clock = pygame.time.Clock()

loop = True
recharge = False
no_animation = True
stop = False
victory1 = False
victory2 = False
time = 0

if stage_select == 0:

    background = pygame.image.load("assets/city_map.png")
    background.get_rect().center = (0, 0)
    screen.blit(background, background.get_rect())

else:

    background = pygame.image.load("assets/vegetation_map.png")
    background.get_rect().center = (0, 0)
    screen.blit(background, background.get_rect())

list_of_obstacles = draw_arena(screen, white, stage_select)

while loop:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            loop = False

        # configuring game keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                tank.set_forward(True)
            if event.key == pygame.K_RIGHT:
                tank.set_turn_right(True)
            if event.key == pygame.K_LEFT:
                tank.set_turn_left(True)
            if event.key == pygame.K_l and (not tank.set_reloading(True)):
                tank.set_fire(True)
                tank.set_reloading(True)
                tank.set_reload_time(pygame.time.get_ticks())

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                tank.set_forward(False)
            if event.key == pygame.K_RIGHT:
                tank.set_turn_right(False)
            if event.key == pygame.K_LEFT:
                tank.set_turn_left(False)

    time = pygame.time.get_ticks()
    screen.blit(background, background.get_rect())

    if no_animation and not victory1 and not victory2:
        if tank.get_forward() or (tank.get_turn_right() and tank.get_turn_left()):
            tank.set_turn_right(False)
            tank.set_turn_left(False)

        if tank.get_forward():
            tank.set_current_x(tank.get_current_x()+tank.get_speed()[0])
            tank.set_current_y(tank.get_current_y()+tank.get_speed()[1])

            if time - time_stop > time_sound * 1000:
                tank_walk.play()
                time_stop = pygame.time.get_ticks()

        if tank.get_turn_right():
            tank.set_angle(tank.get_angle()-1)
            if tank.get_angle() <= -360:
                tank.set_angle(0)
            tank.set_asset(pygame.transform.rotate(tank.get_surface(), tank.get_angle()))
            tank.set_speed(tank.get_speed().rotate(1))
        if tank.get_turn_left():
            tank.set_angle(tank.get_angle()+1)
            if tank.get_angle() >= 360:
                tank.set_angle(0)
            tank.set_asset(pygame.transform.rotate(tank.get_surface(), tank.get_angle()))
            tank.set_speed(tank.get_speed().rotate(-1))

        if time - tank.get_reload_time() > time_limit:
            tank.set_reloading(False)

        tank.set_rect_center(tank.get_current_x(), tank.get_current_y())
        screen.blit(tank.get_asset(), tank.get_rect())

    pygame.display.update()
    clock.tick(60)

pygame.quit()
