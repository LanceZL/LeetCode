from typing import Any


class Case:
    """Provides a basic abstraction for test cases."""

    def __init__(self, params: Any, expect: Any) -> None:
        self.params = params
        self.expect = expect
