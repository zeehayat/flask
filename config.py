import os 
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY =os.environ.get('SECRET_KEY') or 'you will never guess'
    SQLALCHEMORY = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'app.db')
    SQLALCHEMORY_TRACK_MODIFICATION = False

    