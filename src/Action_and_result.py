from Player import player

def actions(last_row_each_col):
    """
    Return list of available columns (0..6) where you can drop a piece.
    last_row_each_col gives the next free row index for each column, or -1 if full.
    """
    available = []
    for col, row_idx in enumerate(last_row_each_col):
        if row_idx >= 0:
            available.append(col)
    return available

def result(matrix, last_row_each_col, action):
    """
    action: column integer
    returns new_matrix, new_last_row_each_col
    """
    col = action
    if last_row_each_col[col] < 0:
        raise ValueError("Column is full")
    new_matrix = [r[:] for r in matrix]
    new_last = last_row_each_col[:]  # shallow copy is fine (list of ints)
    row_to_place = new_last[col]
    cur_player = player(matrix)
    new_matrix[row_to_place][col] = cur_player
    new_last[col] -= 1  # next free row up one
    return new_matrix, new_last
