from typing import Optional

from sqlmodel import Session, select

from app.models.users import Users


class UserRepository:
    def get_by_username(self, session: Session, username: str) -> Optional[Users]:
        statement = select(Users).where(Users.username == username)
        result = session.exec(statement).first()
        return result

    def get_by_email(self, session: Session, email: str) -> Optional[Users]:
        statement = select(Users).where(Users.email == email)
        result = session.exec(statement).first()
        return result

    def create_user(self, session: Session, user: Users) -> Users:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def increment_token_version(self, session: Session, user: Users) -> Users:
        try:
            current_version = int(user.token_version) if user.token_version is not None else 0
        except (TypeError, ValueError):
            current_version = 0
        user.token_version = current_version + 1
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

