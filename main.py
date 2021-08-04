from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Enter bill amount: "))
period = input("Enter bill period, e.g. December 2020: ")

name1 = input("Enter first flatmate's name: ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house? "))
name2 = input("Enter the second flatmate's name: ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house? "))

bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)
print(flatmate1.pays(bill=bill, flatmate2=flatmate2))
print(flatmate2.pays(bill=bill, flatmate2=flatmate1))
report = PdfReport(f'{bill.period}.pdf')
report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=bill)
