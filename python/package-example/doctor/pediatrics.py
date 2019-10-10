#pediatrics.py

FEES = 800
REGISTER = 100

def diagnose(symptoms):
	if symptoms == "sneezing":
		prescription = "take t-minic"
	else:
		prescription= "give paracetmol and take rest"
	return prescription

def fees(first_visit=False):
	if first_visit == True:
		total_fees = FEES + REGISTER
	else:
		total_fees = FEES
	return total_fees
