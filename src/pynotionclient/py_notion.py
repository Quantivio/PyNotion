from src.exceptions import InvalidTokenException
from src.utils import logger


class PyNotion:
    def __init__(self, token: str):
        function_name = "Intialize PyNotion Client"
        # Initialize PyNotion client with SECRET_TOKEN or API_TOKEN from Notion
        self.token: str = 1
        if token is None or len(token) == 0:
            # Raise error if token is not provided
            logger.error(message="Invalid API token provided", function_name=function_name, file_name="py_notion.py")
            raise InvalidTokenException
        logger.info(message="Successfully intialized PyNotion Client", function_name=function_name, file_name="py_notion.py")

    def sample(self) -> int:
        print(self.token)
        return "a"
