from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase): # Tabela em branco
    
    pass # ignorar a implemntaçao

class Personagem(Base): # Construir em cima tabela em branco
    __tablename__ = 'personagens' # Define o nome da tabela
    

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    nivel: Mapped[int]
    ouro: Mapped[int]
    def __repr__(self):
        return f'Personagem(id={self.id}, nome ={self.nome}, nivel={self.nivel}, ouro={self.ouro})'