# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /devices_properties

# Set the working directory to /value_recovery_asset
WORKDIR /devices_properties

# Copy the current directory contents into the container at /devices_properties
ADD . /devices_properties/
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


RUN chmod +x entrypoint.sh
ENTRYPOINT ["/bin/bash", "-c", ". ./entrypoint.sh"]
