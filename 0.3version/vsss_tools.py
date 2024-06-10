import numpy as np

field_length = 1.5  # comprimento do campo [m]
field_width = 1.3  # largura do campo [m]

def length2pixel(length):
    scale = 400
    return int(length * scale)


def org_transform(point):
    x_center = length2pixel(point[0]) + 25 + length2pixel(field_length / 2)
    y_center = -length2pixel(point[1]) + 25 + length2pixel(field_width / 2)
    return x_center, y_center



def get_center_polygon(polygon):
    x_mean = (polygon[0][0] + polygon[2][0]) / 2
    y_mean = (polygon[0][1] + polygon[2][1]) / 2
    return [x_mean, y_mean]


def move_polygon(polygon, x=0.0, y=0.0, theta=0.0):
    sin, cos = np.sin(theta), np.cos(theta)
    rotated_points = []
    center = get_center_polygon(polygon)

    for i in np.arange(4):
        polygon[i][0] -= center[0]
        polygon[i][1] -= center[1]

    polygon = np.hstack((polygon, np.zeros((4, 1))))

    # rotation_matrix = np.array([(cos, -sin), (sin, cos)])
    homogeneous_matrix = np.array([(cos, -sin, -center[0]),
                                   (sin, cos, -center[1]),
                                   (0, 0, 1)])

    for points in polygon:
        rotated_points.append(homogeneous_matrix @ points)

    for i in np.arange(4):
        rotated_points[i][0] += center[0] + x
        rotated_points[i][1] += center[1] + y
        rotated_points[i] = rotated_points[i][:-1]

    return np.array(rotated_points)
