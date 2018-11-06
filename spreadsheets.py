import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
#scope=['https://spreadsheets.google.com/feeds']
creds=ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client=gspread.authorize(creds)

sheet=client.open('WeWillAutomate').sheet1

legislators=sheet.get_all_records()
print(legislators)
