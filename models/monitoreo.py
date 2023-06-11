from typing import Optional
from pydantic import BaseModel

class Monitoreo(BaseModel):
    _id: Optional[str]
    lugar: str
    autor: str
    temperatura: float
    humedad: float
    createdAt: Optional[str]
    updatedAt: Optional[str]

