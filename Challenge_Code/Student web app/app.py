from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#make a Flask app
app = Flask(__name__)
app.config["DEBUG"] = True

#set secret key
app.config["SECRET_KEY"] = "your secret key"

"""
Function to request student data from the api
Input: url
Output: JSON student data
"""
def get_student_data(url:str):

    response = requests.get(url)

    response_json = response.json()

    return response_json

# Create a route for the website index/root/homepage. will display all student data

@app.route('/', methods=['GET'])
def index():
    url = "http://127.0.0.1:5000/api/students/all"
    student_data = get_student_data(url)

    # Send the list of majors to the majors template
    return render_template('index.html', student_data=student_data)

# Create a route for the majors seach page to respond to get requests
@app.route('/majors', methods=['GET'])
def majors_get():
    # Get the list of majors
    url = "http://127.0.0.1:5000/api/majors/all"
    major_list = get_student_data(url)
    # Send the list of majors to the majors template to populate the menu
    return render_template('majors.html', major_list=major_list)

# Create a route for the majors seach page to respond to POST requests after the form is submitted
@app.route('/majors', methods={'POST'})
def majors_post():
    # Get the list of majors
    url = "http://127.0.0.1:5000/api/majors/all"
    major_list = get_student_data(url)
    
    # Get the form data: the chosen major from the select menu
    major = request.form.get('major')

    # if major is invalid, display error and reload page
    if major == "":
        flash("ERROR: Please select a major")
        return redirect(url_for('majors_get'))

    # Create a url to get students from that major
    url = f"http://127.0.0.1:5000/api/majors/{major}"

    # Send the request and get the response
    result_list = get_student_data(url)

    # Send all the data to the majors template to be displayed in the browser
    return render_template('majors.html', major_list=major_list, result_list=result_list, major=major)


# Run the flask app
app.run(port=5001)
