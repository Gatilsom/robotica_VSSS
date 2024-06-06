# ======================================================================================================================
#   BIBLIOTECAS
# ======================================================================================================================
import pygame as pg
from pygame.locals import *
from sys import exit
import numpy as np
from random import randint
from time import time
from field_vsss import *
from vsss_tools import *

# ======================================================================================================================
#   CONSTANTES GLOBAIS
# ======================================================================================================================
robot_length = 0.075  # dimensão do robô cúbico [m]
team_a_points = 0  # gols marcados pelo time A
team_b_points = 0  # gols marcados pelo time B
frame_rate = 15  # taxa de frames por segundo
ball_radius = 42.7 / 2000  # raio da bola [m]
play_time = time()
initial_position = [200, 200]


# ======================================================================================================================
#   FUNÇÔES E CLASSES
# ======================================================================================================================

def event_handling():
    global team_a_points, team_b_points
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                team_a_points += 1
            if event.button == 3:
                team_b_points += 1
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
angle = 0

# poly = [[100, 100], [100, 200], [200, 200], [200, 100]]

poly = [[initial_position[0], initial_position[1]],
        [initial_position[0], initial_position[1] + length2pixel(robot_length)],
        [initial_position[0] + length2pixel(robot_length), initial_position[1] + length2pixel(robot_length)],
        [initial_position[0] + length2pixel(robot_length), initial_position[1]]]


poly_ref = [[initial_position[0], initial_position[1]],
        [initial_position[0], initial_position[1] + length2pixel(robot_length)],
        [initial_position[0] + length2pixel(robot_length), initial_position[1] + length2pixel(robot_length)],
        [initial_position[0] + length2pixel(robot_length), initial_position[1]]]

angle = np.deg2rad(0)

#poly = rotate_polygon(poly, angle)



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


    angle += 0.01
    poly = move_polygon(poly, x=0.005, y=0.005, angle=angle)

    pg.draw.polygon(field_screen, "red", poly_ref)
    pg.draw.polygon(field_screen, "green", poly)

    field_screen.blit(text_time, (125 + length2pixel(field_length), length2pixel(field_width / 2) + 150))
    field_screen.blit(text_score, (100 + length2pixel(field_length), length2pixel(field_width / 2) - 100))
    field_screen.blit(text_goals_a, (75 + length2pixel(field_length), length2pixel(field_width / 2) - 50))
    field_screen.blit(text_goals_b, (75 + length2pixel(field_length), length2pixel(field_width / 2)))

    pg.display.update()
