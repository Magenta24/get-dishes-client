import os
# Enabling CSRF protection
WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret-key-1234-#$%^'

# setting prject's base directory
basedir = os.path.abspath(os.path.dirname(__file__))

GRAPH_SERVICE_URL = '127.0.0.1'