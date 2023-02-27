
class car:
    def __init__(self,model,make,year_of_man,engine_capacity):
        self.model = model
        self.make = make
        self.year_of_man = year_of_man
        self.engine_capacity = engine_capacity

#getters
    def get_model(self):
        return self.model
    
    def get_make(self):
        return self.make

    def get_year(self):
        return self.year_of_man
    
    def get_engine_capacity(self):
        return self.engine_capacity
    
#setters :set the attributes
    def set_model(self,model):
        self,model = model

    def set_make(self,make):
        self,make = make

    def set_year(self,year):
        self,year = year

    def set_engine_capacity(self,engine_capacity):
        self,engine_capacity = engine_capacity

#objects : instance of class    
car1 = car("demio","nissan",2018,1300)
car2 = car("hilux","toyota",2020,3500)
car3 = car("premio","toyota",2018,2900)

car3.set_year(2023)
car1.set_year(2026)
car1.set_model()


print(car1.get_model())
print(car1.get_())

print(car2.get_model())
print(car3.get_year())

   