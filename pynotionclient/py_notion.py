from pynotionclient.block import NotionBlock
from pynotionclient.comment import NotionComment
from pynotionclient.database import NotionDatabase
from pynotionclient.exceptions import InvalidTokenException
from pynotionclient.page import NotionPage
from pynotionclient.user import NotionUser
from pynotionclient.utils import logger


class PyNotion:
    def __init__(self, token: str):
        function_name = "Initialize PyNotion Client"
        # Initialize PyNotion client with SECRET_TOKEN or API_TOKEN from Notion. Default value is None
        self.token: str | None = token
        if self.token is None or len(self.token) == 0:
            # Raise error if token is not provided
            logger.error(
                message="Invalid API token provided",
                function_name=function_name,
                file_name="py_notion.py",
            )
            raise InvalidTokenException

        logger.info(
            message="Successfully initialized PyNotion Client",
            function_name=function_name,
            file_name="py_notion.py",
        )
        self.database: NotionDatabase
        self.page: NotionPage
        self.block: NotionBlock
        self.user: NotionUser
        self.comment: NotionComment
        self.__initialize_modules()

    def __initialize_modules(self) -> None:
        # Initialize all the classes that correspond to different modules with secret token
        self.database = NotionDatabase(token=self.token)  # type: ignore
        self.page = NotionPage(token=self.token)  # type: ignore
        self.block = NotionBlock(token=self.token)  # type: ignore
        self.user = NotionUser(token=self.token)  # type: ignore
        self.comment = NotionComment(token=self.token)  # type: ignore
