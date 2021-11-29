from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
import json

def json_format(raw):
    text = json.dumps(raw, sort_keys= True, indent = 4)
    return text

SERVICE_ACCOUNT_FILE = 'testsheets.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = '1B8Uq14UWNG15-rhGtnaUTkaelHqlJOf6aoKGTvFcSoY'
service = build('sheets', 'v4', credentials=creds)

listas = []
matches = []

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range='jobs!A1:B25').execute()
values = result.get('values', [])
skaicius = len(values)
for i in range(skaicius):
    tarp = values[i]
    listas.append(tarp)

funkcija = input('1. Išvesti viską, 2. Filtruoti')
if(funkcija == '1'):
    print(json_format(listas))

if(funkcija == '2'):
    zodis = input('Pagal kokį žodį filtruoti?')
    for search in listas:
        if zodis in str(search):
            matches.append(search)
print(json_format(matches))



