from loguru import logger

from . import NotionDatabase, NotionPage
from .block import NotionBlock
from .comment import NotionComment
from .core import InvalidTokenException
from .user import NotionUser


class PyNotion:
	def __init__(self, token: str):
		# Initialize PyNotion client with SECRET_TOKEN or API_TOKEN from Notion. Default value is None
		self.token: str | None = token
		if self.token is None or len(self.token) == 0:
			# Raise error if token is not provided
			logger.error(
				"Invalid API token provided",
			)
			raise InvalidTokenException

		logger.info(
			"Successfully initialized PyNotion Client",
		)
		self.database: NotionDatabase
		self.page: NotionPage
		self.block: NotionBlock
		self.user: NotionUser
		self.comment: NotionComment
		self.__initialize_modules()

	def __initialize_modules(self) -> None:
		# Initialize all the classes that correspond to different modules with secret token
		self.database = NotionDatabase(token=self.token)
		self.page = NotionPage(token=self.token)
		self.block = NotionBlock(token=self.token)
		self.user = NotionUser(token=self.token)
		self.comment = NotionComment(token=self.token)
