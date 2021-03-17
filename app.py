from flask import Flask
import overpass
from flask import request, jsonify
from flask import render_template
import sys
app = Flask(__name__)
app.config["DEBUG"] = True

api = overpass.API()



@app.route("/api/", methods=['GET'])
def home():
    return render_template("homepage.html");

@app.route("/api/restos")
def restos():
    return jsonify(api.get("""out;"""))

@app.route('/api/restos/', methods=['GET'])
def api_q():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'q' in request.args:
        q = request.args['q']
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    if request.method == "GET":
        response = api.get(f"""area[name="{q}"]; node["amenity"="restaurant"](area);out;""")
        return jsonify(response)