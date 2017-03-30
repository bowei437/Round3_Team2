# ECE 4574 Team 2: Assignment 6 Phase 2

Pathfinding API using RESTful service with Swagger for ECE 4574 Spring 2017.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python3
* pip3
* Port 8082 open on your machine

## Deployment

Clone the repository:
```
git clone https://github.com/bowei437/Round3_Team2.git
```

Change your current working directory to Round3_Team2/python-flask-server and install dependencies. Depending on your environment, installing dependencies may require root privileges. In that case, preface ```pip3``` with ```sudo```.
```
cd Round3_Team2/python-flask-server
pip3 install -r requirements.txt
```

Start the Flask server by running this command while in the ```Round3_Team2/python-flask-server``` directory.
```
python3 -m swagger_server
```

This should be the output from the command:
```
$ python3 -m swagger_server 
 * Running on http://0.0.0.0:8082/ (Press CTRL+C to quit)
```

Open a web browser and go to http://127.0.0.1:8082/v3/ui or subsitute ```127.0.0.1``` for your local IP address.

This should open the Swagger UI which will allow you to test the API by sending HTTP requests. The default structure of the JSON for each of the requests is shown next to each command. 

View the ```sample_problem.json``` file for a Problem that you can use to test the system by hand. Simply POST for a new Problem, remember the ```problem_id``` given, and POST or PUT to update the values for each of the values. Remember to check the default structure shown in Swagger to avoid getting errors.

Happy pathfinding!

## Running the tests

### Internal Pathfinding Tests

To run internal pathfinding tests, run "python3 testPathfinding.py" while in the "Pathfinding_and_InternalTesting" directory.
A description of each individual is included below. 
'Test 0' is a test of an incorrect JSON file. 'Test 1' is a test of a problem with no obstacles. 
'Test 2' is a test of a problem with obstacles. 


### GUI
run the CLientSDK project within the clientSDk folder. a gui window should pop up. Following out swagger ui guidelines to fill out the body
of the message. Select one of the 4 request types from the drop down, fill in the id's if neccessary and then click the desire function button.
Only Get requests will cause data to be displayed in the graphics view.


## Performance Testing 

You can find more materials (report and sample code) on the performance testing in the "PerformanceTesting" directory.

## Data Validation

The inputs to our API are sanitized using Flask's model feature and Swagger. The API will catch invalid inputs like missing information or out-of-range value. In the server controller code, we catch exceptions when we requset to get json objects and send errors with detailed message. We also have checks in our controller code for the rest of the input sanitization. We use consistent error code and detailed error message to make our API very easy to use.

## Path Efficiency

Our pathfinding algorithm is built to look at the previous path to determine if the new one will be any different. By checking if any new obstacle has been added to block the path, we aim to reduce the time spent pathfinding along the same coordinates. 

## Running with Docker

This service was also built into a Docker image. For more information on building and running the container, see https://github.com/jth2279/Pathfinding_Dockerized.

## Built With

* Swagger API
* Python-Flask

## Authors

* Noah Davis
* Jonathan DeFreeuw
* Jordan Holland
* Jisu Park
* Dylan Zeigler
* Bowei Zhao

## Acknowledgments

* Linus Torvalds

