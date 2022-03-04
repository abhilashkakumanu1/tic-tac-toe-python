# Tic Tac Toe
# Min Max Algorithm
from typing import List, Tuple, Set


class Board:
    __cells: List[List[str]]
    __empty_positions: Set[int]

    def __init__(self):
        self.__cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.__empty_positions = {0, 1, 2, 3, 4, 5, 6, 7, 8}

    def set(self, position: int, value: str):
        self.__validate_input(position, value.upper())
        if position in self.__empty_positions:
            (row, column) = self.__position_to_coordinates(position)
            self.__cells[row][column] = value
            self.__empty_positions.discard(position)
        else:
            raise ValueError(f"Position {position} is already set.")

    def __validate_input(self, position: int, value: str):
        # Position validation
        if position < 0 or position > 8:
            raise ValueError(
                "Oops! Not a valid position. Choose a position in the range: 0-8."
            )

        # Value validation
        if value != "X" and value != "O":
            raise ValueError("Oops! Not a valid value. Value can be 'X' or 'Y'.")

    def __position_to_coordinates(self, position: int) -> Tuple[int, int]:
        row = position // 3
        column = position - row * 3
        return (row, column)

    def __str__(self):
        str = ""
        for i in range(3):
            row = self.__cells[i]
            str += (
                f"{row[0]} | {row[1]} | {row[2]}\n"
                + (("-" * 9) if i != 2 else "")
                + "\n"
            )
        return str


board = Board()
print(board)
board.set(8, "O")
print(board)
board.set(8, "X")
print(board)
