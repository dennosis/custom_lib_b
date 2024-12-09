from typing import Callable


def recursive_extrator_dict(d, callback: Callable[[str], list[str]]):
    extrated = []
    for _, value in d.items():
        if isinstance(value, dict):
            extrated = extrated + recursive_extrator_dict(value, callback)
        elif isinstance(value, list):
            for i_value in value:
                extrated = extrated + recursive_extrator_dict(i_value, callback)
        else:
            extrated = extrated + callback(value)
    return extrated
