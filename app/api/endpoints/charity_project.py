from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_name_duplicate, check_project_delete,
                                check_project_update)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.schemas import (CharityProjectCreate, CharityProjectDB,
                         CharityProjectUpdate)
from app.services.investing import run_investing_process

router = APIRouter()


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    # response_model_exclude_none=True,
)
async def get_all_charity_projects(
    session: AsyncSession = Depends(get_async_session),
):
    all_projects = await charity_project_crud.get_multi(session)
    return all_projects


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_new_charity_project(
    charity_project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
):
    await check_name_duplicate(charity_project.name, session)
    new_project = await charity_project_crud.create(charity_project, session)
    return await run_investing_process(new_project, session)


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def delete_charity_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    project = await check_project_delete(
        project_id, session
    )
    project = await charity_project_crud.remove(
        project, session
    )
    return project


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def update_charity_project(
        project_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    project = await check_project_update(project_id, obj_in, session)
    if obj_in.name != project.name:
        await check_name_duplicate(obj_in.name, session)
    project = await charity_project_crud.update(
        project, obj_in, session
    )
    return project
