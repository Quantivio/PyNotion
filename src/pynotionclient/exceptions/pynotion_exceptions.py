class InvalidTokenException(Exception):
    def __init__(self):
        self.message = "Invalid API Token provided. Cannot initialize PyNotion Client."
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"

    def __repr__(self):
        return f"{self.message}"
