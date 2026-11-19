from pydantic import BaseModel, Field


class IrisInput(BaseModel):
    sepal_length: float = Field(gt=0, le=15, description="Longitud del sépalo en cm (ej. 5.1)")
    sepal_width: float = Field(gt=0, le=15, description="Ancho del sépalo en cm (ej. 3.5)")
    petal_length: float = Field(gt=0, le=15, description="Longitud del pétalo en cm (ej. 1.4)")
    petal_width: float = Field(gt=0, le=15, description="Ancho del pétalo en cm (ej. 0.2)")
