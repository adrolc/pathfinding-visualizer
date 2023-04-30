import random

DEFAULT_MAZE_SIZE = (50, 50)

def create_maze(width, height):
    maze = [[1] * width for _ in range(height)]
    start = (1, 1)
    maze[start[0]][start[1]] = 0

    def in_bounds(x, y):
        return 0 <= x < height and 0 <= y < width

    def get_neighbors(x, y):
        neighbors = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx * 2, y + dy * 2
            if in_bounds(nx, ny):
                neighbors.append((nx, ny))
        return neighbors

    def mark_path(x, y, nx, ny):
        maze[(x + nx) // 2][(y + ny) // 2] = 0
        maze[nx][ny] = 0

    frontier = [start]
    while frontier:
        x, y = frontier.pop(random.randint(0, len(frontier) - 1))
        neighbors = get_neighbors(x, y)
        random.shuffle(neighbors)

        for nx, ny in neighbors:
            if maze[nx][ny] == 1:
                mark_path(x, y, nx, ny)
                frontier.append((nx, ny))

    return maze