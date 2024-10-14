from datamodels.connection import DatabaseConnection
from datamodels.sql_models import DepartmentSQL
from datamodels.import_datas import get_geodf_from_ziped_shape, import_department_gdf_to_db


def initial_dept_geom_import() -> None:
    """Initial departement geometry immport. Loads datas from the source and store them in the database. Erases previous datas."""
    
    # Connect to the database
    con = DatabaseConnection()
    session=con.get_session()

    # Delete previous datas
    session.query(DepartmentSQL).delete()
    session.commit()

    # Import simplified department geometry. See https://www.data.gouv.fr/fr/datasets/contours-des-departements-francais-issus-d-openstreetmap/ for more informations
    gdf = get_geodf_from_ziped_shape("https://www.data.gouv.fr/fr/datasets/r/6e53bca5-1153-49d4-bff5-dd69f39369b5")

    import_department_gdf_to_db(session=session, gdf=gdf)
