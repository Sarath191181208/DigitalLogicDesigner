from .consts import ColoredChars

def check_vals(vals: list[bool], outs: list[bool]) -> str:
    """helper function for testing"""
    char = ColoredChars.tick
    for v, o in zip(vals, outs):
        if v != o:
            char = ColoredChars.cross

    return char

def get_table_header(num_inputs: int, num_outputs: int) -> list[str]:
    table_header = [f"I{i}" for i in range(num_inputs)]
    table_header.extend([f"O{i}" for i in range(num_outputs)])
    table_header.extend([f"Exp{i}" for i in range(num_outputs)])
    table_header.append("Check")
    return table_header

def get_row(arr: list[bool], outputs:list[bool], eval_exp) -> list[str]:
    out_str = [f"{val}" for val in arr]

    vals = eval_exp(*[bool(x) for x in arr])
    outs = [bool(x) for x in outputs]

    check = check_vals(vals, outs)
    
    out_str.extend([f"{bool(x)}" for x in outs])
    out_str.extend([f"{bool(x)}" for x in vals])
    out_str.append(check)

    return out_str

def get_truth_table_vals(num_inputs):
    val = lambda i, j: (i & (2**j)) >> j
    arrs = [
        [val(i, j) for j in range(num_inputs)]
    for i in range(2**num_inputs)
    ]
    return arrs