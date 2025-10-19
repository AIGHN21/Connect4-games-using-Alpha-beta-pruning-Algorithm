import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm

# persistent figure/axis/connection for reuse (do not create a new window each time)
_FIG = None
_AX = None
_CID = None

def visualize(board, ax=None):
    if ax is None:
        fig, ax = plt.subplots()

    ax.clear()
    # map values: BOT(-1)=blue, EMPTY(0)=white, PLAYER(1)=red
    cmap = ListedColormap(["#2777cc", "#ffffff", "#d9534f"])
    norm = BoundaryNorm([-1.5, -0.5, 0.5, 1.5], cmap.N)

    # flip rows so row 0 is at the bottom (connect four convention)
    img = np.flip(board, 0)
    ax.imshow(img, cmap=cmap, norm=norm, origin="lower", aspect="equal")

    ax.set_xticks(range(img.shape[1]))
    ax.set_yticks(range(img.shape[0]))
    ax.set_xticklabels(range(img.shape[1]))
    ax.set_yticklabels(range(img.shape[0]))
    ax.set_title("Connect Four")
    ax.grid(False)
    plt.draw()

def visualize_interactive(board, on_click):
    """
    Open the figure once and register the handler; subsequent calls reuse the same figure.
    Call on_click(col) when the user clicks; on_click is responsible for updating the model (board).
    """
    global _FIG, _AX, _CID
    if _FIG is None:
        _FIG, _AX = plt.subplots()
        visualize(board, _AX)

        def handle_click(event):
            if event.xdata is None:
                return
            col = int(round(event.xdata))
            try:
                on_click(col)
            finally:
                # always redraw the current board state on the same figure
                visualize(board, _AX)
                _FIG.canvas.draw_idle()

        _CID = _FIG.canvas.mpl_connect('button_press_event', handle_click)
        # show non-blocking so the main loop can continue; the GUI event loop will handle clicks
        plt.show(block=False)
    else:
        # if the figure already exists, just update and redraw
        visualize(board, _AX)
        _FIG.canvas.draw_idle()