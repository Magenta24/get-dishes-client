import os
# Enabling CSRF protection
WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret-key-1234-#$%^'

# setting prject's base directory
basedir = os.path.abspath(os.path.dirname(__file__))

GRAPH_SERVICE_URL = 'http://127.0.0.1'
SERVICE1_URL = 'http://127.0.0.1:5000'