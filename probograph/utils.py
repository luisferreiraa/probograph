# utils.py
from sqlmodel import Session
from probograph.models import engine


# Função de dependência para obter a sessão da base de dados
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
