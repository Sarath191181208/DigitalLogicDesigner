from test_components import fails 
from colorama import Fore, Style

if not fails:
    print(Fore.GREEN, "All Pass! Yay!", Style.RESET_ALL)
else:
    print(Fore.RED, "Failed! :", fails, Style.RESET_ALL)