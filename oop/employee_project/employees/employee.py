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
        
        # if self.language.lower() == "none": 
        #     salary += 0
        # if self.language.lower() == "python":
        #     salary += 1005
        # if self.language.lower() == "java":
        #     salary += 704
        # if self.language.lower() == "c++" or self.language.lower() == "c": 
        #     salary += 503
        # if self.language.lower() == "ruby":
        #     salary -= 45000
        
        salary = int(salary)
        return salary
        
    def get_details(self):
        return "{0} {1} works here for {2} years and earns {3} EUR.".format(self.first_name, self.second_name, self.n_years, self.calculate_salary())
        
        
class Coder(Employee): 
    
    language = ""
    
    def __init__(self, the_first_name, the_second_name, the_n_years, the_language):
        
        super(Coder, self).__init__(the_first_name, the_second_name, the_n_years)
        self.language = the_language
    
            
        