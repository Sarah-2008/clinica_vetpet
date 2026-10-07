from sqlalchemy import Column, Integer, String, Boolean, Float
from app.database import Base

class Tutor(Base):
    __tablename__ = 'Tutor' # nome da tabela no banco

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String(100), nullable=False)
    telefone = Column(String(20), default=True)
    email = Column(String(100), unique=True)

    def __repr__(self):
        return f'<Tutor id={self.id} nome_completo={self.nome}>'

class Animal(Base):
    __tablename__ = 'Animal'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_animal = Column(String(60), nullable=False)
    especie = Column(String(40), nullable=False)
    raca = Column(String(60), default=True)
    peso_kg  = Column(Float, nullable=False)
    tutor_id  = Column(Integer, foreign_key=("tutor_id"))

    def __repr__(self):
        return f'<Animal {self.titulo} {self.nome_animal}>'
    
class Atendimento(Base):
    __tablename__ = 'Atendimento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_atend = Column(String(10), nullable=False)
    motivo = Column(String(200), nullable=False)
    valor_cons = Column(Float, nullable=True)
    animal_id = Column(Float, nullable=False)
    ativo = Column(Integer, foreign_key=('Animal.id'))
    
    def __repr__(self):
        return f'<Atendimento id={self.id} nome={self.nome}>'