from employees.employee import Employee, Coder

new_employee = Employee("Henkie", "Penkie", 4)
new_employee2 = Employee("Rick", "Stamina", 40)
new_employee3 = Employee("Sandra", "Montblanc", 6)
new_employee4 = Employee("Riciardo", "Davy de Vries", 1)
new_coder = Coder("Kim", "Marneth", 2, "Python")


print(new_employee.get_details())
print(new_employee2.get_details())
print(new_employee3.get_details())
print(new_employee4.get_details())

print(new_coder.get_details())