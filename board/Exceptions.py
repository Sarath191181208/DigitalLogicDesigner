from colorama import Style, Fore

class Error(Exception):
    def __init__ (self, msg):
        super().__init__(f"{Fore.RED} {msg} {Style.RESET_ALL}")

class InvalidPortNumber(Error):
    def __init__(self, port_name: str, max_ports: int, name: str):
        super().__init__(f'''
Port index out of range !
------------------------
Given port:     {port_name} 
Maximum port:   {f'{port_name[0]}{max_ports-1}'} 
In {name} gate
'''
        )