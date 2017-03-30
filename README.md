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


## Running the tests

Internal Pathfinding Tests

To run internal pathfinding tests, run "Python testPathfinding.py" while in the "Pathfinding_and_InternalTesting" directory.
A description of each individual is included below. 
'Test 0' is a test of an incorrect JSON file. 'Test 1' is a test of a problem with no obstacles. 
'Test 2' is a test of a problem with obstacles. 

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## GUI
run the CLientSDK project within the clientSDk folder. a gui window should pop up. Following out swagger ui guidelines to fill out the body
of the message. Select one of the 4 request types from the drop down, fill in the id's if neccessary and then click the desire function button.
Only Get requests will cause data to be displayed in the graphics view.

## Sanitization

The inputs to our API are sanitized using Flask's model feature and Swagger. The API will catch invalid inputs like missing information or out-of-range value. In the server controller code, we catch exceptions when we requset to get json objects and send errors with detailed message. We also have checks in our controller code for the rest of the input sanitization. We use consistent error code and detailed error message to make our API very easy to use.

## Built With

* Swagger API
* Docker

## Authors

* Noah Davis
* Jonathan DeFreeuw
* Jordan Holland
* Jisu Park
* Dylan Zeigler
* Bowei Zhao

## Acknowledgments

* Linus Torvalds

