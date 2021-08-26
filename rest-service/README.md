# REST Service
This service exposes the coffee shop to the client and it's only component of interaction is the MQ. 

## Docker
The container should be exposed on port 8080 with the following command:

`docker run --name coffee-rest-p 8080:80 coffee-rest:test1.0.0`