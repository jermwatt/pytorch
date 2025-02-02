# Get the type definitions from both multiprocessing and the local spawn module
from multiprocessing import *
from .spawn import *

# Type annotations for the functions defined in the torch.multiprocessing module
from typing import Set

def set_sharing_strategy(new_strategy: str) -> None: ...
def get_sharing_strategy() -> str: ...
def get_all_sharing_strategies() -> Set[str]: ...
