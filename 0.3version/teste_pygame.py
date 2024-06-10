# ======================================================================================================================
#   BIBLIOTECAS
# ======================================================================================================================
from sys import exit
from time import time
from robot_vsss import *

# ======================================================================================================================
#   CONSTANTES GLOBAIS
# ======================================================================================================================

team_a_points = 0  # gols marcados pelo time A
team_b_points = 0  # gols marcados pelo time B
frame_rate = 30  # taxa de frames por segundo
ball_radius = 42.7 / 2000  # raio da bola [m]
play_time = time()
initial_position = [0.2, 0.2] # posição inicial [m]
initial_theta = 0.0 # orientação inicial [rad]


# ======================================================================================================================
#   FUNÇÔES E CLASSES
# ======================================================================================================================

def event_handling():
    global team_a_points, team_b_points, rob1
    global delta_move_x, delta_move_y, delta_theta, passo_trans, passo_rotac
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                team_a_points += 1
            if event.button == 3:
                team_b_points += 1
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                delta_move_y += passo_trans
            if event.key == pg.K_DOWN:
                delta_move_y -= passo_trans
            if event.key == pg.K_LEFT:
                delta_move_x -= passo_trans
            if event.key == pg.K_RIGHT:
                delta_move_x += passo_trans
            if event.key == pg.K_q:
                delta_theta += passo_rotac
            if event.key == pg.K_w:
                delta_theta -= passo_rotac
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                delta_move_y = 0.0
            if event.key == pg.K_DOWN:
                delta_move_y = 0.0
            if event.key == pg.K_LEFT:
                delta_move_x = 0.0
            if event.key == pg.K_RIGHT:
                delta_move_x = 0.0
            if event.key == pg.K_q:
                delta_theta = 0.0
            if event.key == pg.K_w:
                delta_theta = 0.0
    return None



# ======================================================================================================================
#   INIT PYGAME
# ======================================================================================================================
pg.init()
field_screen = pg.display.set_mode((length2pixel(field_length) + 50 + 200, length2pixel(field_width) + 50))
pg.display.set_caption("Futebol de Robôs - VSSS")
text_font = pg.font.SysFont("arial", 25, True, True)
clock = pg.time.Clock()
time_reference = time()

rob1 = Robot(shirt=9, team="A", x=0, y=-0, theta=0, color="yellow")
delta_move_x = 0.0
delta_move_y = 0.0
delta_theta = 0.0
passo_trans = 0.01
passo_rotac = np.deg2rad(5)
# ======================================================================================================================
#   GAME LOOP
# ======================================================================================================================
while True:
    clock.tick(frame_rate)
    field_screen.fill((0, 0, 0))
    play_time = time()
    delta_time = play_time - time_reference
    if delta_time > 300:
        pg.quit()
        exit()
    text_score = text_font.render("Score", True, "white")
    text_time = text_font.render("{}".format(int(delta_time)), True, "white")
    text_goals_a = text_font.render("Team A: {}".format(team_a_points), True, "red")
    text_goals_b = text_font.render("Team B: {}".format(team_b_points), True, "blue")

    event_handling()

    draw_field(field_screen, field_length, field_width, color=(255, 100, 255))
    #draw_ball(field_screen, field_length, field_width, ball_radius)

    rob1.move(delta_move_x, delta_move_y, delta_theta)
    rob1.draw(field_screen)


    field_screen.blit(text_time, (125 + length2pixel(field_length), length2pixel(field_width / 2) + 150))
    field_screen.blit(text_score, (100 + length2pixel(field_length), length2pixel(field_width / 2) - 100))
    field_screen.blit(text_goals_a, (75 + length2pixel(field_length), length2pixel(field_width / 2) - 50))
    field_screen.blit(text_goals_b, (75 + length2pixel(field_length), length2pixel(field_width / 2)))

    pg.display.update()
