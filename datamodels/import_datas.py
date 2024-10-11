"""Importation functions."""

import pandas as pd
import requests
from io import StringIO
from sqlalchemy.orm import Session

from datamodels.pydantic_models import Consumption
from datamodels.sql_models import ConsumptionSQL


def get_df_from_csv(url: str) -> pd.DataFrame:
    """Get dataframe from distant CSV."""

    response = requests.get(url)
    data = StringIO(response.text)
    df = pd.read_csv(data, sep=";")
    return df


def import_consumption_df_to_db(session: Session, df: pd.DataFrame) -> None:
    """Import consumption dataframe to the database, performing pydantic validations"""

    for _, row in df.iterrows():
        try:
            validated_cons_data = Consumption(
                provider=row["operateur"],
                year=row["annee"],
                sector=row["filiere"],
                agri_cons=row["consoa"],
                agri_pos_count=row["pdla"],
                indus_cons=row["consoi"],
                indus_pos_count=row["pdli"],
                terc_cons=row["consot"],
                terc_pos_count=row["pdlt"],
                resid_cons=row["consor"],
                resid_pos_count=row["pdlr"],
                other_cons=row["consona"],
                other_pos_count=row["pdlna"],
                department_code=row["code_departement"],
                departement_name=row["libelle_departement"],
                region_code=row["code_region"],
                region_name=row["libelle_region"],
                total_cons=row["consototale"],
            )

            consumption = ConsumptionSQL(**validated_cons_data.model_dump())
            session.add(consumption)
            session.commit()

        except ValueError as e:
            print(f"Validation error: {e}")
