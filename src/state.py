from dataclasses import dataclass
from typing import List

@dataclass
class GameState:
    board: List[List[int]]
    cols: List[int]

def init_state() -> GameState:
    board = [[0]*7 for _ in range(6)]
    cols = [5]*7
    return GameState(board, cols)