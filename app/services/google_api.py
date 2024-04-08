from typing import Optional

from aiogoogle import Aiogoogle

from app.core.config import settings
from app.services.constants import COLUMN_COUNT, HEADER, SPREADSHEET_BODY


async def spreadsheets_create(
        wrapper_services: Aiogoogle,
        row_count: int,
        spreadsheet_body: Optional[dict] = SPREADSHEET_BODY
) -> str:
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body[
        'sheets'][0]['properties']['gridProperties']['rowCount'] = row_count + 3
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheet_id = response['spreadsheetId']
    return spreadsheet_id


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email}
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheet_id: str,
        projects: list,
        wrapper_services: Aiogoogle,
        row_count: int
) -> None:
    service = await wrapper_services.discover('sheets', 'v4')
    table_values = [
        *HEADER,
        *[list(map(str, [
            project['name'],
            project['time'],
            project['description']])) for project in projects],
    ]

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    response = await wrapper_services.as_service_account(  # noqa
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=f'R1C1:R{row_count+len(HEADER)}C{COLUMN_COUNT}',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
