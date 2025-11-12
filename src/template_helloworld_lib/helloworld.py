from typing import Optional


def tell_me_hello_world(name : Optional[str] = None) -> str:
    if name:
        return f"Hello World, {name}!"
    return "Hello World!"

