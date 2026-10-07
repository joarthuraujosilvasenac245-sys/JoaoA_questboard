from sqlalchemy import create_enegine
from sqlalchemy.orm import sessionmaker

engine =  create_enegine('postgresql+psycong://postgres:@0000@localhost:5432/quest_board')

SessionLocal = sessionmaker(bind = engine)