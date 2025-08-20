from datetime import datetime, timezone
from typing import List, Optional

from sqlmodel import Session

from app.models.movements import Movements
from app.repositories.movement_repository import MovementRepository
from app.schemas.movement import CheckoutRequest


class MovementService:
    def __init__(self, repository: MovementRepository) -> None:
        self._repository = repository

    def checkout_asset(
        self, session: Session, asset_id: int, payload: CheckoutRequest
    ) -> Movements:
        movement = Movements(
            asset_id=asset_id,
            renter_id=payload.renter_id,
            purpose=payload.purpose,
            rental_date=datetime.now(timezone.utc),
            return_due_date=payload.return_due_date,
            status="checked-out",
            approval_status="approved",
        )
        return self._repository.create_movement(session, movement)

    def checkin_asset(self, session: Session, asset_id: int) -> Optional[Movements]:
        movement = self._repository.get_movement_by_asset(session, asset_id)
        if movement is None:
            return None
        movement.return_date = datetime.now(timezone.utc)
        movement.status = "checked-in"
        return self._repository.save_movement(session, movement)

    def list_asset_movements(self, session: Session, asset_id: int) -> List[Movements]:
        return self._repository.list_movements_by_asset(session, asset_id)

    def list_user_movements(self, session: Session, user_id: int) -> List[Movements]:
        return self._repository.list_movements_by_user(session, user_id)

    def list_all_movements(self, session: Session) -> List[Movements]:
        return self._repository.list_movements(session)
