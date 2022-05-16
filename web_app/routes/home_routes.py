from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)



@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return "Welcome Home"


@home_routes.route("/about")
def about():
    print("ABOUT...")
    return "About Me"

@home_routes.route("/another")
def another():
    print("ANOTHER PAGE MAYBE...")
    return "Here is another page"




@home_routes.route("/hello")
def hello_world():
    print("Hello...", dict(request.args))
    
    
    
    name=request.args.get("name") or "World"
   
   
    message = f"Hello, {name}!"
    return message
