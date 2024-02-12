from turtle import Turtle, Screen


# timmy is the object
# Many Objects can be created fro the class (blueprint)
 # Turtle is the blueprint(Class)
timmy = Turtle()   # Turtle Object
print(timmy)
timmy.shape('turtle')
timmy.color('red')   # Color is a function that belong to the  object
timmy.forward(250)
timmy.rt(30)
timmy.fd(100)
timmy.lt(90)
timmy.fd(100)




# attrbutes of the object. What the object has
# attributes defines what the object has
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# method of the object. What the object does
# method defines what the object does