# This python script would work as a separate Module
# Defining a Function for hello world
def hello():
   N = 0
   while True:
#   while N < 5:
      print ("Hello World for "+str(N)+" times")
      N += 1
      if N == 8:
         break

# Defining a variable
var="This is Variable"

# Define a class
class varun:
    def __init__(self, name, color):
        self.color = color
        self.name = name

    def tell_me_about_the_varun(self):
        print("This varun is " + self.color + ".")
        print(self.name + " is the name of varun.")

