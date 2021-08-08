from typing import Dict

class Like:
    def __init__(self, id: str, username: str) -> None:
        self.id = id
        self.username = username

    def __init__(self, dict: Dict[str, str]) -> None:
        self.id = dict['id']
        self.username = dict['username']