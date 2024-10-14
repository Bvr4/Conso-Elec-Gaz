from datamodels.connection import DatabaseConnection
from datamodels.sql_models import ConsumptionSQL
from datamodels.import_datas import get_df_from_csv, import_consumption_df_to_db


def initial_consumptions_import() -> None:
    """Initial consumption import. Loads datas from the source and store them in the database. Erases previous datas."""

    # Connect to the database
    con = DatabaseConnection()
    session=con.get_session()

    # Delete previous datas
    session.query(ConsumptionSQL).delete()
    session.commit()

    # Get consumptions dataset. See https://www.data.gouv.fr/fr/datasets/consommation-annuelle-delectricite-et-gaz-par-departement-et-par-secteur-dactivite/ for more informations
    df = get_df_from_csv("https://www.data.gouv.fr/fr/datasets/r/e455db41-28c2-419d-bdf1-d44635fdc97e")

    import_consumption_df_to_db(session=session, df=df, since_year=2020)