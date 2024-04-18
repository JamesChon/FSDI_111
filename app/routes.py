from flask import Flask       # from the flask module import the Flask class

app = Flask(__name__)         # Create an instance of the Flask class

@app.get("/about")
@app.get("/")                 # Flask decorator that maps view functions to routes  
def index():                  # view function
    me = {                    # python dictionary  
        "first_name": "James",
        "last_name": "Chon",
        "hobbies": "Gaming",
        "is_online": True
    }
    return me                 # When you return a dict from a view function, it becomes a JSON  

# @app.post()
# @app.put()
# @app.patch()
# @app.delete()