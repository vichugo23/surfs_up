from flask import Flask 

# We're now ready to create a new Flask app instance. "Instance" 
#is a general term in programming to refer to a singular version of something. 
#Add the following to your code to create a new Flask instance called app:

app = Flask("__name__")


#Our Flask app has been created—let's create our first route!

#First, we need to define the starting point, also known as the root. To do this, 
# we'll use the function @app.route('/'). Add this to your code now.

@app.route('/')
def hello_world():
    return 'Hello world'

#Notice the forward slash inside of the app.route? This denotes that we want 
# to put our data at the root of our routes. The forward slash is commonly known a
# s the highest level of hierarchy in any computer system.

#Next, create a function called hello_world(). Whenever you make a route in Flask,
#  you put the code you want in that specific route below @app.route(). Here's
#  what it will look like: ^^ LOOK BELOW THE "@APP.ROUTE" LINE OF CODE