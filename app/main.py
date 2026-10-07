from models import Base,Personagem
from db import engine, SessionLocal
def app ():
    Base.metadata.create_all(engine)
     
    with SessionLocal() as session:
        persogem = Personagem (nome= 'Yuki', nivel=1, ouro= 444)
        session.add(persogem)
        session.commit()
if __name__=='__main__':
    app()