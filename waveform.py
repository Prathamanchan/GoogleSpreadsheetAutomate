
sample=input("Enter Sample Time")
TPeriod=input("Enter Time Period")
DutyCycle=input("Enter DutyCycle")
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


