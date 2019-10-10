#calculator.py

FEES = 500
REGISTER = 100


def diagnose(symptoms):
	if symptoms == "joint pain":
		prescription = "take Vitamin D"
	else:
		prescription = "do excerise in morning"
	return prescription


def fees(first_visit=False):
	if first_visit == True:
		total_fees = FEES + REGISTER
	else:
		total_fees = FEES
	return total_fees
