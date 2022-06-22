# from board import BaseGate
# from gates import AND, OR, NOT, NOR, XOR
from board import AND, OR, NOT, connect_wire, get_empty_board
from tests.board_test import test_board
from logical_expressions import *

fails = 0

################################################
################# AND Gate #####################
################################################

def eval_exp(a, b) -> list[bool]:
    """ hepler function for testing """
    return [
        a and b
    ]

# adding inputs & outputs
board = get_empty_board(
    name = "AND Test",
    num_inputs  = 2, 
    num_outputs = 1,
)

# defining gates
not_1 = AND()

# connecting gates
connect_wire(board, not_1, "I0", "I0")
connect_wire(board, not_1, "I1", "I1")

# connecting outputs
connect_wire(board, not_1, "O0", "O0")

print(board.get("name"), " :")
fails += test_board(board, eval_exp)

################################################
################# OR Gate ######################
################################################

def eval_exp(a, b) -> list[bool]:
    """ hepler function for testing """
    return [
        a or b
    ]

# adding inputs & outputs
board = get_empty_board(
    name = "OR Test",
    num_inputs  = 2, 
    num_outputs = 1,
)

# defining gates
not_1 = OR()

# connecting gates
connect_wire(board, not_1, "I0", "I0")
connect_wire(board, not_1, "I1", "I1")

# connecting outputs
connect_wire(board, not_1, "O0", "O0")

print(board.get("name"), " :")
fails += test_board(board, eval_exp)


################################################
################# NOT Gate #####################
################################################

def eval_exp(a) -> list[bool]:
    """ hepler function for testing """
    return [
        not a
    ]

# adding inputs & outputs
board = get_empty_board(
    name = "NOT Test",
    num_inputs  = 1, 
    num_outputs = 1,
)

# defining gates
not_1 = NOT()

# connecting gates
connect_wire(board, not_1, "I0", "I0")

# connecting outputs
connect_wire(board, not_1, "O0", "O0")

print(board.get("name"), " :")
fails += test_board(board, eval_exp)

################################################
################# NAND Gate ####################
################################################

def eval_exp(a, b) -> list[bool]:
    """ hepler function for testing """
    return [
        nand(a, b)
    ]

# adding inputs & outputs
board = get_empty_board(
    name = "NAND Test",
    num_inputs  = 2, 
    num_outputs = 1,
)

# defining gates
not_1 = NOT()
and_1 = AND()

# connecting gates
connect_wire(board, and_1, "I0", "I0")
connect_wire(board, and_1, "I1", "I1")

connect_wire(and_1, not_1, "O0", "I0")

# connecting outputs
connect_wire(board, not_1, "O0", "O0")

print(board.get("name"), " :")
fails += test_board(board, eval_exp)


################################################
############### NAND + OR Gate #################
################################################

def eval_exp(a, b, c) -> list[bool]:
    """ hepler function for testing """
    return [
        nand(a, b) or c
    ]

# adding inputs & outputs
board = get_empty_board(
    name = "NAND + OR Test",
    num_inputs  = 3, 
    num_outputs = 1,
)

# defining gates
not_1 = NOT()
and_1 = AND()
or_1 = OR()

# connecting gates
connect_wire(board, and_1, "I0", "I0")
connect_wire(board, and_1, "I1", "I1")
connect_wire(and_1, not_1, "O0", "I0")

connect_wire(not_1, or_1, "O0", "I0")
connect_wire(board, or_1, "I2", "I1")


# connecting outputs
connect_wire(board, or_1, "O0", "O0")

print(board.get("name"), " :")
fails += test_board(board, eval_exp)

