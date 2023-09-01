""" 
Flask app for each individual map.
"""
import json
from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static'


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
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)
###################### DEATH LOCATIONS ###############################
    mapURL = '/Game/Maps/Ascent/Ascent'
    death_coordinates = []
    round_results = []

    matches = match_data['matches']
    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

        # Iterate through player stats for each round
        for round_result in round_results:
            for player_stat in round_result['playerStats']:
                kills = player_stat['kills']

                # Iterate through kills for each player
                for kill in kills:
                    if 'victimLocation' in kill:
                        victim_location = kill['victimLocation']
                        death_coordinates.append(victim_location)

    map_data = maps['data'][0]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    mini_map_coordinates = []
    for death in death_coordinates:
        mini_x = death['y'] * x_Multiplier + x_ScalarToAdd
        mini_y = death['x'] * y_Multiplier + y_ScalarToAdd
        mini_map_coordinates.append({'x': mini_x, 'y': mini_y})

    image_path  = "valorant-app/static/map_images/ascent_image.png"
    return render_template('ascent.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates,
                            x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, x_ScalarToAdd=x_ScalarToAdd,
                            y_ScalarToAdd=y_ScalarToAdd)
###################### AGENT DROPDOWNS ###############################
#######################################################################
#################### SPLIT ############################################
@app.route("/split")
def split():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)

    mapURL = '/Game/Maps/Bonsai/Bonsai'
    death_coordinates = []
    round_results = []

    matches = match_data['matches']
    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

        # Iterate through player stats for each round
        for round_result in round_results:
            for player_stat in round_result['playerStats']:
                kills = player_stat['kills']

                # Iterate through kills for each player
                for kill in kills:
                    if 'victimLocation' in kill:
                        victim_location = kill['victimLocation']
                        death_coordinates.append(victim_location)

    map_data = maps['data'][1]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    mini_map_coordinates = []
    for death in death_coordinates:
        mini_x = death['y'] * x_Multiplier + x_ScalarToAdd
        mini_y = death['x'] * y_Multiplier + y_ScalarToAdd
        mini_map_coordinates.append({'x': mini_x, 'y': mini_y})

    image_path  = "valorant-app/static/map_images/split_image.png"
    return render_template('split.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates,
                            x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, x_ScalarToAdd=x_ScalarToAdd,
                            y_ScalarToAdd=y_ScalarToAdd)

#######################################################################
#################### FRACTURE #########################################
@app.route("/fracture")
def fracture():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)

    mapURL = "/Game/Maps/Canyon/Canyon"
    death_coordinates = []
    round_results = []

    matches = match_data['matches']
    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

        # Iterate through player stats for each round
        for round_result in round_results:
            for player_stat in round_result['playerStats']:
                kills = player_stat['kills']

                # Iterate through kills for each player
                for kill in kills:
                    if 'victimLocation' in kill:
                        victim_location = kill['victimLocation']
                        death_coordinates.append(victim_location)

    map_data = maps['data'][2]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    mini_map_coordinates = []
    for death in death_coordinates:
        mini_x = death['y'] * x_Multiplier + x_ScalarToAdd
        mini_y = death['x'] * y_Multiplier + y_ScalarToAdd
        mini_map_coordinates.append({'x': mini_x, 'y': mini_y})

    image_path  = "valorant-app/static/map_images/fracture_image.png"
    return render_template('fracture.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates,
                            x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, x_ScalarToAdd=x_ScalarToAdd,
                            y_ScalarToAdd=y_ScalarToAdd)

#######################################################################
#################### BIND #############################################

@app.route("/bind")
def bind():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)

    mapURL = "/Game/Maps/Duality/Duality"
    death_coordinates = []
    round_results = []

    matches = match_data['matches']
    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

        # Iterate through player stats for each round
        for round_result in round_results:
            for player_stat in round_result['playerStats']:
                kills = player_stat['kills']

                # Iterate through kills for each player
                for kill in kills:
                    if 'victimLocation' in kill:
                        victim_location = kill['victimLocation']
                        death_coordinates.append(victim_location)

    map_data = maps['data'][3]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    mini_map_coordinates = []
    for death in death_coordinates:
        mini_x = death['y'] * x_Multiplier + x_ScalarToAdd
        mini_y = death['x'] * y_Multiplier + y_ScalarToAdd
        mini_map_coordinates.append({'x': mini_x, 'y': mini_y})

    image_path  = "valorant-app/static/map_images/bind_image.png"
    return render_template('bind.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates,
                            x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, x_ScalarToAdd=x_ScalarToAdd,
                            y_ScalarToAdd=y_ScalarToAdd)

#######################################################################
#################### BREEZE ###########################################

