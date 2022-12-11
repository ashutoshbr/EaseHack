from pydantic import BaseModel


class PostHome(BaseModel):
    encoded_data: str
