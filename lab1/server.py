# Import the Flask class from the flask module
from flask import Flask, request, make_response

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"

# Define no_content method
@app.route("/no_content")
def no_content():
    return ({"message": "No content found"}, 204)

@app.route("/exp")
def index_explicit():
    res = make_response({"message": "Hello World!"})
    res.status_code = 200
    return res