"""Functions to read informations from the database"""

import pandas as pd
import geopandas as gpd
from sqlalchemy.orm import Session
from sqlalchemy import Engine
from geoalchemy2.shape import to_shape

from datamodels.sql_models import ConsumptionSQL, DepartmentSQL


def get_all_departments(session: Session) -> gpd.GeoDataFrame:
    """Get all departments geometries from the database"""

    # get departments from DB
    departments = session.query(DepartmentSQL).all()

    # convert to GeoDataFrame
    data = []
    for department in departments:
        geom = to_shape(department.geom)
        data.append({
            'insee': department.insee,
            'name': department.name,
            'nuts3': department.nuts3,
            'geometry': geom
        })

    gdf = gpd.GeoDataFrame(data, geometry='geometry')

    gdf.set_crs(epsg=4326, inplace=True)

    return gdf


def get_all_consumptions(connexion: Engine) -> pd.DataFrame:
    """Get all consumptions from the database"""

    # get consumptions from DB
    query = f"SELECT * FROM {ConsumptionSQL.__tablename__}"

    df = pd.read_sql_query(query, con=connexion)

    return df


def get_consumptions_by_year(connexion: Engine, year: int) -> pd.DataFrame:
    """Get all consumptions from the database, for a given year"""

    # get consumptions from DB
    query = f"SELECT * FROM {ConsumptionSQL.__tablename__} WHERE year = {year}"

    df = pd.read_sql_query(query, con=connexion)

    return df


def get_consumptions_by_department(connexion: Engine, department_code: int) -> pd.DataFrame:
    """Get all consumptions from the database, for a given department"""

    # get consumptions from DB
    query = f"SELECT * FROM {ConsumptionSQL.__tablename__} WHERE department_code = {department_code}"

    df = pd.read_sql_query(query, con=connexion)

    return df