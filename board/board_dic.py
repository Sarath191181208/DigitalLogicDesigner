
from copy import deepcopy
from .Exceptions import InvalidPortNumber

get_empty_board = get_empty_gate = lambda name, num_inputs, num_outputs: {
    "name": name,
    "inputs": [0]*num_inputs,
    "outputs":[0]*num_outputs,
    "input_connections": [],
    "output_connections": [],
}

# this returns a list of outputs for each gate 
# because some base gates can have multiple outputs
base_gates = {
    "AND": lambda a, b: [a and b],
    "OR": lambda a, b: [a or b],
    "NOT": lambda a: [not a],
}

def get_unique_gates(gate) -> list:
    unique_gates = []
    for child_gate, in_port, gate_port in gate.get("input_connections"):
        if child_gate not in unique_gates:
            unique_gates.append(child_gate)
    return unique_gates
    

add_input = lambda gate: gate.get("inputs").append(0)
add_output = lambda gate: gate.get("outputs").append(0)

get_num_inputs: int = lambda gate: len(gate.get("inputs"))
get_num_outputs: int = lambda gate: len(gate.get("outputs"))


def get_ports_list(gate, port_name) -> list[bool]:
    _helper_dic = {
        "I": gate.get("inputs"),
        "O": gate.get("outputs")
    }
    return _helper_dic[port_name[0].upper()]

def get_port(gate: dict, port_name: str) -> bool:
    lst = get_ports_list(gate, port_name)
    port_idx = int(port_name[1:])
    if port_idx >= len(lst):
        raise InvalidPortNumber(port_name, len(lst), gate.get("name"))
    return lst[port_idx]

def set_port(gate: dict, port_name: str, value: bool) -> None:
    lst = get_ports_list(gate, port_name)
    port_idx = int(port_name[1:])
    if port_idx >= len(lst):
        raise InvalidPortNumber(port_name, len(lst), gate.get("name"))
    lst[port_idx] = value

def get_conns_list(gate: dict, port_name: str) -> list[tuple]:
    _helper_dic = {
        "I": gate.get("input_connections"),
        "O": gate.get("output_connections")
    }
    return _helper_dic[port_name[0].upper()]

def connect_wire(gate_1: dict, gate_2: dict, port_1: str, port_2: str) -> None:
    get_conns_list(gate_1, port_2).append((gate_2, port_1, port_2))

def calc_base_gate(gate: dict) -> None:
    out: list[bool] = base_gates.get(gate.get("name"))(*gate.get("inputs"))
    gate["outputs"] = out

def evaluate(gate: dict) -> list[bool]:

    is_base_gate = gate.get("name").upper() in base_gates
    if is_base_gate:
        calc_base_gate(gate)

    for child_gate, in_port, gate_port in gate.get("input_connections"):
        val = get_port(gate, in_port)
        set_port(child_gate, gate_port, val)

    unique_gates = get_unique_gates(gate)

    for child_gate in unique_gates:
        evaluate(child_gate)

    for child_gate, out_port, gate_port in gate.get("output_connections"):
        val = get_port(child_gate, out_port)
        set_port(gate, out_port, val)

    return gate.get("outputs")
    