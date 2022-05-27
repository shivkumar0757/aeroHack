from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Enabling CORS
cors = CORS(app, resources={r"*": {"origins": "*"}})
#Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('configuration.ProductionConfig')
app.config.from_object('app.configuration.DevelopmentConfig')
#app.config.from_object('configuration.TestingConfig')


from app import views