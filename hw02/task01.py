# Структурное программирование:
# Трассировка пути в лабиринте:
# Задание: Создайте функцию, которая принимает двумерный массив (лабиринт) и начальную и конечную точки. 
# Функция должна возвращать путь от начальной до конечной точки или сообщение, что путь невозможен.
# Входные данные:Двумерный массив размера MxN, где '0' - это проход, а '1' - это стена.
# Координаты начальной и конечной точки.Выходные данные:Массив координат пути или сообщение об ошибке.

from collections import deque

def find_path(maze, start, end):
    queue = deque([start])
    visited = set([start])
    parents = {start: None}

    while queue:
        cell = queue.popleft()
        if cell == end:
            path = []
            while cell:
                path.append(cell)
                cell = parents[cell]
            return list(reversed(path))
        row, col = cell
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            r, c = row + dr, col + dc
            if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == 0 and (r, c) not in visited:
                queue.append((r, c))
                visited.add((r, c))
                parents[(r, c)] = cell

    return None



maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0]
]


maze2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0]
]

start = (0, 0)
end = (6, 8)

path = find_path(maze, start, end)
path2 = find_path(maze2, start, end)
print(path)
print(path2)