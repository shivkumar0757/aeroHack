Local installation

make sure you have installed python3.x in your system.

using command line, navigate to project folder.
and use foollwoing commands:

-------------------
pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
------------------------
your application wil be running on http://localhost:8000/


Using with Frontend:
Add URL of your application at end of Django/Setting.py 
CORS_ALLOWED_ORIGINS = [
    'Your_URL',
]