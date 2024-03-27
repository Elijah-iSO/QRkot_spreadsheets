from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models.charity_project import CharityProject
from app.schemas import CharityProjectUpdate


async def check_name_duplicate(
    project_name: str,
    session: AsyncSession,
) -> None:
    project_id = await charity_project_crud.get_project_id_by_name(project_name, session)
    if project_id is not None:
        raise HTTPException(
            status_code=400,
            detail='Проект с таким именем уже существует!',
        )


async def check_project_exists(
    project_id: int,
    session: AsyncSession,
) -> CharityProject:
    project = await charity_project_crud.get(
        project_id, session
    )
    if project is None:
        raise HTTPException(
            status_code=404,
            detail='Проект не найден!'
        )
    return project


async def check_project_update(
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession,
) -> CharityProject:
    project = await check_project_exists(project_id, session)

    if project.fully_invested:
        raise HTTPException(
            status_code=400,
            detail='Закрытый проект нельзя редактировать!'
        )
    if obj_in.full_amount and project.invested_amount > obj_in.full_amount:
        raise HTTPException(
            status_code=400,
            detail='Запрещено устанавливать требуемую сумму меньше внесённой!'
        )
    return project


async def check_project_delete(
    project_id: int,
    session: AsyncSession,
) -> CharityProject:
    project = await check_project_exists(project_id, session)

    if project.invested_amount:
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!'
        )
    return project
