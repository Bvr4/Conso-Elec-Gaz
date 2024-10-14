"""Importation functions."""

import requests
import os
import shutil
from io import StringIO
import pandas as pd
import geopandas as gpd
from sqlalchemy.orm import Session
from sqlalchemy import text

from datamodels.pydantic_models import Consumption
from datamodels.sql_models import ConsumptionSQL, DepartmentSQL


def get_df_from_csv(url: str) -> pd.DataFrame:
    """Get DataFrame from distant CSV."""

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


def get_geodf_from_ziped_shape(url: str) -> gpd.GeoDataFrame:
    """Get GeoDataFrame from distant ziped shape file"""

    extract_to = "temp_geom_file"
    zip_path = os.path.join(extract_to, 'data.zip')

    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
        
    response = requests.get(url)

    # Save the zip file
    with open(zip_path, 'wb') as file:
        file.write(response.content)

    gdf = gpd.read_file(zip_path)

    # deleting temp files
    shutil.rmtree(extract_to)

    return gdf


def import_department_gdf_to_db(session: Session, gdf: gpd.GeoDataFrame) -> None:
    """Import department geometry to the database"""

    gdf['geometry'] = gdf.geometry.apply(lambda x: x.wkt)
    
    for _, row in gdf.iterrows():
        departments = DepartmentSQL(
            insee=row["code_insee"],
            name=row["nom"],
            nuts3=row["nuts3"],
            geom=row["geometry"],
        )

        session.add(departments)

        # session.execute(
        # text("""
        #     INSERT INTO departments (insee, name, nuts3, geom) 
        #     VALUES (:insee, :name, :nuts3, ST_GeomFromText(:geom, 4326))
        #     """),
        #     {"insee": row["code_insee"], "name": row["nom"], "nuts3": row["nuts3"], "geom": row["geometry"]}
        # )
        session.commit()
