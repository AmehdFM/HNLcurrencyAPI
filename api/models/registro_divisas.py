from pydantic import BaseModel, Field

class RegistroDivisaRequest(BaseModel):
    fecha: str = Field(description="Date of the currency exchange rate (YYYY-MM-DD)")
    divisa: str = Field(max_length=3, description="Currency code (USD, EUR, etc.)")
    tasa_cambio: float = Field(gt=0, description="Exchange rate of the currency")

class RegistroDivisaResponse(BaseModel):
    id: int
    fecha: str = Field(format="date")
    divisa: str = Field(max_length=3)
    tasa_cambio: float
