# player.py
PLAYER = 1
BOT = -1
EMPTY = 0
def player(matrix):
    """
    Return who moves next on the board: PLAYER (1) or BOT (-1).
    We count non-empty cells; X (PLAYER) plays first (even count => PLAYER).
    """
    count = 0
    for row in matrix:
        for cell in row:
            if cell != EMPTY:
                count += 1
    # if count is even -> PLAYER's turn (PLAYER starts); if odd -> BOT's turn
    return PLAYER if (count % 2 == 0) else BOT
