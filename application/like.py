from typing import Dict

class Like:

    def __init__(self, **kwargs) -> None:
        self.id = kwargs['id']
        self.username = kwargs['username']