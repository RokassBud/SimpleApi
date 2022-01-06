from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
import json

def json_format(raw):
    text = json.dumps(raw, sort_keys= True, indent = 4)
    return text

def show_sheet():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range='Lapas1!A1:E10').execute()
    values = result.get('values', [])
    skaicius = len(values)
    for i in range(skaicius):
        tarp = values[i]
        listas.append(tarp)
        print(json_format(listas))

def check_sheet(row):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=(f'Lapas1!{row}2:{row}11')).execute()
    values = result.get('values', [])
    number = 10
    for i in range(number):
        if not values[i]:
            break
    return i

def insert(row, row2, empty, cost, udata):
    sheet = service.spreadsheets()
    empty = empty + 1
    result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=(f'Lapas1!{row}{empty}'),valueInputOption='USER_ENTERED',
                                insertDataOption='OVERWRITE', body={'values':[udata]}).execute()
    result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                   range=(f'Lapas1!{row2}{empty}'), valueInputOption='USER_ENTERED',
                                   insertDataOption='OVERWRITE', body={'values': [cost]}).execute()

SERVICE_ACCOUNT_FILE = 'testsheets.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = '1B8Uq14UWNG15-rhGtnaUTkaelHqlJOf6aoKGTvFcSoY'
service = build('sheets', 'v4', credentials=creds)

listas = []




