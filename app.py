from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)
PORT = 3500

#FILEPATH = "data.json"



@app.route("/", methods=["GET", "POST"])
def startpy():

    result = {

        "Greetings": "Tactlabs welcomes you"
    }

    return render_template("index.html")




@app.route("/data", methods=["GET"])
def read_json():

    #data = None
    #with open(FILEPATH) as json_file:
     #   data = json.load(json_file)

    
    bike_list = ['Kawasaki', 'Suzuki', 'Honda', 'Triumph', 'Harley Davidson', 'Royal Enfield']

    per_list =[23, 5, 3, 14, 42, 13]

    result_dict = {
        'bike': bike_list,
        #'local_data': data,
        'bike_names': 'bike names',
        'title': 'Market share by volume - superbikes & imports 2018',
        'subtitle': 'Source: https://www.team-bhp.com/forum/superbikes-imports/205960-2018-annual-report-card-superbikes-imports.html',
        'percent': per_list
    }

    

    return jsonify(result_dict)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
