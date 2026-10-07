from models import Base, Personagem # importa a tabela vazia e a tabela personagem
from db import engine, SessionLocal # importa a ponte e o arquivo de esboço

def app():
    Base.metadata.create_all(engine)
    
    # Sessionlocal e responsavel por  criar o "arquivo"
    with SessionLocal() as session:
        personagem = Personagem(nome='Joao', nivel=1, ouro=100)
#criaçao de um objeto no python, ainda nao existe no BD
        session.add(personagem)
        session.flush()
        print(personagem)
        #session.commit()#Responsavel por modificar o banco de dados

if __name__ == '__main__':
    app() #Inicio do programa , responsavel por chamar a liha 4