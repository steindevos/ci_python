class Auto: 
    def __init__(self, auto_type, engine_type, capacity, composition, is_soft_top=False, is_articulated=False):
        
        self.auto_type = auto_type.lower()
        self.engine_type = engine_type.lower()
        self.capacity = capacity
        self.composition = composition.lower()
        self.is_soft_top = is_soft_top
        self.is_articulated = is_articulated
        self.operation_type = "manual"
        
        self.my_engine = Engine(engine_type, capacity)
        
        self.my_body = Body(composition, is_soft_top, is_articulated)
        
        self.my_wheels = []
        self.my_doors = []
        
        if self.auto_type == "car":
            for wheel in range(4):
                self.my_wheels.append(Wheel(17, "Radial"))
            if self.composition == "carbon fibre":
                self.operation_type == "automatic"
            for door in range(4):
                self.my_doors.append(Door(self.operation_type))
                
        elif self.auto_type == "bike":
            for wheel in range(2):
                self.my_wheels.append(Wheel(18, "slick"))
        
        elif self.auto_type == "truck":
            if self.is_articulated:
                for wheel in range(18):
                    self.my_wheels.append(Wheel(24, "Assymetric"))
            else:
                for wheel in range(10):
                    self.my_wheels.append(Wheel(24, "Assymetric"))
            
            for door in range(2):
                self.my_doors.append(Door(self.operation_type))
        
    def drive(self):
        if len(self.my_doors) > 0:
            print(self.my_doors[0].open())
            print(self.my_doors[0].close())

        print(self.my_engine.start())

        for wheel in self.my_wheels:
            print(wheel.rotate())

        if self.is_soft_top:
            print(self.my_body.open_roof())

        print("Driving!")

        print("----------------------------")

    def stop(self):
        for wheel in self.my_wheels:
            print(wheel.stop())

        print("Stopping!!")
        print(self.my_engine.stop())

        if self.is_soft_top:
            print(self.my_body.close_roof())

        if len(self.my_doors) > 0:
            print(self.my_doors[0].open())
            print(self.my_doors[0].close())

        print("----------------------------")

    def description(self):
        print("Description:")
        print(self.auto_type)
        print(self.engine_type)
        print(self.capacity)
        print(self.composition)
        print(self.is_soft_top)
        print(self.is_articulated)
        print(self.operation_type)
        print("----------------------------")
        
        
class Engine: 
    def __init__(self, engine_type, capacity=0): 
        self.engine_type = engine_type.lower()
        self.capacity = capacity
        
    def start(self):
        return "Engine started"
    
    def stop(self): 
        return "Engine stopped"

class Wheel: 
    def __init__(self, size, tyre_type): 
        self.size = 0
        self.tyre_type = tyre_type.lower()
        
    def rotate(self):
        return "turnning"
    
    def stop(self):
        return "braking"

class Door: 
    def __init__(self, operation_type):
        self.operation_type = operation_type.lower()
    
    def open(self):
        if self.operation_type == "automatic":
            return "fancy door open"
        else:
            return "door open"
    
    def close(self):
        if self.operation_type == "automatic":
            return "fancy door closed"
        else: 
            return "door closed"

class Body: 
    def __init__(self, composition, is_soft_top = False, is_articulated = False): 
        self.composition = composition.lower()
        self.is_soft_top = is_soft_top
        is_articulated = is_articulated
        
    def open_roof(self):  
        if self.is_soft_top == True: 
            return "opening roof"
        
    def close_roof(self): 
        if self.is_soft_top == True: 
            return "Closing roof"