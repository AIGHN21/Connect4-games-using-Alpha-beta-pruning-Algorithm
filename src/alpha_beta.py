# alpha_beta.py

from Player import player
from Action_and_result import actions , result
from Heuristic import heuristic
import math
PLAYER = 1
BOT = -1
def get_winner_exact(matrix):
    """
    Check for 4-in-a-row. Return PLAYER(1) or BOT(-1) if there's a winner, else None.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # horizontal
    for r in range(rows):
        for c in range(cols - 3):
            w = [matrix[r][c+i] for i in range(4)]
            if w.count(PLAYER) == 4:
                return PLAYER
            if w.count(BOT) == 4:
                return BOT

    # vertical
    for c in range(cols):
        for r in range(rows - 3):
            w = [matrix[r+i][c] for i in range(4)]
            if w.count(PLAYER) == 4:
                return PLAYER
            if w.count(BOT) == 4:
                return BOT

    # main diagonal (top-left to bottom-right)
    for r in range(rows - 3):
        for c in range(cols - 3):
            w = [matrix[r+i][c+i] for i in range(4)]
            if w.count(PLAYER) == 4:
                return PLAYER
            if w.count(BOT) == 4:
                return BOT

    # secondary diagonal (bottom-left to top-right)
    for r in range(3, rows):
        for c in range(cols - 3):
            w = [matrix[r-i][c+i] for i in range(4)]
            if w.count(PLAYER) == 4:
                return PLAYER
            if w.count(BOT) == 4:
                return BOT

    return None


def terminal(matrix, last_row_each_col):
    """
    Return True if game over (win or full).
    """
    if get_winner_exact(matrix) is not None:
        return True
    # full?
    if all(idx < 0 for idx in last_row_each_col):
        return True
    return False
def alphabeta_decision(matrix, last_row_each_col, depth):
    """
    Return best column (action) for current player using alpha-beta search to given depth.
    """
    cur = player(matrix)
    alpha = -math.inf
    beta = math.inf

    best_action = None
    if cur == PLAYER:
        value = -math.inf
        for a in actions(last_row_each_col):
            nm, nl = result(matrix, last_row_each_col, a)
            v = min_value(nm, nl, depth-1, alpha, beta)
            if v > value:
                value = v
                best_action = a
            alpha = max(alpha, value)
    else:
        value = math.inf
        for a in actions(last_row_each_col):
            nm, nl = result(matrix, last_row_each_col, a)
            v = min_value(nm, nl, depth-1, alpha, beta)  # Đã sửa: gọi min_value cho BOT
            if v < value:
                value = v
                best_action = a
            beta = min(beta, value)

    return best_action

def max_value(matrix, last_row_each_col, depth, alpha, beta):
    winner = get_winner_exact(matrix)
    if winner == PLAYER:
        return math.inf
    if winner == BOT:
        return -math.inf
    if depth == 0 or terminal(matrix, last_row_each_col):
        return heuristic(matrix)

    v = -math.inf
    for a in actions(last_row_each_col):
        nm, nl = result(matrix, last_row_each_col, a)
        v = max(v, min_value(nm, nl, depth-1, alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def min_value(matrix, last_row_each_col, depth, alpha, beta):
    winner = get_winner_exact(matrix)
    if winner == PLAYER:
        return math.inf
    if winner == BOT:
        return -math.inf
    if depth == 0 or terminal(matrix, last_row_each_col):
        return heuristic(matrix)

    v = math.inf
    for a in actions(last_row_each_col):
        nm, nl = result(matrix, last_row_each_col, a)
        v = min(v, max_value(nm, nl, depth-1, alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v