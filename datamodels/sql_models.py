"""SQLAlchemy definition of the consummption database schema."""

import uuid
from datetime import datetime, timezone
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy_guid import GUID


Base = declarative_base()


class CreatedMixin:
    """Mixin to add created datetime to model."""

    created_utc = sa.Column(sa.DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))


class ConsumptionSQL(Base, CreatedMixin):
    """Class representing the consumption table."""

    __tablename__ = "consumptions"

    guid = sa.Column(GUID(), primary_key=True, default=uuid.uuid4)
    provider = sa.Column(sa.String(255), index=True, comment="Energy provider")
    year = sa.Column(sa.Integer, index=True, comment="Year of consuption")
    sector = sa.Column(sa.String(255), index=True, comment="Type of energy")
    agri_cons = sa.Column(sa.Float, comment="Consumption attributed to agriculture")
    agri_pos_count = sa.Column(sa.Integer, comment="number of agricultural points of supply")
    indus_cons = sa.Column(sa.Float, comment="Consumption attributed to industry")
    indus_pos_count = sa.Column(sa.Integer, comment="number of industrial points of supply")
    terc_cons = sa.Column(sa.Float, comment="Consumption attributed to tertiary industry")
    terc_pos_count = sa.Column(sa.Integer, comment="number of tertiary industry points of supply")
    resid_cons = sa.Column(sa.Float, comment="Consumption attributed to residential")
    resid_pos_count = sa.Column(sa.Integer, comment="number of residential points of supply")
    other_cons = sa.Column(sa.Float, comment="Consumption attributed to other")
    other_pos_count = sa.Column(sa.Integer, comment="number of other points of supply")
    department_code = sa.Column(sa.String(3), index=True, comment="Department code")
    departement_name = sa.Column(sa.String(255), index=True, comment="Department name")
    region_code = sa.Column(sa.Integer, index=True, comment="Region code")
    region_name = sa.Column(sa.String(255), index=True, comment="Region name")
    total_cons = sa.Column(sa.Float, comment="Total consuption")