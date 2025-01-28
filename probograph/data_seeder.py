# data_seeder.py
from sqlmodel import Session

from probograph.models import AdType, Floor, PropertyType, PropertySubType, EnergyClass, Condition, State, City, \
    Neighborhood


def seed_data(session: Session, model, data: list):
    """
    Função genérica para inserir dados numa tabela se estiver vazia.

    Args:
        session (Session): Sessão do banco de dados.
        model: Modelo SQLModel da tabela.
        data (list): Lista de instâncias do modelo para inserir.
    """

    if session.query(model). count() == 0:
        session.add_all(data)
        session.commit()
        print(f"{model.__name__} successfully seeded!")
    else:
        print(f"{model.__name__} already contains data.")


def seed_all_data(session: Session):
    # Dados para AdType
    adtypes = [
        AdType(name='For Sale'),
        AdType(name='For Rent')
    ]

    floors = [
        Floor(name='Basement'),
        Floor(name='Ground Floor'),
        Floor(name='1'),
        Floor(name='2'),
        Floor(name='3'),
        Floor(name='4'),
        Floor(name='5'),
        Floor(name='6'),
        Floor(name='7'),
        Floor(name='8'),
        Floor(name='9'),
        Floor(name='10')
    ]

    property_types = [
        PropertyType(name='Apartment, Penthouse or Duplex'),
        PropertyType(name='House'),
        PropertyType(name='Farm'),
        PropertyType(name='Loft'),
        PropertyType(name='Palace'),
        PropertyType(name='Mansion'),
        PropertyType(name='Villa')
    ]

    property_sub_types = [
        PropertySubType(name='Apartment', property_type_id=1),
        PropertySubType(name='Penthouse', property_type_id=1),
        PropertySubType(name='Duplex', property_type_id=1),
        PropertySubType(name='Isolated', property_type_id=2),
        PropertySubType(name='Semi-Detached', property_type_id=2),
        PropertySubType(name='Townhouse', property_type_id=2),
        PropertySubType(name='Rustic House', property_type_id=2)
    ]

    energy_classes = [
        EnergyClass(name='A+'),
        EnergyClass(name='A'),
        EnergyClass(name='B'),
        EnergyClass(name='B-'),
        EnergyClass(name='C'),
        EnergyClass(name='D'),
        EnergyClass(name='E'),
        EnergyClass(name='F'),
    ]

    conditions = [
        Condition(name='New Construction'),
        Condition(name='Good Condition'),
        Condition(name='To Renovate')
    ]

    states = [
        State(name='Massachussets')
    ]

    cities = [
        City(name='Boston')
    ]

    # Seed para AdType
    seed_data(session, AdType, adtypes)

    # Seed para Floor
    seed_data(session, Floor, floors)

    # Seed para PropertyType
    seed_data(session, PropertyType, property_types)

    # Seed para PropertySubType
    seed_data(session, PropertySubType, property_sub_types)

    # Seed para EnergyClass
    seed_data(session, EnergyClass, energy_classes)

    # Seed para Condition
    seed_data(session, Condition, conditions)

    # Seed para State
    seed_data(session, State, states)

    # Seed para City
    seed_data(session, City, cities)

