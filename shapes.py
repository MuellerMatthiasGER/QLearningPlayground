import math

def get_star_shape(center_x, center_y, radius) -> list:
    outer_radius = radius
    inner_radius = radius / 2
    points = []

    for i in range(11):
        angle = math.pi / 5 * i
        x = center_x + outer_radius * math.cos(angle)
        y = center_y + outer_radius * math.sin(angle)
        points.append(x)
        points.append(y)
        x = center_x + inner_radius * math.cos(angle + math.pi/10)
        y = center_y + inner_radius * math.sin(angle + math.pi/10)
        points.append(x)
        points.append(y)

    return points