from datetime import datetime

FORMAT = "%Y/%m/%d %H:%M:%S"
NOW_DATE_TIME = datetime.now().strftime(FORMAT)
HEADER = [
    ['Отчёт от', NOW_DATE_TIME],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]
COLUMN_COUNT = len(HEADER[2])
SPREADSHEET_BODY = {
    'properties': {'title': f'Отчёт от {NOW_DATE_TIME}',
                   'locale': 'ru_RU'},
    'sheets': [
        {
            'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': 'Лист1',
                'gridProperties': {
                    'rowCount': '',
                    'columnCount': COLUMN_COUNT
                }
            }
        }
    ]
}
