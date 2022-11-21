## Pre-requisites

To run the client you will need python3 (preferably between versions 3.6 and 3.9).

To download python refer to the installation guide https://www.python.org/downloads/

## Run

To run the project do the following steps:

* create a virtual environment
<code>python3 -m venv venv </code>

* activate the virtual environment (assuming linux. If using other operating system refer to the documentation https://docs.python.org/3/library/venv.html)
<code> source venv/bin/activate </code>

* Install required packages
<code> pip3 install -r requirements.txt </code>

* Run the program
* python3 run.py


The application will be available on port 4333. This is however configurable by exporting the environemntal variable <code>FLASK_RUN_PORT<code>

If client and other services are on different servers, you can configure the urls in the config.py file.

## Time validation

Service Benchmarking. The benchmarking program is available in timer.py, with the number of trials, and urls also configurable.