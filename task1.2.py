def is_cross(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    x_a = (ax1, ax2)  # координаты x обеих точек прямоугольника А
    x_b = (bx1, bx2)  # координаты x обеих точке прямоугольника В

    y_a = (ay1, ay2)  # координаты x обеих точек прямоугольника А
    y_b = (by1, by2)  # координаты x обеих точек прямоугольника В

    if max(x_a) < min(x_b) or max(y_a) < min(y_b) or min(y_a) > max(y_b):
        return False  # не пересекаются
    else:
        dx = max(x_a) - min(x_b)
        dy = max(y_a) - min(y_b)
        print(f"Площадь пересечения: {dx * dy}")
    return True  # пересекаются


if __name__ == "__main__":
    print(is_cross(1, 1, 2, 2, 3, 3, 4, 4))  # False
    print(is_cross(5, 5, 7, 3, 1, 4, 6, 1))  # True
    print(is_cross(-2, 3, 0, -2, 0, -2, 2, -4))  # True
