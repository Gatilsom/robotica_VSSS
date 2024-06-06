
"""
side_lines = pg.draw.lines(screen, color, closed=False,
                           points=[(25, 25 + length2pixel(field_chamfer)),
                                   (25, 25 + length2pixel(field_width - field_chamfer)),
                                   (25 + length2pixel(field_chamfer),
                                    25 + length2pixel(field_width)),
                                   (25 + length2pixel(field_length - field_chamfer),
                                    25 + length2pixel(field_width)),
                                   (25 + length2pixel(field_length),
                                    25 + length2pixel(field_width - field_chamfer)),
                                   (25 + length2pixel(field_length), 25 + length2pixel(field_chamfer)),
                                   (25 + length2pixel(field_length - field_chamfer), 25),
                                   (25 + length2pixel(field_chamfer), 25),
                                   (25, 25 + length2pixel(field_chamfer))
                                   ], width=3)
"""

"""
import pygame as pg
from pygame.locals import *
from sys import exit
import numpy as np

field_length = 1.5  # comprimento do campo [m]
field_width = 1.3  # largura do campo [m]
robot_length = 0.075  # dimensão do robô cúbico [m]
team_a_points = 0 # gols marcados pelo time A
team_b_points = 0 # gols marcados pelo time B
frame_rate = 30 # taxa de frames por segundo


def length2pixel(length):
    scale = 400
    return int(length * scale)


def field_draw(screen, field_length=1.5, field_width=1.3, color=(255, 0, 0)):
    field_chamfer = field_length * 7 / 150
    field_center = field_length * 2 / 15
    side_lines = pg.draw.lines(screen, color, closed=False,
                               points=[(25, 25 + length2pixel(field_chamfer)),
                                       (25, 25 + length2pixel(field_width - field_chamfer)),
                                       (25 + length2pixel(field_chamfer),
                                        25 + length2pixel(field_width)),
                                       (25 + length2pixel(field_length - field_chamfer),
                                        25 + length2pixel(field_width)),
                                       (
                                           25 + length2pixel(field_length),
                                           25 + length2pixel(field_width - field_chamfer)),
                                       (25 + length2pixel(field_length), 25 + length2pixel(field_chamfer)),
                                       (25 + length2pixel(field_length - field_chamfer), 25),
                                       (25 + length2pixel(field_chamfer), 25),
                                       (25, 25 + length2pixel(field_chamfer))
                                       ], width=3)
    center_line = pg.draw.line(screen, color, (25 + length2pixel(field_length / 2), 25),
                               (25 + length2pixel(field_length / 2), 25 + length2pixel(field_width)))

    center_circle = pg.draw.circle(screen, color,
                                   (25 + length2pixel(field_length / 2), 25 + length2pixel(field_width / 2)),
                                   length2pixel(field_center), 1)
    center_field = pg.draw.circle(screen, color,
                                  (25 + length2pixel(field_length / 2), 25 + length2pixel(field_width / 2)),
                                  length2pixel(field_center / 15), 0)

    line = pg.draw.line(screen, (0, 255, 0), (25, 25 + length2pixel(field_width / 2)),
                        (25 + length2pixel(field_length), 25 + length2pixel(field_width / 2)))

    left_area = pg.draw.lines(screen, color, closed=False,
                              points=[(25, 25 + length2pixel(field_width / 2) - length2pixel(field_width * 7 / 26)),
                                      (25 + length2pixel(field_length * 3 / 28),
                                       25 + length2pixel(field_width / 2) - length2pixel(field_width * 7 / 26)),
                                      (25 + length2pixel(field_length * 3 / 28),
                                       25 + length2pixel(field_width / 2) + length2pixel(field_width * 7 / 26)),
                                      (25, 25 + length2pixel(field_width / 2) + length2pixel(field_width * 7 / 26))
                                      ])

    right_area = pg.draw.lines(screen, color, closed=False,
                               points=[(25 + length2pixel(field_length),
                                        25 + length2pixel(field_width / 2) - length2pixel(field_width * 7 / 26)),
                                       (25 + length2pixel(field_length) - length2pixel(field_length * 3 / 28),
                                        25 + length2pixel(field_width / 2) - length2pixel(field_width * 7 / 26)),
                                       (25 + length2pixel(field_length) - length2pixel(field_length * 3 / 28),
                                        25 + length2pixel(field_width / 2) + length2pixel(field_width * 7 / 26)),
                                       (25 + length2pixel(field_length),
                                        25 + length2pixel(field_width / 2) + length2pixel(field_width * 7 / 26))
                                       ])

    left_circle = pg.draw.arc(screen, color, (25 + length2pixel(field_length * 3 / 28) - length2pixel(10.09 / 100) / 2,
                                              25 + length2pixel(field_width / 2) - length2pixel(20 / 100) / 2,
                                              length2pixel(field_length * 1009 / 15000),
                                              length2pixel(field_width * 2 / 13)), np.deg2rad(-90),
                              np.deg2rad(90))

    right_circle = pg.draw.arc(screen, color, (
        25 + length2pixel(field_length * 59 / 75) + length2pixel(field_length * 3 / 28) - length2pixel(10.09 / 100) / 2,
        25 + length2pixel(field_width / 2) - length2pixel(20 / 100) / 2,
        length2pixel(field_length * 1009 / 15000),
        length2pixel(field_width * 2 / 13)), np.deg2rad(90),
                               np.deg2rad(-90))

    left_goal_area = pg.draw.line(screen, (0, 255, 0), (25, 25 + length2pixel(field_width / 2 - field_width * 2 / 13)),
                                  (25, 25 + length2pixel(field_width / 2 + field_width * 2 / 13)), 5)
    right_goal_area = pg.draw.line(screen, (0, 255, 0), (
        25 + length2pixel(field_length), 25 + length2pixel(field_width / 2 - field_width * 2 / 13)),
                                   (25 + length2pixel(field_length),
                                    25 + length2pixel(field_width / 2 + field_width * 2 / 13)), 5)

    return [side_lines, left_goal_area, right_goal_area]


pg.init()

field_screen = pg.display.set_mode((length2pixel(field_length) + 50+200, length2pixel(field_width) + 50))
pg.display.set_caption("Futebol de Robôs - VSSS")
text_font = pg.font.SysFont("arial", 25, True, True)
clock = pg.time.Clock()

while True:
    clock.tick(frame_rate)
    field_screen.fill((0,0,0))

    text_score = text_font.render("Score", True, "white")
    text_goals_a = text_font.render("Team A: {}".format(team_a_points), True, "red")
    text_goals_b = text_font.render("Team B: {}".format(team_b_points), True, "blue")

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            team_a_points += 1
            team_b_points -= 1

    field_draw(field_screen, field_length, field_width, color=(255, 100, 255))

    field_screen.blit(text_score, (100+length2pixel(field_length), length2pixel(field_width/2)-100))
    field_screen.blit(text_goals_a, (75 + length2pixel(field_length), length2pixel(field_width/2)-50))
    field_screen.blit(text_goals_b, (75 + length2pixel(field_length), length2pixel(field_width/2)))

    pg.display.update()



"""
