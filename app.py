import flask
from flask import request, jsonify
import Student_generator as sg

# Create a flask app object
app = flask.Flask(__name__)

# Tell the server to reload each time the code changes
app.config["DEBUG"] = True

"""
# Function to query the list of student dictionaries based on a search key, and a value
# Input: search_key - key in the dictionary we want to check the value of
        # Search_value - the value of the key we need to match
# Output: a list of student dictionaries that match te search criteria
"""
def search_dictionary_list(search_key, search_value):
    student_dictionaries = sg.get_student_dictionaries()
    Included_students = []
    for student in [student_dictionaries]:
        if search_value.lower() == student[search_key]:
            Included_students.append(student)
        else:
            continue
    print(Included_students)
# Create a route/view for the home page of the application
@app.route('/', methods=['GET'])
def index():
    return "<h1>Student Data API</h1>"

# Create end points for the functions we will create
# Create a route to return all student data
@app.route('/api/students/all', methods=['GET'])
def api_all():
    # get student dictionaries
    student_dictionaries = sg.get_student_dictionaries()
    return jsonify(student_dictionaries)

# Create a route that returns students in a specific major
# Create a route that returns student of a specifc class (freshman, sophomore, junior, senior)
# Create a route that returns a specific student by ID

# Run the application
app.run(debug=True)
search_dictionary_list