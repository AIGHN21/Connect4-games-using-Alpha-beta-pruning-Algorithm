# heuristic.py
# ---- heuristic (utility) ----
PLAYER = 1
BOT = -1
EMPTY = 0
def evaluate_window(window, player_id):
    """
    window: list of 4 cells
    player_id: 1 or -1
    return score for this window from perspective of player_id
    """
    opponent = -player_id
    score = 0
    if window.count(player_id) == 4:
        score += 10000
    elif window.count(player_id) == 3 and window.count(EMPTY) == 1:
        score += 50
    elif window.count(player_id) == 2 and window.count(EMPTY) == 2:
        score += 5

    # block opponent 3-in-row
    if window.count(opponent) == 3 and window.count(EMPTY) == 1:
        score -= 300

    return score

def heuristic(matrix):
    """
    Sum heuristic over all windows (rows, cols, diagonals).
    positive => advantage PLAYER, negative => advantage BOT.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    score = 0

    # prefer center column a bit
    center_col = cols // 2
    center_count_player = sum(1 for r in range(rows) if matrix[r][center_col] == PLAYER)
    center_count_bot = sum(1 for r in range(rows) if matrix[r][center_col] == BOT)
    score += (center_count_player - center_count_bot) * 3

    # horizontal
    for r in range(rows):
        for c in range(cols - 3):
            w = [matrix[r][c+i] for i in range(4)]
            score += evaluate_window(w, PLAYER)
            score -= evaluate_window(w, BOT)  # subtracting opponent's perspective

    # vertical
    for c in range(cols):
        for r in range(rows - 3):
            w = [matrix[r+i][c] for i in range(4)]
            score += evaluate_window(w, PLAYER)
            score -= evaluate_window(w, BOT)

    # main diagonal
    for r in range(rows - 3):
        for c in range(cols - 3):
            w = [matrix[r+i][c+i] for i in range(4)]
            score += evaluate_window(w, PLAYER)
            score -= evaluate_window(w, BOT)

    # secondary diagonal
    for r in range(3, rows):
        for c in range(cols - 3):
            w = [matrix[r-i][c+i] for i in range(4)]
            score += evaluate_window(w, PLAYER)
            score -= evaluate_window(w, BOT)

    return score
