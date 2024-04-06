from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import User
from app.schemas import DonationCreate, DonationDB
from app.services.investing import run_investing_process

router = APIRouter()


@router.get(
    '/',
    response_model=list[DonationDB],
    dependencies=[Depends(current_superuser)],
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    all_donations = await donation_crud.get_multi(session)
    return all_donations


@router.post(
    '/',
    response_model=DonationDB,
    response_model_exclude={'invested_amount', 'fully_invested', 'close_date', 'user_id'}
)
async def create_new_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    new_donation = await donation_crud.create(donation, session, user)
    return await run_investing_process(new_donation, session)


@router.get(
    '/my',
    response_model=list[DonationDB],
    response_model_exclude={'user_id',
                            'invested_amount',
                            'fully_invested',
                            'close_date'},
)
async def get_user_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    donations = await donation_crud.get_by_user(
        session=session,
        user=user
    )
    return donations
