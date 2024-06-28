class InvalidTokenException(Exception):
    def __init__(self) -> None:
        self.message = "Invalid API Token provided. Cannot initialize PyNotion Client."
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.message}"

    def __repr__(self) -> str:
        return f"{self.message}"
