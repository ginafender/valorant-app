import json
from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return render_template('index.html')

#######################################################################
#################### ASCENT ###########################################

@app.route("/ascent")
def ascent():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        data = json.load(json_file)
    image_path  = data['data'][0]['displayIcon']
    return render_template('ascent.html', image_path=image_path)

#######################################################################
#################### SPLIT ############################################

@app.route("/split")
def split():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        data = json.load(json_file)
    image_path  = data['data'][1]['displayIcon']
    return render_template('split.html', image_path=image_path)

#######################################################################
#################### FRACTURE #########################################

@app.route("/fracture")
def fracture():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        data = json.load(json_file)
    image_path  = data['data'][2]['displayIcon']
    return render_template('fracture.html', image_path=image_path)

#######################################################################
#################### BIND #############################################

@app.route("/bind")
def bind():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        data = json.load(json_file)
    image_path  = data['data'][3]['displayIcon']
    return render_template('bind.html', image_path=image_path)

#######################################################################
#################### BREEZE ###########################################

@app.route("/breeze")
def breeze():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        data = json.load(json_file)
    image_path  = data['data'][4]['displayIcon']
    return render_template('breeze.html', image_path=image_path)


#######################################################################
#################### LOTUS ############################################

@app.route("/lotus")
def lotus():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        data = json.load(json_file)
    image_path  = data['data'][8]['displayIcon']
    return render_template('lotus.html', image_path=image_path)

#######################################################################
#################### PEARL ############################################

@app.route("/pearl")
def pearl():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        data = json.load(json_file)
    image_path  = data['data'][9]['displayIcon']
    return render_template('pearl.html', image_path=image_path)

#######################################################################
#################### ICEBOX ###########################################

@app.route("/icebox")
def icebox():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        data = json.load(json_file)
    image_path  = data['data'][10]['displayIcon']
    return render_template('icebox.html', image_path=image_path)

#######################################################################
#################### HAVEN ############################################

@app.route("/haven")
def haven():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        data = json.load(json_file)
    image_path  = data['data'][12]['displayIcon']
    return render_template('haven.html', image_path=image_path)

if __name__ == "__main__":
    app.run(debug=True)
