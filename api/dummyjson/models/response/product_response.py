from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    title: str
    description: str
    price: float
    discountPercentage: float | None = None
    rating: float | None = None
    stock: int | None = None
    brand: str | None = None
    category: str | None = None
    thumbnail: str | None = None
