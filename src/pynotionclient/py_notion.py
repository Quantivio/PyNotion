from src.pynotionclient.exceptions import InvalidTokenException
from src.pynotionclient.block import NotionBlock
from src.pynotionclient.comment import NotionComment
from src.pynotionclient.database import NotionDatabase
from src.pynotionclient.page import NotionPage
from src.pynotionclient.user import NotionUser
from src.pynotionclient.utils import logger


class PyNotion:
    def __init__(self, token: str):
        function_name = "Intialize PyNotion Client"
        # Initialize PyNotion client with SECRET_TOKEN or API_TOKEN from Notion. Default value is None
        self.token: str | None = token
        if self.token is None or len(self.token) == 0:
            # Raise error if token is not provided
            logger.error(message="Invalid API token provided", function_name=function_name, file_name="py_notion.py")
            raise InvalidTokenException

        logger.info(message="Successfully intialized PyNotion Client", function_name=function_name, file_name="py_notion.py")
        self.database: NotionDatabase
        self.page: NotionPage
        self.block: NotionBlock
        self.user: NotionUser
        self.comment: NotionComment
        self.__initialize_modules()

    def __initialize_modules(self):
        # Initialize all the classes that correspond to different modules with secret token
        self.database: NotionDatabase = NotionDatabase(token=self.token)
        self.page: NotionPage = NotionPage(token=self.token)
        self.block: NotionBlock = NotionBlock(token=self.token)
        self.user: NotionUser = NotionUser(token=self.token)
        self.comment: NotionComment = NotionComment(token=self.token)
