# actuall code of ran: https://github.com/ranerlich7/flask_garage/tree/main
from flask import Flask, render_template, request

app = Flask(__name__)
cost = [
    ("Engine", 2000),
    ("Breaks", 1000),
    ("5000_km_treatment", 500),
    ("10,000 km treatment", 1000),
    ("Filters+ Oil", 250),
    ("Gear", 1000),
]

car1 = {
    "id": "1",
    "number": "123-456",
    "problems": [],
    "image": "https://images.pexels.com/photos/1592384/pexels-photo-1592384.jpeg?auto=compress&cs=tinysrgb&w=600",
    "if_urgent": False,
}
car2 = {
    "id": "2",
    "number": "456-789",
    "problems": [],
    "image": "https://images.pexels.com/photos/112460/pexels-photo-112460.jpeg?auto=compress&cs=tinysrgb&w=600",
    "if_urgent": False,
}
cars = [car1, car2]


@app.route("/")
def cars_list():
    return render_template("car_list.html", car_list=cars)


@app.route("/urgent/")
def urgent_cars_list():
    return render_template("urgent_car_list.html", car_list=cars)


@app.route("/prices/")
def prices():
    return render_template("prices.html", prices=cost)


@app.route("/single_car/<id>")
def single_car(id):
    for car in cars:
        if car["id"] == id:
            return render_template("single_car.html", car=car)
    return render_template("single_car.html", car=None)


@app.route("/add_car/")
def add_car():
    print("****** Adding car")
    return render_template("add_car.html")


@app.route("/add_to_list/", methods=["POST", "GET"])
def add_to_list():
    print("****** Adding to list", request.form["cNumber"])
    new_car = {
        "id": int(len(cars) + 1),
        "number": request.form["cNumber"],
        "problems": [],
        "image": "https://images.pexels.com/photos/1592384/pexels-photo-1592384.jpeg?auto=compress&cs=tinysrgb&w=600",
        "if_urgent": False,
    }
    cars.append(new_car)
    return (
        "Added to list:"
        + request.form["cNumber"]
        + "to return to homepage:'http://127.0.0.1:9000/'"
    )


@app.route("/add_urgent/")
def add_to_urgent():
    print("Adding to urgent")
    return render_template("add_urgent.html")


@app.route("/add_to_urgent_list", methods=["POST", "GET"])
def add_to_urgent_list():
    print("Adding to urgent list", request.form["cUrgent"])
    new_car = {
        "id": int(len(cars) + 1),
        "number": request.form["cUrgent"],
        "problems": [],
        "image": "https://images.pexels.com/photos/1592384/pexels-photo-1592384.jpeg?auto=compress&cs=tinysrgb&w=600",
        "if_urgent": True,
    }
    cars.append(new_car)
    return (
        "Added to urgent list:"
        + request.form["cUrgent"]
        + "to return to homepage:'http://127.0.0.1:9000/'"
    )


if __name__ == "__main__":
    app.run(debug=True, port=9000)
