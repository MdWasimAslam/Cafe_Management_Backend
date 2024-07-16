from flask import Flask

app = Flask(__name__)  # create an instance of the Flask class


items = [
    {"name": "Green Apple Mojito", "price": 160},
    {"name": "Mango Mojito", "price": 150},
    {"name": "Virgin Mojito", "price": 120},
] 


@app.route("/get-items")  # route() decorator to tell Flask what URL should trigger our function
def get_items():
    return {"items": items}  
