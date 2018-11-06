import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(credentials)

#Authorisation

worksheet = gc.open("WeWillAutomate").sheet1

cell_list = worksheet.range('A1:A7')
cell_values = [1,2,3,4,5,6,7]

for i, val in enumerate(cell_values):  #gives us a tuple of an index and value
    cell_list[i].value = val    #use the index on cell_list and the val from cell_values

# Update in batch
worksheet.update_cells(cell_list)


