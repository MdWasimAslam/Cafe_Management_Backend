from flask import Flask, request

app = Flask(__name__)  # create an instance of the Flask class


items = [
    {"name": "Green Apple Mojito", "price": 160},
    {"name": "Mango Mojito", "price": 150},
    {"name": "Virgin Mojito", "price": 120},
    {"name": "Momos", "price": 140},
] 


@app.get("/get-items")  # route() decorator to tell Flask what URL should trigger our function
def get_items():
    return {"items": items}  


# @app.get("/get-item/<string:name>")  # route() decorator to tell Flask what URL should trigger our function
# def get_item(name):
#     print(name)
#     for item in items:
#         if item["name"] == name:
#             return {"item": item}
#     return {"message": "Item not found"}, 404 

@app.get("/get-item")  # route() decorator to tell Flask what URL should trigger our function
def get_item():
    name = request.args.get('name')
    print(name)
    for item in items:
        if item["name"] == name:
            return {"item": item}
    return {"message": "Item not found"}, 404 



@app.post("/add-items")  # route() decorator to tell Flask what URL should trigger our function
def add_items():
    request_data = request.get_json()
    print(request_data)
    items.append(request_data)
    return {'message': 'Item added successfully'},201


@app.put("/update-item")  # route() decorator to tell Flask what URL should trigger our function
def update_item():
    request_data = request.get_json()
    for item in items:
        if item["name"] == request_data["name"]:
            item["price"] = int(request_data["price"])
            return {'message': 'Item updated successfully'},201
    return {'message': 'Item not found!'},401