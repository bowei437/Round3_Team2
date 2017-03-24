# ECE 4575 Team 2: Assignment 6 Phase 2

Pathfinding API using RESTful service with Swagger for ECE 4575 Spring 2017.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python3 
* VirtualBox (VM for Docker)
* SSH access to AWS server

## Deployment

Add additional notes about how to deploy this on a live system

## Running the tests

Explain how to run the automated tests for this system

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

