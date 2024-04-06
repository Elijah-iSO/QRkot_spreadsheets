from datetime import datetime
from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import get_obj_investing
from app.models import CharityProject, Donation


async def run_investing_process(
    obj_created: Union[CharityProject, Donation],
    session: AsyncSession,
):
    process_db_model = (
        Donation if isinstance(obj_created, CharityProject) else CharityProject
    )
    obj_investing = await get_obj_investing(process_db_model, session)
    money = obj_created.full_amount

    if obj_investing:
        for obj in obj_investing:
            need = obj.full_amount - obj.invested_amount
            if money > need:
                will_invest = need
            else:
                will_invest = money
            obj.invested_amount += will_invest
            obj_created.invested_amount += will_invest
            money -= will_invest

            if obj.full_amount == obj.invested_amount:
                obj.fully_invested = True
                obj.close_date = datetime.now()

            if money == 0:
                obj_created.fully_invested = True
                obj_created.close_date = datetime.now()

        await session.commit()
        await session.refresh(obj_created)

    return obj_created