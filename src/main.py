# ...existing code...
import random
import matplotlib.pyplot as plt
from Board import visualize,visualize_interactive
import sys
from Alpha_Beta import terminal, get_winner_exact, alphabeta_decision
from Player import player
from Action_and_result import result, actions
from state import init_state, GameState
PLAYER = 1
BOT = -1
def init_state_wrapper():
    gs = init_state()

    return gs


def on_click(col):
    global gs
    if terminal(gs.board, gs.cols):
        return

    if player(gs.board) == PLAYER:
        if col not in actions(gs.cols):
            print("Invalid move")
            return
        gs.board, gs.cols = result(gs.board, gs.cols, col)
    else:
        move = alphabeta_decision(gs.board, gs.cols, depth=5)
        if move is None:
            move = random.choice(actions(gs.cols))
        print("AI chooses", move)
        gs.board, gs.cols = result(gs.board, gs.cols, move)

    visualize_interactive(gs.board, on_click)


# if __name__ == "__main__":
#     gs = init_state_wrapper()
#     # visualize(gs.board)

#     while True:
#         if terminal(gs.board, gs.cols):
#             w = get_winner_exact(gs.board)
#             if w == PLAYER:
#                 print("PLAYER wins")
#             elif w == BOT:
#                 print("BOT wins")
#             else:
#                 print("Draw")
#             break

#         if player(gs.board) == PLAYER:
#             while True:
#                 try:
#                     c = visualize_interactive(gs.board, on_click)
#                     if c not in actions(gs.cols):
#                         print("Invalid/Full column")
#                         sys.exit(1)
#                     gs.board, gs.cols = result(gs.board, gs.cols, c)
#                     # visualize(gs.board)
#                     break
#                 except ValueError:
#                     print("Enter integer 0-6")
#         else:
#             move = alphabeta_decision(gs.board, gs.cols, depth=5)
#             if move is None:
#                 move = random.choice(actions(gs.cols))
#             print("AI chooses", move)
#             gs.board, gs.cols = result(gs.board, gs.cols, move)
#             fig, ax = plt.subplots()
#             visualize(gs.board, ax)
#             fig.canvas.draw_idle()
#             plt.pause(0.5)



def on_click(col):
    global gs
    if terminal(gs.board, gs.cols):
        return

    if player(gs.board) == PLAYER:
        if col not in actions(gs.cols):
            print("Invalid move")
            return
        gs.board, gs.cols = result(gs.board, gs.cols, col)
    else:
        move = alphabeta_decision(gs.board, gs.cols, depth=5)
        if move is None:
            move = random.choice(actions(gs.cols))
        print("AI chooses", move)
        gs.board, gs.cols = result(gs.board, gs.cols, move)

    # DO NOT create a new figure here — board.visualize_interactive already redraws on the same figure
    # only request a redraw if needed (visualize_interactive will redraw when called)
    # visualize_interactive(gs.board, on_click)


if __name__ == "__main__":
    gs = init_state_wrapper()

    # open the interactive window once (non-blocking); the handler will call on_click on clicks
    visualize_interactive(gs.board, on_click)

    # main loop handles AI moves and end-of-game checks; GUI events handle the human player's clicks
    while True:
        if terminal(gs.board, gs.cols):
            w = get_winner_exact(gs.board)
            if w == PLAYER:
                print("PLAYER wins")
            elif w == BOT:
                print("BOT wins")
            else:
                print("Draw")
            break

        # if it's the human player's turn -> let GUI handle clicks. Pause briefly to allow event loop to run.
        if player(gs.board) == PLAYER:
            plt.pause(0.1)
            continue

        # if it's the AI's turn -> compute move, apply it, then redraw on the same figure
        move = alphabeta_decision(gs.board, gs.cols, depth=5)
        if move is None:
            move = random.choice(actions(gs.cols))
        print("AI chooses", move)
        gs.board, gs.cols = result(gs.board, gs.cols, move)
        # request a redraw on the existing figure
        visualize_interactive(gs.board, on_click)
        plt.pause(0.5)