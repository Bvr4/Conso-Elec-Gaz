""" Pydantic models."""

from pydantic import BaseModel, Field, field_validator


class Consumption(BaseModel):
    """Pydantic Model for consumptions"""
    
    provider: str = Field(..., description="Energy provider")
    year: int = Field(..., description="Year of consumption")
    sector: str = Field(..., description="Type of energy")
    agri_cons: float = Field(..., description="Consumption attributed to agriculture")
    agri_pos_count: int = Field(..., description="number of agricultural points of supply")
    indus_cons: float = Field(..., description="Consumption attributed to industry")
    indus_pos_count: int = Field(..., description="number of industrial points of supply")
    terc_cons: float = Field(..., description="Consumption attributed to tertiary industry")
    terc_pos_count: int = Field(..., description="number of tertiary industry points of supply")
    resid_cons: float = Field(..., description="Consumption attributed to residential")
    resid_pos_count: int = Field(..., description="number of residential points of supply")
    other_cons: float = Field(..., description="Consumption attributed to other")
    other_pos_count: int = Field(..., description="number of other points of supply")
    department_code: str = Field(..., description="Department code")
    departement_name: str = Field(..., description="Department name")
    region_code: int = Field(..., description="Region code")
    region_name: str = Field(..., description="Region name")
    total_cons: float = Field(..., description="Total consumption")

    @field_validator("agri_cons", "indus_cons", "terc_cons", "resid_cons", "other_cons", "total_cons")
    def check_value_positive(cls, v):
        if v < 0:
            raise ValueError("Consumption value mustn't be negative")
        return v
    
    @field_validator("sector")
    def check_sector(cls, v):
        if v == "Electricité":
            return "electricity"
        elif v == "Gaz":
            return "gas"
        else:
            raise ValueError("Invalid sector value")


