
from time import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.patches import Rectangle, Circle

_field_length = 1.5 # comprimento do campo [m]
_field_width = 1.3 # largura do campo [m]
_robot_length = 0.075 # dimensão do robô cúbico [m]

_delta_t = 0.1 # tempo de amostragem [s]
_max_time = 5 # tempo de simulação [s]
_time = 0 # variável de tempo [s]

_inicial_position = [0, 0, 0]
#_inicial_position = [_field_length/2, _field_width/2, 0] # posição inicial [m, m, rad]
_radius_wheel = 25 / 1000 # raio da roda [m]
_length_wheel = 75 / 1000 # distância entre eixos das rodas [m]

_wheel_left = 30 * np.pi / 180 # velocidade angular da roda esquerda [rad/s]
_wheel_right = 60 * np.pi / 180 # velocidade angular da roda direita [rad/s]

# velocidades do robô em relação ao seu próprio frame
_angular_robot = _radius_wheel * (_wheel_right - _wheel_left) / _length_wheel # velocidade angular [rad/s]
_linear_robot = _radius_wheel * (_wheel_right + _wheel_left) / 2 # velocidade linear [m/s]

# velocidades do robô em relação ao frame inercial
_theta = 30 * np.pi / 180 # orientação em relação ao frame inercial [rad]
_ine_angular_robot = _angular_robot # [rad/s]
_ine_linear_robot_x = _linear_robot * np.cos(_theta) # em relação ao eixo x [m/s]
_ine_linear_robot_y = _linear_robot * np.sin(_theta) # em relação ao eixo y [m/s]

print(int(_max_time/_delta_t))
print("======================")

# criando a figura e delimitando o campo
_fig = plt.figure()
_field_margin = 0.1
_axis = plt.axes(xlim=(-_field_margin, _field_length + _field_margin), ylim=(-_field_margin, _field_width + _field_margin))
_line, = _axis.plot([], [], lw=2, color="red")
_x_data, _y_data = [], []
_axis.add_patch(Rectangle((0, 0), _field_length, _field_width, facecolor="#F5F5DC", edgecolor="000000", fill=True,))
_robot_capsule = Rectangle((-_robot_length/2, -_robot_length/2), _robot_length, _robot_length, facecolor="black", edgecolor="red", fill=True,)
#_axis.add_patch(_robot_capsule)
#_axis.add_patch(Circle((0, 0), radius=0.05, fill=True,))



# função inicial chamada no início da plotagem
def init_plot():
    global _line, _x_data, _y_data, _robot_capsule
    _line.set_data([], [])
    _x_data.append(_inicial_position[0])
    _y_data.append(_inicial_position[1])
    _line.set_data(_x_data, _y_data)
    _axis.add_patch(_robot_capsule)
    return _robot_capsule,

# função de animação
def animate_plot(i):
    global _line, _x_data, _y_data, _delta_t, _time, flag_teste, _robot_capsule, _axis

    if i == int(_max_time/_delta_t) - 1:
        #plt.close()
        pass
    x = _time
    y = _time*_time
    #_robot_capsule.set_x(x)
    #_robot_capsule.set_y(y)

    _robot_capsule.set_xy([x, y])

    _time += _delta_t

    if x > _field_length or y > _field_width:
        _time = 0

    return _robot_capsule,


tempo = time()
animation_plot = ani.FuncAnimation(_fig, animate_plot, init_func=init_plot,frames=int(_max_time/_delta_t),interval=_delta_t*1000, blit=True, repeat=False)
plt.show()

print(time()-tempo)

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