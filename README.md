
# Employee Application

Employee Application is a Python web application for dealing with CRUD operations on employees.

Install Flask in a virtual environment to avoid problems with conflicting libraries. Check Python version before starting:

Python 3 comes with a virtual environment module called venv preinstalled.


Create a virtual environment and store its tools in the “env” folder:

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Employee App.

```bash
$python3 -m venv env
```

##Running vertual env
```bash
$  source env/bin/activate
(env)$ 
```

## Installing Flask and Dependencies

```python
(env)$ pip install flask

# install Flask-SQLAlchemy
(env)$ pip install Flask-SQLAlchemy

# copy git files and folder from [flask app](https://github.com/Shidram/Interactions.git) inside virtual environment
app/

# run flask app
(env)$ python app.py
```

```bash

#confirm the app running on localhost with default 5000 port

C:\app>python app.py
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 403-783-412
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000// (Press CTRL+C to quit)
```
