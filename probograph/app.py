# app.py
from fastapi import FastAPI
import strawberry
from sqlmodel import Session
from strawberry.fastapi import GraphQLRouter

from probograph.data_seeder import seed_all_data
from probograph.models import engine
from probograph.resolvers import Query, Mutation

# Configuraçao do Schema
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)


# Configuração do FastAPI
app = FastAPI()
app.include_router(graphql_app, prefix='/graphql')


# Dependency: cria e fecha a sessão automaticamente
def get_session():
    with Session(engine) as session:
        yield session


# Chama o seeder ao iniciar a aplicação
@app.on_event('startup')
def startup_event():
    with Session(engine) as session:
        seed_all_data(session)
