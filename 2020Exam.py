TotalCommission = 0

EmployeeNumber = input("How many employees are there in the company? ")

for n in range(0,int(EmployeeNumber)):

    EmployeeName = input("Enter the name of the Employee ")
    EmployeeID = input("Enter the ID of the Employee ")
    PropertiesSold = input("Enter the amount of properties sold ")

    SalesCommission = int(PropertiesSold) * 500

    TotalCommission =+ int(SalesCommission)

print(TotalCommission)