"""SQLAlchemy definition of the consummption database schema."""

from datetime import datetime, timezone
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class CreatedMixin:
    """Mixin to add created datetime to model."""

    created_utc = sa.Column(sa.DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))


class ConsumptionSQL(Base, CreatedMixin):
    """Class representing the consumption table."""
    __tablename__ = "consumptions"

    provider = sa.column(sa.String(255), comment="Energy provider")
    year = sa.column(sa.Integer, comment="Year of consuption")
    sector = sa.column(sa.String(255), comment="Type of energy")
    agri_cons = sa.column(sa.Float, comment="Consumption attributed to agriculture")
    agri_pos_count = sa.column(sa.Integer, comment="number of agricultural points of supply")
    indus_cons = sa.column(sa.Float, comment="Consumption attributed to industry")
    indus_pos_count = sa.column(sa.Integer, comment="number of industrial points of supply")
    terc_cons = sa.column(sa.Float, comment="Consumption attributed to tertiary industry")
    terc_pos_count = sa.column(sa.Integer, comment="number of tertiary industry points of supply")
    resid_cons = sa.column(sa.Float, comment="Consumption attributed to residential")
    resid_pos_count = sa.column(sa.Integer, comment="number of residential points of supply")
    other_cons = sa.column(sa.Float, comment="Consumption attributed to other")
    other_pos_count = sa.column(sa.Integer, comment="number of other points of supply")
    department_code = sa.column(sa.String(3), comment="Department code")
    departement_name = sa.column(sa.String(255), comment="Department name")
    region_code = sa.column(sa.Integer, comment="Region code")
    region_name = sa.column(sa.String(255), comment="Region name")
    total_cons = sa.column(sa.Float, comment="Total consuption")