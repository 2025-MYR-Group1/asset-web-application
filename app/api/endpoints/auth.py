from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status

from app.api.dependencies import get_auth_service
from app.core.settings import Settings
from app.db.session import SessionDep
from app.schemas.auth import LoginRequest, SignupRequest, TokenResponse
from app.schemas.response import ApiResponse
from app.schemas.user import UserRead
from app.services.auth_service import AuthService


router = APIRouter()
settings = Settings()


def _set_auth_cookies(response: Response, access_token: str, refresh_token: str) -> None:
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=settings.cookie_secure,
        samesite=settings.cookie_samesite,
        domain=settings.cookie_domain,
        max_age=settings.access_token_expires_minutes * 60,
        path="/",
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=settings.cookie_secure,
        samesite=settings.cookie_samesite,
        domain=settings.cookie_domain,
        max_age=settings.refresh_token_expires_days * 24 * 60 * 60,
        path="/",
    )


def _clear_auth_cookies(response: Response) -> None:
    response.delete_cookie(key="access_token", domain=settings.cookie_domain, path="/")
    response.delete_cookie(key="refresh_token", domain=settings.cookie_domain, path="/")


@router.post("/signup", response_model=ApiResponse[UserRead], status_code=status.HTTP_201_CREATED)
def signup(
    payload: SignupRequest,
    response: Response,
    session: SessionDep,
    auth_service: AuthService = Depends(get_auth_service),
) -> ApiResponse[UserRead]:
    user = auth_service.signup(session, username=payload.username, email=payload.email, password=payload.password)
    data = UserRead(id=user.id, username=user.username, email=user.email, role=user.role, created_at=user.created_at)
    message = "User created successfully"
    return ApiResponse(success=True, data=data, message=message)


@router.post("/login", response_model=ApiResponse[TokenResponse])
def login(
    payload: LoginRequest,
    response: Response,
    session: SessionDep,
    auth_service: AuthService = Depends(get_auth_service),
) -> ApiResponse[TokenResponse]:
    user, access, refresh = auth_service.login(session, username=payload.username, password=payload.password)
    _set_auth_cookies(response, access, refresh)
    token_data = TokenResponse(access_token=access, refresh_token=refresh, token_type="bearer", user=UserRead(
        id=user.id, username=user.username, email=user.email, role=user.role, created_at=user.created_at
    ))
    message = "Logged in successfully"
    return ApiResponse(success=True, data=token_data, message=message)


@router.post("/logout", response_model=ApiResponse[None])
def logout(
    request: Request,
    response: Response,
    session: SessionDep,
    auth_service: AuthService = Depends(get_auth_service),
) -> ApiResponse[None]:
    refresh_token: Optional[str] = request.cookies.get("refresh_token")
    if not refresh_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    user = auth_service.get_user_from_refresh(session, refresh_token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    auth_service.logout(session, user)
    _clear_auth_cookies(response)
    return ApiResponse(success=True, data=None, message="Logged out successfully")


