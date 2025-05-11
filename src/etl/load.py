from pandas import DataFrame
from google.oauth2 import service_account
from googleapiclient.discovery import build

from settings import SCOPES, SERVICE_ACCOUNT_FILE, SPREADSHEET_ID, SHEET_NAME


def load_data_to_gspread(data: DataFrame, sheet_name: str = SHEET_NAME) -> None:
    """
    Load data to Google Sheets using gspread.
    
    Args:
        data (DataFrame): Data to be loaded into Google Sheets.
    """
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, 
            scopes=SCOPES
        )

    service = build('sheets', 'v4', credentials=creds)

    values = [data.columns.tolist()] + data.values.tolist()

    body = {
        'values': values
    }
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=f'{sheet_name}!A1',
        valueInputOption='RAW',
        body=body
    ).execute()

    spreadsheet = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
    sheet_id = None
    for sheet in spreadsheet['sheets']:
        if sheet['properties']['title'] == sheet_name:
            sheet_id = sheet['properties']['sheetId']
            break

    if sheet_id is None:
        raise Exception(f"Sheet '{sheet_name}' not found.")
    
    requests = [
        # Freeze the first row
        {
            'updateSheetProperties': {
                'properties': {
                    'sheetId': sheet_id,
                    'gridProperties': {
                        'frozenRowCount': 1
                    }
                },
                'fields': 'gridProperties.frozenRowCount'
            }
        },
        # Apply bold formatting to the header row
        {
            'repeatCell': {
                'range': {
                    'sheetId': sheet_id,
                    'startRowIndex': 0,
                    'endRowIndex': 1
                },
                'cell': {
                    'userEnteredFormat': {
                        'textFormat': {
                            'bold': True
                        }
                    }
                },
                'fields': 'userEnteredFormat.textFormat.bold'
            }
        },
        # Apply a basic filter to the header row
        {
            'setBasicFilter': {
                'filter': {
                    'range': {
                        'sheetId': sheet_id,
                        'startRowIndex': 0,
                        'endRowIndex': len(values),
                        'startColumnIndex': 0,
                        'endColumnIndex': len(values[0])
                    }
                }
            }
        },
        # Apply autoresize to all columns
        {
            "autoResizeDimensions": {
                "dimensions": {
                    "sheetId": sheet_id,
                    "dimension": "COLUMNS",
                    "startIndex": 0,
                    "endIndex": len(data.columns)
                }
            }
        }
    ]

    body = {
        'requests': requests
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body=body
    ).execute()

    print("✅ Data uploaded and formatted as a table successfully.")
