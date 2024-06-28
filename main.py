import click
import chess
import re

piece_map = {
    "k": "♔",
    "K": "♚",
    "q": "♕",
    "Q": "♛",
    "r": "♖",
    "R": "♜",
    "b": "♗",
    "B": "♝",
    "N": "♞",
    "n": "♘",
    "p": "♙",
    "P": "♟︎"
}

starting_pos_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"


def draw_board(fen):
    board = chess.Board(fen)
    for word, replacement in piece_map.items():
        board = re.sub(word, replacement, str(board))
    print(board)


def player_move(fen):
    fen = starting_pos_fen
    board = chess.Board(fen)
    Pe4 = chess.Move.from_uci("e2e4")
    board.push(Pe4)
    fen = board.fen()
    draw_board(fen)


if __name__ == "__main__":
    player_move(fen=starting_pos_fen)
