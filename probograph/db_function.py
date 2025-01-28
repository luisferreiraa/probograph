# db_function.py
from typing import Optional

from fastapi import HTTPException
from sqlalchemy.orm import joinedload
from sqlmodel import Session, select
from passlib.context import CryptContext

from probograph.models import User, engine, UserProfileImage, AdType
from probograph.schema import DeleteUserResponse

# Configuração para hash de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def get_users():
    with Session(engine) as session:
        query = select(User).options(joinedload(User.user_profile_image))
        result = session.execute(query).scalars().all()

    return result


def get_user_profile_image(user_id: int):
    with Session(engine) as session:
        query: select = select(UserProfileImage).where(UserProfileImage.user_id == user_id)
        result = session.execute(query).scalar()

        return result


def get_ad_types():
    with Session(engine) as session:
        query = select(AdType)
        result = session.execute(query).scalars().all()

        return result


def create_user(first_name: str, last_name: str, email: str, password: str, phone: int, is_company: bool):
    with Session(engine) as session:
        # Hash da senha antes de armazenar
        hashed_password = hash_password(password)

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_password,
            phone=phone,
            is_company=is_company
        )

        session.add(user)
        session.commit()
        session.refresh(user)

        return user


def create_ad_type(name: str, is_active: bool):
    with Session(engine) as session:
        ad_type = AdType(name=name, is_active=is_active)
        session.add(ad_type)
        session.commit()
        session.refresh(ad_type)

        return ad_type


def update_user(
        user_id: int,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[int] = None,
        is_company: Optional[bool] = None
):
    with Session(engine) as session:
        # Busca o utilizador pelo ID
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail='User not found')

        # Atualiza os campos fornecidos
        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name
        if email is not None:
            user.email = email
        if phone is not None:
            user.phone = phone
        if is_company is not None:
            user.is_company = is_company

        session.add(user)
        session.commit()
        session.refresh(user)

        return user


def delete_user(user_id: int) -> DeleteUserResponse:
    with Session(engine) as session:
        # Busca o utilizador pelo ID
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail='User not found')

        session.delete(user)
        session.commit()

        # Retorna uma instância de DeleteUserResponse
        return DeleteUserResponse(id=user_id, message="User deleted successfully")


def delete_ad_type(ad_type_id: int):
    with Session(engine) as session:
        adtype = session.get(AdType, ad_type_id)
        if not adtype:
            raise HTTPException(status_code=404, detail='AdType not found')
        session.delete(adtype)
        session.commit()

        return DeleteUserResponse(id=ad_type_id, message='AdType deleted successfully')

