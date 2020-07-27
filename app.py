from flask import Flask, render_template

from models import Flight, Passenger

app = Flask(__name__)  # Creates the flask object


@app.route('/')
def index(): # By convention, the home page of websites is often index.html hence the route here is named index
    # Create sample flight and passenger objects to provide some data to work with as we don't have a database
    f1 = Flight(flight_num="AZ1244", origin="New York", destination="Paris")
    p1 = Passenger(firstname="Paris", lastname="Holt")
    p2 = Passenger(firstname="Susan", lastname="York")
    f1.add_passenger(p1)
    f1.add_passenger(p2)
    f2 = Flight(flight_num="BB9876", origin="Paris", destination="Tokyo")
    f2.add_passenger(p2)
    # render the view using the index.html template, passing the flight details to the template
    return render_template('index.html', flights=[f1, f2])


if __name__ == '__main__':
    app.run()  # Runs the Flask app in a web server, the default URL is http://127.0.0.1:5000/