@app.route("/breeze")
def breeze():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)

    mapURL = "/Game/Maps/Foxtrot/Foxtrot"
    death_coordinates = []
    round_results = []

    matches = match_data['matches']
    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

        # Iterate through player stats for each round
        for round_result in round_results:
            for player_stat in round_result['playerStats']:
                kills = player_stat['kills']

                # Iterate through kills for each player
                for kill in kills:
                    if 'victimLocation' in kill:
                        victim_location = kill['victimLocation']
                        death_coordinates.append(victim_location)

    map_data = maps['data'][4]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    mini_map_coordinates = []
    for death in death_coordinates:
        mini_x = death['y'] * x_Multiplier + x_ScalarToAdd
        mini_y = death['x'] * y_Multiplier + y_ScalarToAdd
        mini_map_coordinates.append({'x': mini_x, 'y': mini_y})

    image_path  = "valorant-app/static/map_images/breeze_image.png"
    return render_template('breeze.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates,
                            x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, x_ScalarToAdd=x_ScalarToAdd,
                            y_ScalarToAdd=y_ScalarToAdd)


#######################################################################
#################### LOTUS ############################################

@app.route("/lotus")
def lotus():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)

    mapURL = "/Game/Maps/Jam/Jam"
    death_coordinates = []
    round_results = []

    matches = match_data['matches']
    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

        # Iterate through player stats for each round
        for round_result in round_results:
            for player_stat in round_result['playerStats']:
                kills = player_stat['kills']

                # Iterate through kills for each player
                for kill in kills:
                    if 'victimLocation' in kill:
                        victim_location = kill['victimLocation']
                        death_coordinates.append(victim_location)

    map_data = maps['data'][8]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    mini_map_coordinates = []
    for death in death_coordinates:
        mini_x = death['y'] * x_Multiplier + x_ScalarToAdd
        mini_y = death['x'] * y_Multiplier + y_ScalarToAdd
        mini_map_coordinates.append({'x': mini_x, 'y': mini_y})

    image_path  = "valorant-app/static/map_images/lotus_image.png"
    return render_template('lotus.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates,
                            x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, x_ScalarToAdd=x_ScalarToAdd,
                            y_ScalarToAdd=y_ScalarToAdd)

#######################################################################
#################### PEARL ############################################

@app.route("/pearl")
def pearl():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)

    mapURL = "/Game/Maps/Pitt/Pitt"
    death_coordinates = []
    round_results = []

    matches = match_data['matches']
    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

        # Iterate through player stats for each round
        for round_result in round_results:
            for player_stat in round_result['playerStats']:
                kills = player_stat['kills']

                # Iterate through kills for each player
                for kill in kills:
                    if 'victimLocation' in kill:
                        victim_location = kill['victimLocation']
                        death_coordinates.append(victim_location)

    map_data = maps['data'][9]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    mini_map_coordinates = []
    for death in death_coordinates:
        mini_x = death['y'] * x_Multiplier + x_ScalarToAdd
        mini_y = death['x'] * y_Multiplier + y_ScalarToAdd
        mini_map_coordinates.append({'x': mini_x, 'y': mini_y})

    image_path  = "valorant-app/static/map_images/pearl_image.png"
    return render_template('pearl.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates,
                            x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, x_ScalarToAdd=x_ScalarToAdd,
                            y_ScalarToAdd=y_ScalarToAdd)

#######################################################################
#################### ICEBOX ###########################################

@app.route("/icebox")
def icebox():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)

    mapURL = "/Game/Maps/Port/Port"
    death_coordinates = []
    round_results = []

    matches = match_data['matches']
    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

        # Iterate through player stats for each round
        for round_result in round_results:
            for player_stat in round_result['playerStats']:
                kills = player_stat['kills']

                # Iterate through kills for each player
                for kill in kills:
                    if 'victimLocation' in kill:
                        victim_location = kill['victimLocation']
                        death_coordinates.append(victim_location)

    map_data = maps['data'][10]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    mini_map_coordinates = []
    for death in death_coordinates:
        mini_x = death['y'] * x_Multiplier + x_ScalarToAdd
        mini_y = death['x'] * y_Multiplier + y_ScalarToAdd
        mini_map_coordinates.append({'x': mini_x, 'y': mini_y})

    image_path  = "valorant-app/static/map_images/icebox_image.png"
    return render_template('icebox.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates,
                            x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, x_ScalarToAdd=x_ScalarToAdd,
                            y_ScalarToAdd=y_ScalarToAdd)

#######################################################################
#################### HAVEN ############################################

@app.route("/haven")
def haven():
    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)

    mapURL = "/Game/Maps/Triad/Triad"
    death_coordinates = []
    round_results = []

    matches = match_data['matches']
    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

        # Iterate through player stats for each round
        for round_result in round_results:
            for player_stat in round_result['playerStats']:
                kills = player_stat['kills']

                # Iterate through kills for each player
                for kill in kills:
                    if 'victimLocation' in kill:
                        victim_location = kill['victimLocation']
                        death_coordinates.append(victim_location)

    map_data = maps['data'][12]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    mini_map_coordinates = []
    for death in death_coordinates:
        mini_x = death['y'] * x_Multiplier + x_ScalarToAdd
        mini_y = death['x'] * y_Multiplier + y_ScalarToAdd
        mini_map_coordinates.append({'x': mini_x, 'y': mini_y})

    image_path  = "valorant-app/static/map_images/haven_image.png"
    return render_template('haven.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates,
                            x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, x_ScalarToAdd=x_ScalarToAdd,
                            y_ScalarToAdd=y_ScalarToAdd)

if __name__ == "__main__":
    app.run(debug=True)
