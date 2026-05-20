from importlib import import_module
from typing import Any


def load_object(module_path: str) -> Any:
    """
    Load a object from a python-style `module_path`.

    :param module_path: Python-style module path.

    :returns: The imported python object.
    """
    module_name, func_name = module_path.rsplit(".", 1)
    module = import_module(module_name)
    return getattr(module, func_name)

