from pathlib import Path


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = Path('src\credentials.json')
SPREADSHEET_ID = '13QqX10qsfU2UH-z40rM4Qe2A6YLoTPxh5INQJusf7-A'
SHEET_NAME = 'Data'

BASE_URL = "https://www.alfabeta.net/precio/"

DRUGS_NAMES = [
    "saxenda",
    "vintix",
    "trapax",
    "novo-insomnium"
]

COLUMNS_NAMES = [
    "product",
    "manufacturer",
    "drug",
    "therapeutic_use",
    "form_and_dosage",
    "price"
]
