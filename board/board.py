
from copy import copy, deepcopy
from .Exceptions import InvalidPortNumber

class BaseGate:
    def __init__(self, name="000", num_inputs=0, num_outputs=0) -> None:
        self.name = name
        self._inputs: list[bool] = [0]*num_inputs
        self._outputs: list[bool] = [0]*num_outputs
        self._input_connections = set()  # gate, port_name, gate_port_name
        self._output_connections = set()  # gate, port_name, gate_port_name
    
    def __call__(self):
        return deepcopy(self)
    
    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result

    
    def add_input(self) -> None:
        self._inputs.append(0)

    def add_output(self) -> None:
        self._outputs.append(0)
    
    def get_num_inputs(self) -> int:
        return len(self._inputs)
    
    def get_num_outputs(self) -> int:
        return len(self._outputs)

    def _get_conn(self, port_name):
        _helper_dic = {
            "I": self._input_connections,
            "O": self._output_connections
        }
        return _helper_dic[port_name[0].upper()]

    def connect_wire(self, gate, port_name: str, gate_port_name: str) -> None:
        self._get_conn(gate_port_name).add(
            (gate, port_name, gate_port_name))

    def get_unique_gates(self) -> list:
        return set([gate for gate, _, _ in self._input_connections])

    def get_ports_list(self, port_name: str) -> list:
        _helper_dic = {
            "I": self._inputs,
            "O": self._outputs
        }
        return _helper_dic[port_name[0].upper()]

    def get_port(self, port_name: str) -> bool:
        lst = self.get_ports_list(port_name)
        port_idx = int(port_name[1:])
        if port_idx >= len(lst):
            raise InvalidPortNumber(port_name, len(lst), self.name)
        return lst[port_idx]

    def set_port(self, port_name: str, value: bool) -> None:
        lst = self.get_ports_list(port_name)
        port_idx = int(port_name[1:])
        if port_idx >= len(lst):
            raise InvalidPortNumber(port_name, len(lst), self.name)
        lst[port_idx] = value

    def evaluate(self) -> None:
        for gate, in_port, gate_port in self._input_connections:
            val = self.get_port(in_port)
            gate.set_port(gate_port, val)

        unique_gates = self.get_unique_gates()

        for gate in unique_gates:
            gate.evaluate()

        for gate, out_port, gate_port in self._output_connections:
            val = gate.get_port(gate_port)
            self.set_port(out_port, val)

        return self._outputs