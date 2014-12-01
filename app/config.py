#config.py 


import os

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'x14vvxe8x82x9d22rx86x12xe7x86xd3xd8woxe4x86x1dxe4tx94'

#grab the folder of the running script
basedir = os.path.abspath(os.path.dirname(__file__))

#defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)