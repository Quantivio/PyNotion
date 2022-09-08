from dotenv import load_dotenv

from config import base_config
from src.pynotionclient import PyNotion

load_dotenv()
py_notion_client = PyNotion(token=base_config.notion_secret_token)
py_notion_client.database.query_database(database_id="28004d693dd64da99b4cbdc08a79094e")
