class Bird(object): 
    kind = ""
    call = ""
    
    def __init__(self, the_kind, the_call):   #"self" in python is "this" in JavaScript
        self.kind = the_kind
        self.call = the_call
        
    def get_description(self): 
        return "The {0} goes {1}".format(self.kind, self.call)
        
        
class Seabird(Bird):
    diving_depth = 0
    
    def __init__(self, the_kind, the_call, the_diving_depth):
        super(Seabird, self).__init__(the_kind, the_call)
        
        self.diving_depth = the_diving_depth
        
    def get_description(self):
        return super(Seabird, self).get_description() + "and dives to a depth of {0} metres".format(self.diving_depth)
        
class Fowl(Bird): 
    fowl_type = ""
    fowl_types = {'landfowl':'Landfowl is an order of heavy-bodied ground-feeding birds',
                 'waterfowl':'Waterfowl is an order of birds that comprises three families: \nAnhimidae (the screamers)\n Anseranatidae (the magpie goose), \nAnatidae'}
    
    def __init__(self, the_kind, the_call, the_fowl_type):
        super(Fowl, self).__init__(the_kind, the_call)
        self.fowl_type = the_fowl_type
    
    def get_description(self):
        return super(Fowl, self).get_description() + " {0}".format(self.fowl_types[self.fowl_type.lower()])
        
        
        
class Owls(Bird): 
    type_of_hairball = ""
    
    def __init__(self, the_kind, the_call, the_type_of_hairball): 
        super(Owls, self).__init__(the_kind, the_call)
        self.type_of_hairball = the_type_of_hairball
        
    def get_description(self): 
        return super(Owls, self).get_description() + " and has the following type of hairball: {0}".format(self.type_of_hairball)