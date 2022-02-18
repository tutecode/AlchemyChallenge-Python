import db

from sqlalchemy import Column, Integer, String, Float

"""CREATE TABLE cultural (
    cod_localidad INTEGER,
    id_provincia INTEGER,
    id_departamento INTEGER,
    categoria TEXT,
    provincia TEXT,
    localidad TEXT,
    nombre TEXT,
    domicilio TEXT,
    cod_postal TEXT,
    num_telefono INTEGER,
    mail TEXT,
    web TEXT
);"""

class Cultural(db.Base):
    __tablename__ = 'cultural'

    cod_localidad = Column(Integer)
    id_provincia = Column(Integer, nullable=False)
    id_departamento = Column(Integer)
    categoria = Column(String)
    provincia = Column(String)
    localidad = Column(String)
    nombre = Column(String)
    domicilio = Column(String)
    cod_postal = Column(String)
    num_telefono = Column(Integer)
    mail = Column(String)
    web = Column(String)


    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f'Producto({self.nombre}, {self.precio})'

    def __str__(self):
        return self.nombre