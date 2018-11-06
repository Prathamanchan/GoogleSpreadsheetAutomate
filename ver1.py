
#Authorisation
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(credentials)

#Function
def rangeCalculator(lst,str1):
	lenlst=len(lst)
	Fcolindex=int(filter(str.isdigit, str1))
	Fcolname=filter(str.isalpha, str1)
	Lcolindex=Fcolindex+lenlst
	ConString=Fcolname+str(Lcolindex)    #('A1:A7')
	Fstring=str1+":"+ConString
	print Fstring
	return Fstring
		
#DutyCycle
sample=input("Enter Sample Time")
TPeriod=input("Enter Time Period")
DutyCycle=input("Enter DutyCycle")
Cycle=input("Number of Cycles")
str1=raw_input("Enter Starting Cell Name")
voltage=[]

On=1
Off=0
Start=0
DC=0

while On==1:
	DC=Start/TPeriod
	print DC
	Start=Start+sample
	voltage.append(5)
	if DC >= DutyCycle:
		print("Hai")
		On=0
		Off=1
		break

while Off==1:
	DC=Start/TPeriod
	print DC
	Start=Start+sample
	voltage.append(0)
	if DC >= 1.0:
		print("Hello")
		On=0
		Off=0
		DC=0
		break

print voltage
rowcol=rangeCalculator(voltage,str1)


#WriteToSheet
worksheet = gc.open("WeWillAutomate").sheet1

cell_list = worksheet.range(rowcol)
cell_values = voltage

for i, val in enumerate(cell_values):  #gives us a tuple of an index and value
    cell_list[i].value = val    #use the index on cell_list and the val from cell_values

# Update in batch
worksheet.update_cells(cell_list)



	


