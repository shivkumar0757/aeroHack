from flask import Response
from app import app



@app.route('/')
def index():
    data='{"status":"success","data":[{"id":1,"employee_name":"Tiger Nixon","employee_salary":320800,"employee_age":61,"profile_image":""},{"id":2,"employee_name":"Garrett Winters","employee_salary":170750,"employee_age":63,"profile_image":""}],"message":"Successfully! All records has been fetched."}'
    return data

@app.route('/ping')
def ping():
    return Response("OK",status=200)


# ====================