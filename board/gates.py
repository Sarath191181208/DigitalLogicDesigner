from copy import deepcopy
from .board_dic import get_empty_gate

AND = lambda:  deepcopy(get_empty_gate("AND", 2, 1))
OR = lambda: deepcopy(get_empty_gate("OR", 2, 1))
NOT = lambda: deepcopy(get_empty_gate("NOT", 1, 1))

# from .board import BaseGate

# class Board(BaseGate):
#     pass

# class OR(BaseGate):
#     def __init__(self) -> None:
#         super().__init__(name="OR", num_inputs=2, num_outputs=1)

#     def evaluate(self) -> None:
#         self._outputs[0] = bool(self._inputs[0] or self._inputs[1])
#         super().evaluate()


# class AND(BaseGate):
#     def __init__(self) -> None:
#         super().__init__(name="AND", num_inputs=2, num_outputs=1)

#     def evaluate(self) -> None:
#         self._outputs[0] = bool(self._inputs[0] and self._inputs[1])
#         super().evaluate()


# class NOT(BaseGate):
#     def __init__(self) -> None:
#         super().__init__(name="NOT", num_inputs=1, num_outputs=1)

#     def evaluate(self) -> None:
#         self._outputs[0] = bool(not self._inputs[0])
#         super().evaluate()

# class XOR(BaseGate):
#     def __init__(self) -> None:
#         super().__init__(name="XOR", num_inputs=2, num_outputs=1)

#     def evaluate(self) -> None:
#         self._outputs[0] = bool(self._inputs[0] != self._inputs[1])
#         super().evaluate()

# NOR = BaseGate("NOR")
# NOR.add_input()
# NOR.add_input()

# NOR.add_output()

# NOR_OR = OR()  
# NOR.connect_wire(NOR_OR, "I0", "I0")
# NOR.connect_wire(NOR_OR, "I1", "I1")

# NOR_NOT = NOT()
# NOR_OR.connect_wire(NOR_NOT, "O0", "I0")

# NOR.connect_wire(NOR_NOT, "O0", "O0")



