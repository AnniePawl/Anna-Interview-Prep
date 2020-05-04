# Classes in Python 

# Initialize class w/ super/parent class to inherit all parameters and methods from that parent class

# class Animal():
# class Mammal(Animal) --> inherits from Animal 
# class Fox(Mammal) --> inherits from animal and mammal

class ClassName(__superclass_optional):
  # initialize class w/ these parameters 
  def __init__(self, parameters, optional_parameter = None):
    super().__init__(parameters_for_superclass)
    # properties that your class has should be initialzied here 
    self.property = parameters 

  # Methods for your class are implemented here 
  def custom_method(self, parameters)

  # Override 
  def override_method_name_from_superclass(class,parameter):
    pass

  # Example 
  # class customArray(array):
    # init method 
    # self.size 
  # def __len__():
    # return self.size * 2