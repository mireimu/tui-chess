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


def player_move(fen, move):
    fen = starting_pos_fen
    board = chess.Board(fen)
    Pe4 = chess.Move.from_uci(move)
    board.push(Pe4)
    fen = board.fen()


@click.group()
def cli():
    pass


@click.command()
@click.argument("file", type=click.Path(exists=False), required=0)
@click.option("-f", "--file", prompt="Enter file name", required=0)
def startgame(file):
    filename = file if file is not None else "chessgame.txt"
    with open(filename, "a+") as f:
        f.write(starting_pos_fen)
    draw_board(starting_pos_fen)


@click.command()
@click.argument("file", type=click.Path(exists=True), required=1)
@click.option("-m", "--move", prompt="Input your move", required=1)
@click.option("-f", "--file", prompt="Enter file name", required=0)
def move(file, move):
    file = file if file is not None else "chessgame.txt"
    fen = ""
    with open(file, "r") as f:
        fen += f.read()
    board = chess.Board(fen)
    player_move(fen, move)
    fen = board.fen()
    with open(file, "w") as f:
        f.write(fen)
    draw_board(fen)


cli.add_command(startgame)
cli.add_command(move)


if __name__ == "__main__":
    cli()
