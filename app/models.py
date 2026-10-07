from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

class Base(DeclarativeBase):
    pass

class Personagem(Base):
    __tablename__ = 'personagens'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    nivel: Mapped[int]
    ouro: Mapped[int]
    