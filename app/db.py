from sqlalchemy import create_engine # Funçao de cria a conexao  com bd
from sqlalchemy.orm import sessionmaker # Sessao (Documento para criar os personagens)

engine = create_engine('postgresql+psycopg://postgres:0000@localhost:5432/quest_board') #bibliotecas: // usuario_do_ba


SessionLocal = sessionmaker(bind=engine) # Cria a sessao com base na ponte com o bd