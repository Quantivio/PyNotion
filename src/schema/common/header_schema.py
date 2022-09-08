import pydantic
from pydantic import Field


class HeaderSchema(pydantic.BaseModel):
    accept: str = Field(default="application/json", alias="Accept", title="Accept",
                        description="Value which defines what type of data is expected in the response.")
    notion_version: str = Field(default="2022-06-28", alias="Notion-Version", title="Notion-Version",
                                description="Value which defines the version of Notion API to be used.")
    content_type: str = Field(default="application/json", alias="Content-Type", title="Content-Type",
                              description="Value which defines the type of content that is being sent in the request.")
    authorization: str = Field(default="Bearer ", alias="Authorization", title="Authorziation",
                               description="Value which defines the authorization token to be used.")
    """
        Header schema that can be used to customize the header for a request.
        :param accept: Value which defines the expected response type of request.
        :param notion_version: Value which defines the version of Notion API to be used.
        :param content_type: Value which defines the type of content that is being sent in the request.
        :param authorization: Value which defines the authorization token to be used.
    """


default_header_schema: HeaderSchema = HeaderSchema()
