# Размер доски (6x6)
BOARD_SIZE = 6

# Возможные ходы коня
MOVES = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def is_valid_move(x, y, board):
    """Проверяет, находится ли клетка (x, y) на доске и не посещена ли она."""
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[x][y] == -1

def print_board(board):
    """Выводит доску в виде матрицы."""
    for row in board:
        print(" ".join(f"{cell:2}" for cell in row))
    print()

def knight_tour(x, y, move_count, board):
    """Рекурсивная функция для поиска маршрута коня."""
    # Если все клетки посещены, маршрут найден
    if move_count == BOARD_SIZE * BOARD_SIZE:
        print_board(board)
        return True

    # Перебираем все возможные ходы
    for dx, dy in MOVES:
        next_x, next_y = x + dx, y + dy
        if is_valid_move(next_x, next_y, board):
            # Делаем ход
            board[next_x][next_y] = move_count
            # Рекурсивно пытаемся найти следующий ход
            if knight_tour(next_x, next_y, move_count + 1, board):
                return True
            # Если маршрут не найден, откатываем ход (backtracking)
            board[next_x][next_y] = -1

    # Если ни один ход не привел к решению, возвращаем False
    return False

def start_knight_tour(start_x, start_y):
    """Инициализирует доску и начинает поиск маршрута."""
    # Создаем доску и заполняем её -1 (клетки не посещены)
    board = [[-1 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    # Начальная позиция коня
    board[start_x][start_y] = 0
    # Запускаем рекурсивный поиск
    if not knight_tour(start_x, start_y, 1, board):
        print("Маршрут не найден.")

# Ввод начальных координат
start_x = int(input("Введите начальную координату X (0-5): "))
start_y = int(input("Введите начальную координату Y (0-5): "))

# Проверка корректности ввода
if 0 <= start_x < BOARD_SIZE and 0 <= start_y < BOARD_SIZE:
    start_knight_tour(start_x, start_y)
else:
    print("Некорректные координаты. Введите числа от 0 до 5.")

