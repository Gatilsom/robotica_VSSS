import numpy as np


def length2pixel(length):
    scale = 400
    return int(length * scale)


def get_center_polygon(polygon):
    x_mean = (polygon[0][0] + polygon[2][0]) / 2
    y_mean = (polygon[0][1] + polygon[2][1]) / 2
    return [x_mean, y_mean]


def move_polygon(polygon, x=0.0, y=0.0, angle=0.0):
    sin, cos = np.sin(angle), np.cos(angle)
    rotated_points = []
    center = get_center_polygon(polygon)

    for i in np.arange(4):
        polygon[i][0] -= center[0]
        polygon[i][1] -= center[1]

    polygon = np.hstack((polygon, np.zeros((4, 1))))

    #rotation_matrix = np.array([(cos, -sin), (sin, cos)])
    homogeneous_matrix = np.array([(cos, -sin, -center[0]),
                                   (sin, cos, -center[1]),
                                   (0, 0, 1)])

    for points in polygon:
        rotated_points.append(homogeneous_matrix @ points)

    for i in np.arange(4):
        rotated_points[i][0] += center[0] + length2pixel(x)
        rotated_points[i][1] += center[1] + length2pixel(y)
        rotated_points[i] = rotated_points[i][:-1]

    return rotated_points
