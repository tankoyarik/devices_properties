## Project description:
 With the following project you can add devices and properties.
 You will find the following urls for the project:
   `devices/` - GET method will show up a list of all devices, POST - will create a new device
   
   `devices/<device_id>` - GET - retrieve a single device , PUT - update device , DELETE - removes a device (OPTIONS included as well)
   
   `properties/` - GET method will show up a list of all properties, POST - will create a new property
   
   `properties/<property_id>` - GET - retrieve a single property, PUT - update property, DELETE - removes a property (OPTIONS included as well)
   

## To run project:

1) `docker-compose build`
2) `docker-compose up`
