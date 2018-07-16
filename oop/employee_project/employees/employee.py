
class Employee(object): 
    first_name = ""
    second_name = ""
    n_years = 0
  
    
    def __init__(self, the_first_name, the_second_name, the_n_years):
        self.first_name = the_first_name
        self.second_name = the_second_name
        self.n_years = the_n_years
       
    
    def calculate_salary(self):
        salary = 50000
        
        if self.n_years < 3: 
            salary *= 1.01
        elif self.n_years <= 5:
            salary *= 1.1
        elif self.n_years > 5: 
            salary *= 1.25
        else: 
            return "what happened?"
        
        salary = int(salary)
        return salary
        
    def get_details(self):
        return "Full name: {0} {1}\nYears in service: {2}\nCurrent salary: {3} EUR.".format(self.first_name, self.second_name, self.n_years, self.calculate_salary())
        
        
class Coder(Employee): 
    
    language = ""
    
    def __init__(self, the_first_name, the_second_name, the_n_years, the_language):
        
        super(Coder, self).__init__(the_first_name, the_second_name, the_n_years)
        self.language = the_language
    
    def calculate_salary(self):
        salary = super(Coder, self).calculate_salary()
        if self.language.lower() == "none": 
            salary += 0
        elif self.language.lower() == "python":
            salary += 1005
        elif self.language.lower() == "java":
            salary += 704
        elif self.language.lower() == "c++" or self.language.lower() == "c": 
            salary += 503
        elif self.language.lower() == "ruby":
            salary -= 45000
        return salary
        
    def get_details(self): 
        return super(Coder, self).get_details() + " \nCodes in: {0}".format(self.language)
              
class SalesPerson(Employee): 
    
    territory = ""
    
    def __init__(self, the_first_name, the_second_name, the_n_years, the_territory): 
        super(SalesPerson, self).__init__(the_first_name, the_second_name, the_n_years)
        self.territory = the_territory
        
    def calculate_salary(self): 
        salary = super(SalesPerson, self).calculate_salary()
        
        if self.territory.lower() == "europe":
            salary += 50
        elif self.territory.lower() == "africa":
            salary += 1000
        elif self.territory.lower() == "north america":
            salary += 400
        elif self.territory.lower() == "asia":
            salary += 1000
        
        return salary
    
    def get_details(self):
        return super(SalesPerson, self).get_details() + " \nTerritory: {0}".format(self.territory).title()
        
class Ceo(Employee):
    positive_growth = True
    
    def __init__(self, the_first_name, the_second_name, the_n_years, the_positive_growth): 
        super(Ceo, self).__init__(the_first_name, the_second_name, the_n_years)
        self.positive_growth = the_positive_growth
    
    def calculate_salary(self):
        salary = super(Ceo, self).calculate_salary()
        if self.positive_growth == True:
            salary *= 3
        if self.positive_growth == False:
            salary *= 2
        return salary
        
    
    # def get_details(self):
    #     return super(Ceo, self).get_details() + "This
        