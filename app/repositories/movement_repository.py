from typing import List, Optional

from sqlmodel import Session, select

from app.models.movements import Movements


class MovementRepository:

    def list_movements(self, session: Session) -> List[Movements]:
        query = select(Movements)
        return list(session.exec(query).all())

    def list_movements_by_asset(
        self, session: Session, asset_id: int
    ) -> List[Movements]:
        query = select(Movements).where(Movements.asset_id == asset_id)
        return list(session.exec(query).all())

    def list_movements_by_user(self, session: Session, user_id: int) -> List[Movements]:
        query = select(Movements).where(Movements.renter_id == user_id)
        return list(session.exec(query).all())

    def create_movement(self, session: Session, movement: Movements) -> Movements:
        session.add(movement)
        session.commit()
        session.refresh(movement)
        return movement

    def save_movement(self, session: Session, movement: Movements) -> Movements:
        session.add(movement)
        session.commit()
        session.refresh(movement)
        return movement

    def get_movement_by_asset(
        self, session: Session, asset_id: int
    ) -> Optional[Movements]:
        query = (
            select(Movements)
            .where(
                Movements.asset_id == asset_id,
                Movements.return_date.is_(None),
            )
            .order_by(Movements.rental_date.desc())
        )
        return session.exec(query).first()
