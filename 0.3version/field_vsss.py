
import pygame as pg
from pygame.locals import *
from random import randint
from vsss_tools import *

field_length = 1.5  # comprimento do campo [m]
field_width = 1.3  # largura do campo [m]


def draw_field(screen, length=1.5, width=1.3, color=(255, 0, 0)):
    field_chamfer = length * 7 / 150
    field_center = length * 2 / 15

    side_lines_top = pg.draw.lines(screen, color, closed=False,
                                   points=[(25, 25 + length2pixel(width / 2 - width * 2 / 13)),
                                           (25, 25 + length2pixel(field_chamfer)),
                                           (25 + length2pixel(field_chamfer), 25),
                                           (25 + length2pixel(length - field_chamfer), 25),
                                           (25 + length2pixel(length), 25 + length2pixel(field_chamfer)),
                                           (
                                               25 + length2pixel(length),
                                               25 + length2pixel(width / 2 - width * 2 / 13))

                                           ], width=3)

    side_lines_bottom = pg.draw.lines(screen, color, closed=False,
                                      points=[
                                          (25, 25 + length2pixel(width / 2 + width * 2 / 13)),
                                          (25, 25 + length2pixel(width - field_chamfer)),
                                          (25 + length2pixel(field_chamfer),
                                           25 + length2pixel(width)),
                                          (25 + length2pixel(length - field_chamfer),
                                           25 + length2pixel(width)),
                                          (25 + length2pixel(length),
                                           25 + length2pixel(width - field_chamfer)),
                                          (25 + length2pixel(length),
                                           25 + length2pixel(width / 2 + width * 2 / 13))
                                      ], width=3)

    center_line = pg.draw.line(screen, color, (25 + length2pixel(length / 2), 25),
                               (25 + length2pixel(length / 2), 25 + length2pixel(width)))

    center_circle = pg.draw.circle(screen, color,
                                   (25 + length2pixel(length / 2), 25 + length2pixel(width / 2)),
                                   length2pixel(field_center), 1)

    center_field = pg.draw.circle(screen, color,
                                  (25 + length2pixel(length / 2), 25 + length2pixel(width / 2)),
                                  length2pixel(field_center / 15), 0)


    left_area = pg.draw.lines(screen, color, closed=False,
                              points=[(25, 25 + length2pixel(width / 2) - length2pixel(width * 7 / 26)),
                                      (25 + length2pixel(length * 3 / 28),
                                       25 + length2pixel(width / 2) - length2pixel(width * 7 / 26)),
                                      (25 + length2pixel(length * 3 / 28),
                                       25 + length2pixel(width / 2) + length2pixel(width * 7 / 26)),
                                      (25, 25 + length2pixel(width / 2) + length2pixel(width * 7 / 26))
                                      ])

    right_area = pg.draw.lines(screen, color, closed=False,
                               points=[(25 + length2pixel(length),
                                        25 + length2pixel(width / 2) - length2pixel(width * 7 / 26)),
                                       (25 + length2pixel(length) - length2pixel(length * 3 / 28),
                                        25 + length2pixel(width / 2) - length2pixel(width * 7 / 26)),
                                       (25 + length2pixel(length) - length2pixel(length * 3 / 28),
                                        25 + length2pixel(width / 2) + length2pixel(width * 7 / 26)),
                                       (25 + length2pixel(length),
                                        25 + length2pixel(width / 2) + length2pixel(width * 7 / 26))
                                       ])

    left_circle = pg.draw.arc(screen, color, (25 + length2pixel(length * 3 / 28) - length2pixel(10.09 / 100) / 2,
                                              25 + length2pixel(width / 2) - length2pixel(20 / 100) / 2,
                                              length2pixel(length * 1009 / 15000),
                                              length2pixel(width * 2 / 13)), np.deg2rad(-90), np.deg2rad(90))

    right_circle = pg.draw.arc(screen, color, (
        25 + length2pixel(length * 59 / 75) + length2pixel(length * 3 / 28) - length2pixel(10.09 / 100) / 2,
        25 + length2pixel(width / 2) - length2pixel(20 / 100) / 2, length2pixel(length * 1009 / 15000),
        length2pixel(width * 2 / 13)), np.deg2rad(90), np.deg2rad(-90))

    left_goal_area = pg.draw.line(screen, (0, 255, 0), (25, 25 + length2pixel(width / 2 - width * 2 / 13)),
                                  (25, 25 + length2pixel(width / 2 + width * 2 / 13)), 5)

    right_goal_area = pg.draw.line(screen, (0, 255, 0), (
        25 + length2pixel(length), 25 + length2pixel(width / 2 - width * 2 / 13)),
                                   (25 + length2pixel(length),
                                    25 + length2pixel(width / 2 + width * 2 / 13)), 5)

    return [side_lines_top, side_lines_bottom, left_goal_area, right_goal_area]


def draw_ball(screen, length=1.5, width=1.3, radius=42.7 / 2000, color="orange"):
    x_pos = randint(25, 25 + length2pixel(length))
    y_pos = randint(25, 25 + length2pixel(width))
    baal = pg.draw.circle(screen, color, (x_pos, y_pos), length2pixel(radius), 0)
    return baal
