import gspread

gc = gspread.authorize('client_secret.json')

# Open a worksheet from spreadsheet with one shot
wks = gc.open("WeWillAutomate").sheet1

wks.update_acell('B2', "it's down there somewhere, let me take another look.")

# Fetch a cell range
cell_list = wks.range('A1:B7')
