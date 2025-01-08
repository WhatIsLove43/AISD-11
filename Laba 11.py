import math


def find_closest_pair(points):
    """
    Находит пару точек с минимальным расстоянием.
    :param points: список точек [(x1, y1), (x2, y2), ...]
    :return: минимальное расстояние и соответствующая пара точек
    """
    n = len(points)
    if n < 2:
        return None, "Недостаточно точек для вычисления."

    min_distance = float('inf')  # Инициализируем минимальное расстояние
    closest_pair = None  # Инициализируем пару точек

    # Перебираем все возможные пары точек
    for i in range(n):
        for j in range(i + 1, n):
            # Вычисляем евклидово расстояние
            distance = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return min_distance, closest_pair


# Тестовый пример
if __name__ == "__main__":
    points = [
        (1, 2), (4, 6), (7, 8), (2, 1), (5, 5), (9, 0)
    ]

    distance, pair = find_closest_pair(points)
    if pair:
        print(f"Минимальное расстояние: {distance:.2f}")
        print(f"Пара точек: {pair[0]} и {pair[1]}")
    else:
        print(pair)
