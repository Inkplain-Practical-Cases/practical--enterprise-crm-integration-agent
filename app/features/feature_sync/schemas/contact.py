"""Contact contract. Why: rejects malformed external identifiers and limits tenant crossover."""
from pydantic import BaseModel, Field
class Contact(BaseModel):
    tenant_id: str = Field(min_length=1)
    external_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
