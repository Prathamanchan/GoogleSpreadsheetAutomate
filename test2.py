import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(credentials)

#Authorisation

worksheet = gc.open("WeWillAutomate").sheet1
check='A1:C7'
cell_list = worksheet.range(check)

for cell in cell_list:
    cell.value = 'Adi'

# Update in batch
worksheet.update_cells(cell_list)



def getIndex(str1):
	ret=int(filter(str.isdigit, str1))
	return ret
