from typing import Any, Callable
import uuid


def change_function_name(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__ + uuid.uuid4().hex
    return wrapper
