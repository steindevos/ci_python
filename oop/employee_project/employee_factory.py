from employees.employee import Employee, Coder, SalesPerson, Ceo

new_employee = Employee("Henkie", "Penkie", 4)
new_employee2 = Employee("Rick", "Stamina", 40)
new_employee3 = Employee("Sandra", "Montblanc", 6)
new_employee4 = Employee("Riciardo", "Davy de Vries", 1)
new_coder = Coder("Kim", "Marneth", 2, "Python")
new_coder2 = Coder("Klara", "Rambo", 10, "Ruby")
new_coder3 = Coder("Stein", "de Vos", 1, "Python")
new_sales_person = SalesPerson("chanine", "van Eijsden", 2, "asia")
new_sales_person1 = SalesPerson("Frank", "Hooghartig", 3, "europe")
new_ceo = Ceo("Rita", "Muita", 10, True)

employees = []
employees.append(new_employee)
employees.append(new_employee2)
employees.append(new_employee3)
employees.append(new_employee4)
employees.append(new_coder)
employees.append(new_coder2)
employees.append(new_coder3)
employees.append(new_sales_person)
employees.append(new_sales_person1)
employees.append(new_ceo)

def calculate_total_salary(): 
    total_salary = 0 
    for emp in employees:
        total_salary += emp.calculate_salary()
    return "total labour cost: {0} EUR".format(total_salary)

print(calculate_total_salary())

salary_dict = {}
for emp in employees:
    salary_dict[emp.first_name +" "+ emp.second_name] = emp.calculate_salary()
print(salary_dict)

