from prettytable import PrettyTable

from .board_test_helper import get_truth_table_vals, get_table_header, get_row

from board import evaluate
from board import get_num_inputs, get_num_outputs, set_port

from .consts import ColoredChars

def test_board(board: dict, eval_func) -> None:

    total_fails = 0

    num_inputs = get_num_inputs(board)
    num_outputs = get_num_outputs(board)

    truth_table_vals = get_truth_table_vals(num_inputs)
    truth_table_header = get_table_header(num_inputs, num_outputs)
    truth_table = PrettyTable(truth_table_header)

    for arr in truth_table_vals:
        for i in range(num_inputs):
            set_port(board, f"I{i}", arr[i])
        evaluate(board)
        out_row_list = get_row(arr, board.get("outputs"), eval_func)

        is_failure = out_row_list[-1] == ColoredChars.cross
        total_fails += is_failure

        truth_table.add_row(out_row_list)
    print(truth_table)

    return total_fails