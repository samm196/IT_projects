employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
housing_allowance = float(input("Enter housing allowance: "))
transport_allowance = float(input("Enter transport allowance: "))
tax_percentage = float(input("Enter tax percentage: "))

gross_salary = basic_salary + housing_allowance + transport_allowance
tax = gross_salary * tax_percentage / 100
net_salary = gross_salary - tax

employee = {
    "name": employee_name,
    "basic_salary": basic_salary,
    "housing_allowance": housing_allowance,
    "transport_allowance": transport_allowance,
    "tax_percentage": tax_percentage,
    "gross_salary": gross_salary,
    "tax": tax,
    "net_salary": net_salary
}

print("\n----- Salary Report -----")
print("Employee Name:", employee["name"])
print("Basic Salary:", employee["basic_salary"])
print("Housing Allowance:", employee["housing_allowance"])
print("Transport Allowance:", employee["transport_allowance"])
print("Gross Salary:", employee["gross_salary"])
print("Tax (" + str(employee["tax_percentage"]) + "%):", employee["tax"])
print("Net Salary:", employee["net_salary"])
print("--------------------------")
