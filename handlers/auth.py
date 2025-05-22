from fastapi import APIRouter, Depends, HTTPException, status
from schema import UserLoginSchema, UserCreateSchema
from dependencies import get_auth_service
from service.auth import AuthService
from exception import UserNotFoundException, UserNotCorrectPasswordException

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/login",
    response_model=UserLoginSchema
)
async def login_user(
        body: UserCreateSchema,
        auth_service: AuthService = Depends(get_auth_service)
):
    try:
        user_login_data = auth_service.login(body.username, body.password)
    except UserNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )
    except UserNotCorrectPasswordException as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=e.detail
        )
    else:
        return user_login_data

