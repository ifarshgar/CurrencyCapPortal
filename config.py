import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'default secret'
DEBUG = True
