from time import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.patches import Rectangle, Circle

_field_length = 1.5  # comprimento do campo [m]
_field_width = 1.3  # largura do campo [m]
_robot_length = 0.075  # dimensão do robô cúbico [m]

_delta_t = 0.1  # tempo de amostragem [s]
_max_time = 5  # tempo de simulação [s]
_time = 0  # variável de tempo atual [s]
_time_reference = 0  # variável de tempo de referência [s]
_n_frames = 1  # int(_max_time/_delta_t) # número de frames

_inicial_position = [0, 0, 0]
# _inicial_position = [_field_length/2, _field_width/2, 0] # posição inicial [m, m, rad]
_radius_wheel = 25 / 1000  # raio da roda [m]
_length_wheel = 75 / 1000  # distância entre eixos das rodas [m]

_wheel_left = 30 * np.pi / 180  # velocidade angular da roda esquerda [rad/s]
_wheel_right = 60 * np.pi / 180  # velocidade angular da roda direita [rad/s]



print(int(_max_time / _delta_t))
print("======================")

# criando a figura e delimitando o campo
_fig = plt.figure()
_field_margin = 0.1
_axis = plt.axes(xlim=(-_field_margin, _field_length + _field_margin),
                 ylim=(-_field_margin, _field_width + _field_margin))
_line, = _axis.plot([], [], lw=2, color="red")
_x_data, _y_data = [], []
_axis.add_patch(Rectangle((0, 0), _field_length, _field_width, facecolor="#F5F5DC", edgecolor="000000", fill=True, ))
_robot_capsule = Rectangle((_inicial_position[0], _inicial_position[1]), _robot_length, _robot_length,
                           facecolor="black", edgecolor="red", fill=True, )
_robot_capsule2 = Rectangle((0.6, _robot_length / 2), _robot_length, _robot_length, facecolor="blue", edgecolor="red",
                            fill=True, )


# _axis.add_patch(_robot_capsule)
# _axis.add_patch(Circle((0, 0), radius=0.05, fill=True,))


class Robot:

    def __int__(self, shirt, team, length, wheel_radius, x, y, theta, color):
        self.robot = Rectangle((x, y), length, length, facecolor=color, edgecolor="black", fill=True, )
        self.shirt = shirt
        self.team = team
        self.length = length
        self.x_pos = None
        self.y_pos = None
        self.theta_pos = theta
        self.left_wheel = 0.0
        self.right_wheel = 0.0
        self.set_position(x, y)
        self.color = color
        self.vel_linear = 0.0
        self.vel_angular = 0.0
        self.wheel_radius = wheel_radius


    def set_position(self, x, y):
        self.x_pos = x - self.length / 2
        self.y_pos = y - self.length / 2
        self.robot.set_xy([self.x_pos, self.y_pos])


    def set_wheel(self, left, right):  # usar rad/s
        self.left_wheel = left
        self.right_wheel = right
        self.vel_angular = self.wheel_radius * (self.right_wheel - self.left_wheel) / self.length  # velocidade angular [rad/s]
        self.vel_linear = self.wheel_radius * (self.right_wheel + self.left_wheel) / 2  # velocidade linear [m/s]


    def get_velocity_robot(self):
        return [self.vel_linear, self.vel_angular]


    def get_velocity_org(self):
        # velocidades do robô em relação ao frame inercial
        _theta = 30 * np.pi / 180  # orientação em relação ao frame inercial [rad]
        _ine_angular_robot = _angular_robot  # [rad/s]
        _ine_linear_robot_x = _linear_robot * np.cos(_theta)  # em relação ao eixo x [m/s]
        _ine_linear_robot_y = _linear_robot * np.sin(_theta)  # em relação ao eixo y [m/s]

    def get_position(self):
        return [self.x_pos + self.length / 2, self.y_pos + self.length / 2]




    # função inicial chamada no início da plotagem
def init_plot():
    global _robot_capsule, _robot_capsule2
    global _time_reference, _time
    _axis.add_patch(_robot_capsule)
    _axis.add_patch(_robot_capsule2)
    _time_reference = time()
    return _robot_capsule, _robot_capsule2,


# função de animação
def animate_plot(i):
    global _axis, _robot_capsule, _robot_capsule2
    global _time_reference, _time, _delta_t, _n_frames

    if i == _n_frames - 1:
        # plt.close()
        pass
    if i != 0:
        _time = time() - _time_reference
    else:
        _time = _time_reference

    x = _time
    y = x * x

    # _robot_capsule.set_xy([x, y])
    # _robot_capsule2.set_xy([x, y])

    _time = _time - time()

    if x > _field_length or y > _field_width:
        _time_reference = time()

    return _robot_capsule, _robot_capsule2,


tempo = time()
animation_plot = ani.FuncAnimation(_fig, animate_plot, init_func=init_plot, frames=_n_frames, interval=_delta_t * 1000,
                                   blit=True, repeat=False)
plt.show()

print(time() - tempo)
