from pydantic import BaseModel


class ProductRequest(BaseModel):
    title: str
    price: float
    description: str
    category: str
    thumbnail: str
