import ortha
import pediatrics
from datetime import date

inputs,problem,name,first_visit_flag = input("doctor type, problem description, name,first Visit: ").split(",")


if inputs == "ortha":
	print("Visiting Ortho Specialist")
	prescriptions = ortha.diagnose(problem)
	fee_to_pay = ortha.fees(bool(first_visit_flag))

elif inputs == "pediatrics":
	print("Visiting Child specialists")
	prescriptions = pediatrics.diagnose(problem)
	fee_to_pay = pediatrics.fees(bool(first_visit_flag))

print("------------------------------------------")
print("PATIENT NAME : ",name)
print("BILL DATE : ",date.today())
print("------------------------------------------")
print(prescriptions)
print(fee_to_pay)




