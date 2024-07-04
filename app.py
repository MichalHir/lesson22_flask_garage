# actuall code of ran: https://github.com/ranerlich7/flask_garage/tree/main
from flask import Flask, render_template, request

app = Flask(__name__)

# car1 = {"number": "123-456", "problems": [],"image": "https://picsum.photos/id/133/20/30"}
# car2 = {"number": "456-789", "problems": [],"image": "https://picsum.photos/id/133/20/30"}
car1 = {
    "id": "1",
    "number": "123-456",
    "problems": [],
    "image": "https://images.pexels.com/photos/1592384/pexels-photo-1592384.jpeg?auto=compress&cs=tinysrgb&w=600",
}
car2 = {
    "id": "2",
    "number": "456-789",
    "problems": [],
    "image": "https://images.pexels.com/photos/112460/pexels-photo-112460.jpeg?auto=compress&cs=tinysrgb&w=600",
}
cars = [car1, car2]


@app.route("/")
def cars_list():
    return render_template("car_list.html", car_list=cars)

    # final_str = ""
    # for car in cars:
    #     final_str += f"<p>{car['number']}</p>"

    # return final_str


# @app.route("/single_car/<int:index>")
# def single_car(index):
#     return (
#         f"<p>Number:{cars[index]['number']} <br> Problems:{cars[index]['problems']}</p>"
#     )
@app.route("/single_car/<id>")
def single_car(id):
    for car in cars:
        if car["id"] == id:
            return render_template("single_car.html", car=car)
    return render_template("single_car.html", car=None)


# @app.route("/add_car/")
# def add_car():
#     print("****** Adding car")
#     return "Adding car"


@app.route("/add_car/")
def add_car():
    print("****** Adding car")
    return render_template("add_car.html")


@app.route("/add_to_list/", methods=["POST", "GET"])
def add_to_list():
    print("****** Adding to list", request.form["cNumber"])
    return "Added to list:" + request.form["cNumber"]


if __name__ == "__main__":
    app.run(debug=True, port=9000)
