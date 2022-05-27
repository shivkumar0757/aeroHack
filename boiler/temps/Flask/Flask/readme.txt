Local installation

make sure you have installed python3.x in your system.

using command line, navigate to project folder.
and use foollwoing commands:

-------------------
pip install flask

python run.py
------------------------
your application wil be running on http://localhost:5000/


Using with Frontend:
you can secure the by allowing cross origin requests to specific routes 
and specific origins
CORS(app, resources={r"{Route}": {"origins": "{allowed origin}"}})