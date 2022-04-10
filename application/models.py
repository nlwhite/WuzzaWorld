
from application import app
# The database connections and session management are managed with SQLAlchemy functions
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# The Geometry columns of the data tables are added to the ORM using the Geometry data type
from geoalchemy2 import Geometry

# Connect to the database called chapter11 using SQLAlchemy functions
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Street(Base):
    __tablename__ = 'streets'
    gid = Column(Integer, primary_key=True, index=True)
    street = Column(String, index=True)
    geom = Column(Geometry(geometry_type='POINT', srid=4326))
