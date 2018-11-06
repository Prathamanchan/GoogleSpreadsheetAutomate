import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(credentials)

#Authorisation

worksheet = gc.open("WeWillAutomate").sheet1
i=0

for x in range(6):
	worksheet.update_cell(i, 2, 'Bingo!')
	i=i+1


