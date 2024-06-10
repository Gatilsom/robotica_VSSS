
from field_vsss import *


robot_length = 75 / 1000  # dimensão do robô cúbico [m]
wheel_radius = 25 / 1000  # raio da roda [m]


class Robot:

    def __init__(self, shirt, team, x, y, theta, color):
        global robot_length, wheel_radius
        xa, ya = x - robot_length / 2, y - robot_length / 2
        xb, yb = x - robot_length / 2, y + robot_length / 2
        xc, yc = x + robot_length / 2, y + robot_length / 2
        xd, yd = x + robot_length / 2, y - robot_length / 2

        self.x, self.y = x, y

        self.theta = theta  # orientação em relação ao frame inercial [rad]
        self.vertices = np.array([[xa, ya], [xb, yb], [xc, yc], [xd, yd]])
        self.move(0.0, 0.0, theta)
        self.x_ref, self.y_ref = (xc + xd) / 2, (yc + yd) / 2

        self.velocity_left_wheel = 0.0
        self.velocity_right_wheel = 0.0
        self.velocity_linear = 0.0
        self.velocity_angular = 0.0
        self.length = robot_length
        self.wheel_radius = wheel_radius
        self.shirt = shirt
        self.team = team
        self.color = color

    def draw(self, screen):
        aux = []
        for vertice in self.vertices:
            x, y = org_transform(vertice)
            aux.append([x, y])
        pg.draw.polygon(screen, self.color, aux)
        pg.draw.line(screen, "red", aux[2], aux[3], width=5)
        pass

    def set_wheel(self, left, right):  # usar rad/s
        self.velocity_left_wheel = left
        self.velocity_right_wheel = right
        R = self.wheel_radius
        wr = left
        wl = right
        L = self.length
        self.velocity_angular = R * (wr - wl) / L  # velocidade angular [rad/s]
        self.velocity_linear = R * (wr + wl) / 2  # velocidade linear [m/s]
        pass

    def get_velocity_org(self):
        v = self.velocity_linear
        w = self.velocity_angular
        theta = self.theta
        # velocidades do robô em relação ao frame inercial
        return np.array([v * np.cos(theta),  # em relação ao eixo x [m/s]
                         v * np.sin(theta),  # em relação ao eixo y [m/s]
                         w])  # [rad/s]

    def move(self, x, y, theta):
        self.vertices = move_polygon(self.vertices, x, y, theta)
        center = get_center_polygon(self.vertices)
        self.x = center[0]
        self.y = center[1]
        pass
