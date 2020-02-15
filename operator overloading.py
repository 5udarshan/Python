class Human:

   def Say_hello(self, name=None):

      if name is not None:
         print("Hello", name)
      else:
         print("Hello")

#Create instance
obj = Human()

#Call the Method
obj.Say_hello

#Call the method with a Parameter
obj.Say_hello("Everyone")
