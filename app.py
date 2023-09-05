""" 
Flask app for each individual map.
"""

import json
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return render_template('index.html')
# ----------------------- ASCENT -----------------------
@app.route("/ascent")
def ascent():
    """ Function for ascent map route """
    selected_tier = request.args.get('tier')  # Get the selected tier from request args

    with open("..//valorant-app/json/valorantmaps.json", "r", encoding="utf-8") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r", encoding="utf-8") as map_file:
        match_data = json.load(map_file)
    with open("..//valorant-app/json/characterMapping.json", "r", encoding="utf-8") as char_map_file:
        character_mapping = json.load(char_map_file)

    mapURL = '/Game/Maps/Ascent/Ascent'
    death_coordinates = []

    map_data = maps['data'][0]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    matches = match_data['matches']

    # Create a set to store unique character IDs
    unique_character_ids = set()
    unique_character_list = []

    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

            # Create a dictionary to map player puuids to competitive tiers, character IDs, and character names
            player_data_dict = {
                player['puuid']: {
                    'competitiveTier': player['competitiveTier'],
                    'characterId': player['characterId'],
                    'characterName': character_mapping.get(player['characterId'], "Unknown Character")
                }
                for player in match['players']
            }

            # Iterate through player stats for each round
            for round_result in round_results:
                for player_stat in round_result['playerStats']:
                    kills = player_stat['kills']

                    # Iterate through kills for each player
                    for kill in kills:
                        if 'victimLocation' in kill:
                            victim_location = kill['victimLocation']

                            # Check if the competitive tier matches the selected tier
                            player_puuid = player_stat['puuid']
                            player_tier = player_data_dict.get(player_puuid, {}).get('competitiveTier')
                            character_id = player_data_dict.get(player_puuid, {}).get('characterId')
                            character_name = player_data_dict.get(player_puuid, {}).get('characterName')

                            # Filter by competitive tier and set mini_x and mini_y
                            if selected_tier is None or player_tier == selected_tier:
                                death_coordinates.append({
                                    'x': victim_location['y'] * x_Multiplier + x_ScalarToAdd,
                                    'y': victim_location['x'] * y_Multiplier + y_ScalarToAdd,
                                    'player_puuid': player_puuid,
                                    'player_tier': player_tier,
                                    'character_id': character_id,
                                    'character_name': character_name  # Include character name
                                })

                                # Add character IDs to the set for uniqueness
                                unique_character_ids.add(character_id)

    # Create a list of unique characters
    for character_id in unique_character_ids:
        unique_character_list.append({
            'character_id': character_id,
            'character_name': character_mapping.get(character_id, "Unknown Character")
        })

    mini_map_coordinates = []

    for death in death_coordinates:
        mini_x = death['x']
        mini_y = death['y']
        mini_map_coordinates.append({
            'x': mini_x,
            'y': mini_y,
            'player_puuid': death['player_puuid'],
            'player_tier': death['player_tier'],
            'character_id': death['character_id'],  # Store the UUID here
        })


    image_path = "valorant-app/static/map_images/ascent_image.png"

    return render_template('ascent.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates, 
                        unique_character_list=unique_character_list, x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, 
                        x_ScalarToAdd=x_ScalarToAdd, y_ScalarToAdd=y_ScalarToAdd)


# ----------------------- split -----------------------
@app.route("/split")
def split():
    selected_tier = request.args.get('tier')  # Get the selected tier from request args

    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)
    with open("..//valorant-app/json/characterMapping.json", "r") as char_map_file:
        character_mapping = json.load(char_map_file)

    mapURL = '/Game/Maps/Bonsai/Bonsai'
    death_coordinates = []

    map_data = maps['data'][1]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    matches = match_data['matches']

    # Create a set to store unique character IDs
    unique_character_ids = set()
    unique_character_list = []

    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

            # Create a dictionary to map player puuids to competitive tiers, character IDs, and character names
            player_data_dict = {
                player['puuid']: {
                    'competitiveTier': player['competitiveTier'],
                    'characterId': player['characterId'],
                    'characterName': character_mapping.get(player['characterId'], "Unknown Character")
                }
                for player in match['players']
            }

            # Iterate through player stats for each round
            for round_result in round_results:
                for player_stat in round_result['playerStats']:
                    kills = player_stat['kills']

                    # Iterate through kills for each player
                    for kill in kills:
                        if 'victimLocation' in kill:
                            victim_location = kill['victimLocation']

                            # Check if the competitive tier matches the selected tier
                            player_puuid = player_stat['puuid']
                            player_tier = player_data_dict.get(player_puuid, {}).get('competitiveTier')
                            character_id = player_data_dict.get(player_puuid, {}).get('characterId')
                            character_name = player_data_dict.get(player_puuid, {}).get('characterName')

                            # Filter by competitive tier and set mini_x and mini_y
                            if selected_tier is None or player_tier == selected_tier:
                                death_coordinates.append({
                                    'x': victim_location['y'] * x_Multiplier + x_ScalarToAdd,
                                    'y': victim_location['x'] * y_Multiplier + y_ScalarToAdd,
                                    'player_puuid': player_puuid,
                                    'player_tier': player_tier,
                                    'character_id': character_id,
                                    'character_name': character_name  # Include character name
                                })

                                # Add character IDs to the set for uniqueness
                                unique_character_ids.add(character_id)

    # Create a list of unique characters
    for character_id in unique_character_ids:
        unique_character_list.append({
            'character_id': character_id,
            'character_name': character_mapping.get(character_id, "Unknown Character")
        })

    mini_map_coordinates = []

    for death in death_coordinates:
        mini_x = death['x']
        mini_y = death['y']
        mini_map_coordinates.append({
            'x': mini_x,
            'y': mini_y,
            'player_puuid': death['player_puuid'],
            'player_tier': death['player_tier'],
            'character_id': death['character_id'],  # Store the UUID here
        })


    image_path = "valorant-app/static/map_images/split_image.png"

    return render_template('split.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates, 
                        unique_character_list=unique_character_list, x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, 
                        x_ScalarToAdd=x_ScalarToAdd, y_ScalarToAdd=y_ScalarToAdd)

# ----------------------- fracture -----------------------
@app.route("/fracture")
def fracture():
    selected_tier = request.args.get('tier')  # Get the selected tier from request args

    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)
    with open("..//valorant-app/json/characterMapping.json", "r") as char_map_file:
        character_mapping = json.load(char_map_file)

    mapURL = '/Game/Maps/Canyon/Canyon'
    death_coordinates = []

    map_data = maps['data'][2]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    matches = match_data['matches']

    # Create a set to store unique character IDs
    unique_character_ids = set()
    unique_character_list = []

    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

            # Create a dictionary to map player puuids to competitive tiers, character IDs, and character names
            player_data_dict = {
                player['puuid']: {
                    'competitiveTier': player['competitiveTier'],
                    'characterId': player['characterId'],
                    'characterName': character_mapping.get(player['characterId'], "Unknown Character")
                }
                for player in match['players']
            }

            # Iterate through player stats for each round
            for round_result in round_results:
                for player_stat in round_result['playerStats']:
                    kills = player_stat['kills']

                    # Iterate through kills for each player
                    for kill in kills:
                        if 'victimLocation' in kill:
                            victim_location = kill['victimLocation']

                            # Check if the competitive tier matches the selected tier
                            player_puuid = player_stat['puuid']
                            player_tier = player_data_dict.get(player_puuid, {}).get('competitiveTier')
                            character_id = player_data_dict.get(player_puuid, {}).get('characterId')
                            character_name = player_data_dict.get(player_puuid, {}).get('characterName')

                            # Filter by competitive tier and set mini_x and mini_y
                            if selected_tier is None or player_tier == selected_tier:
                                death_coordinates.append({
                                    'x': victim_location['y'] * x_Multiplier + x_ScalarToAdd,
                                    'y': victim_location['x'] * y_Multiplier + y_ScalarToAdd,
                                    'player_puuid': player_puuid,
                                    'player_tier': player_tier,
                                    'character_id': character_id,
                                    'character_name': character_name  # Include character name
                                })

                                # Add character IDs to the set for uniqueness
                                unique_character_ids.add(character_id)

    # Create a list of unique characters
    for character_id in unique_character_ids:
        unique_character_list.append({
            'character_id': character_id,
            'character_name': character_mapping.get(character_id, "Unknown Character")
        })

    mini_map_coordinates = []

    for death in death_coordinates:
        mini_x = death['x']
        mini_y = death['y']
        mini_map_coordinates.append({
            'x': mini_x,
            'y': mini_y,
            'player_puuid': death['player_puuid'],
            'player_tier': death['player_tier'],
            'character_id': death['character_id'],  # Store the UUID here
        })


    image_path = "valorant-app/static/map_images/fracture_image.png"

    return render_template('fracture.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates, 
                        unique_character_list=unique_character_list, x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, 
                        x_ScalarToAdd=x_ScalarToAdd, y_ScalarToAdd=y_ScalarToAdd)

# ----------------------- bind -----------------------
@app.route("/bind")
def bind():
    selected_tier = request.args.get('tier')  # Get the selected tier from request args

    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)
    with open("..//valorant-app/json/characterMapping.json", "r") as char_map_file:
        character_mapping = json.load(char_map_file)

    mapURL = '/Game/Maps/Duality/Duality'
    death_coordinates = []

    map_data = maps['data'][3]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    matches = match_data['matches']

    # Create a set to store unique character IDs
    unique_character_ids = set()
    unique_character_list = []

    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

            # Create a dictionary to map player puuids to competitive tiers, character IDs, and character names
            player_data_dict = {
                player['puuid']: {
                    'competitiveTier': player['competitiveTier'],
                    'characterId': player['characterId'],
                    'characterName': character_mapping.get(player['characterId'], "Unknown Character")
                }
                for player in match['players']
            }

            # Iterate through player stats for each round
            for round_result in round_results:
                for player_stat in round_result['playerStats']:
                    kills = player_stat['kills']

                    # Iterate through kills for each player
                    for kill in kills:
                        if 'victimLocation' in kill:
                            victim_location = kill['victimLocation']

                            # Check if the competitive tier matches the selected tier
                            player_puuid = player_stat['puuid']
                            player_tier = player_data_dict.get(player_puuid, {}).get('competitiveTier')
                            character_id = player_data_dict.get(player_puuid, {}).get('characterId')
                            character_name = player_data_dict.get(player_puuid, {}).get('characterName')

                            # Filter by competitive tier and set mini_x and mini_y
                            if selected_tier is None or player_tier == selected_tier:
                                death_coordinates.append({
                                    'x': victim_location['y'] * x_Multiplier + x_ScalarToAdd,
                                    'y': victim_location['x'] * y_Multiplier + y_ScalarToAdd,
                                    'player_puuid': player_puuid,
                                    'player_tier': player_tier,
                                    'character_id': character_id,
                                    'character_name': character_name  # Include character name
                                })

                                # Add character IDs to the set for uniqueness
                                unique_character_ids.add(character_id)

    # Create a list of unique characters
    for character_id in unique_character_ids:
        unique_character_list.append({
            'character_id': character_id,
            'character_name': character_mapping.get(character_id, "Unknown Character")
        })

    mini_map_coordinates = []

    for death in death_coordinates:
        mini_x = death['x']
        mini_y = death['y']
        mini_map_coordinates.append({
            'x': mini_x,
            'y': mini_y,
            'player_puuid': death['player_puuid'],
            'player_tier': death['player_tier'],
            'character_id': death['character_id'],  # Store the UUID here
        })


    image_path = "valorant-app/static/map_images/bind_image.png"

    return render_template('bind.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates, 
                        unique_character_list=unique_character_list, x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, 
                        x_ScalarToAdd=x_ScalarToAdd, y_ScalarToAdd=y_ScalarToAdd)


# ----------------------- breeze -----------------------
@app.route("/breeze")
def breeze():
    selected_tier = request.args.get('tier')  # Get the selected tier from request args

    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)
    with open("..//valorant-app/json/characterMapping.json", "r") as char_map_file:
        character_mapping = json.load(char_map_file)

    mapURL = '/Game/Maps/Foxtrot/Foxtrot'
    death_coordinates = []

    map_data = maps['data'][4]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    matches = match_data['matches']

    # Create a set to store unique character IDs
    unique_character_ids = set()
    unique_character_list = []

    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

            # Create a dictionary to map player puuids to competitive tiers, character IDs, and character names
            player_data_dict = {
                player['puuid']: {
                    'competitiveTier': player['competitiveTier'],
                    'characterId': player['characterId'],
                    'characterName': character_mapping.get(player['characterId'], "Unknown Character")
                }
                for player in match['players']
            }

            # Iterate through player stats for each round
            for round_result in round_results:
                for player_stat in round_result['playerStats']:
                    kills = player_stat['kills']

                    # Iterate through kills for each player
                    for kill in kills:
                        if 'victimLocation' in kill:
                            victim_location = kill['victimLocation']

                            # Check if the competitive tier matches the selected tier
                            player_puuid = player_stat['puuid']
                            player_tier = player_data_dict.get(player_puuid, {}).get('competitiveTier')
                            character_id = player_data_dict.get(player_puuid, {}).get('characterId')
                            character_name = player_data_dict.get(player_puuid, {}).get('characterName')

                            # Filter by competitive tier and set mini_x and mini_y
                            if selected_tier is None or player_tier == selected_tier:
                                death_coordinates.append({
                                    'x': victim_location['y'] * x_Multiplier + x_ScalarToAdd,
                                    'y': victim_location['x'] * y_Multiplier + y_ScalarToAdd,
                                    'player_puuid': player_puuid,
                                    'player_tier': player_tier,
                                    'character_id': character_id,
                                    'character_name': character_name  # Include character name
                                })

                                # Add character IDs to the set for uniqueness
                                unique_character_ids.add(character_id)

    # Create a list of unique characters
    for character_id in unique_character_ids:
        unique_character_list.append({
            'character_id': character_id,
            'character_name': character_mapping.get(character_id, "Unknown Character")
        })

    mini_map_coordinates = []

    for death in death_coordinates:
        mini_x = death['x']
        mini_y = death['y']
        mini_map_coordinates.append({
            'x': mini_x,
            'y': mini_y,
            'player_puuid': death['player_puuid'],
            'player_tier': death['player_tier'],
            'character_id': death['character_id'],  # Store the UUID here
        })


    image_path = "valorant-app/static/map_images/breeze_image.png"

    return render_template('breeze.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates, 
                        unique_character_list=unique_character_list, x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, 
                        x_ScalarToAdd=x_ScalarToAdd, y_ScalarToAdd=y_ScalarToAdd)


# ----------------------- lotus -----------------------
@app.route("/lotus")
def lotus():
    selected_tier = request.args.get('tier')  # Get the selected tier from request args

    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)
    with open("..//valorant-app/json/characterMapping.json", "r") as char_map_file:
        character_mapping = json.load(char_map_file)

    mapURL = '/Game/Maps/Jam/Jam'
    death_coordinates = []

    map_data = maps['data'][8]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    matches = match_data['matches']

    # Create a set to store unique character IDs
    unique_character_ids = set()
    unique_character_list = []

    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

            # Create a dictionary to map player puuids to competitive tiers, character IDs, and character names
            player_data_dict = {
                player['puuid']: {
                    'competitiveTier': player['competitiveTier'],
                    'characterId': player['characterId'],
                    'characterName': character_mapping.get(player['characterId'], "Unknown Character")
                }
                for player in match['players']
            }

            # Iterate through player stats for each round
            for round_result in round_results:
                for player_stat in round_result['playerStats']:
                    kills = player_stat['kills']

                    # Iterate through kills for each player
                    for kill in kills:
                        if 'victimLocation' in kill:
                            victim_location = kill['victimLocation']

                            # Check if the competitive tier matches the selected tier
                            player_puuid = player_stat['puuid']
                            player_tier = player_data_dict.get(player_puuid, {}).get('competitiveTier')
                            character_id = player_data_dict.get(player_puuid, {}).get('characterId')
                            character_name = player_data_dict.get(player_puuid, {}).get('characterName')

                            # Filter by competitive tier and set mini_x and mini_y
                            if selected_tier is None or player_tier == selected_tier:
                                death_coordinates.append({
                                    'x': victim_location['y'] * x_Multiplier + x_ScalarToAdd,
                                    'y': victim_location['x'] * y_Multiplier + y_ScalarToAdd,
                                    'player_puuid': player_puuid,
                                    'player_tier': player_tier,
                                    'character_id': character_id,
                                    'character_name': character_name  # Include character name
                                })

                                # Add character IDs to the set for uniqueness
                                unique_character_ids.add(character_id)

    # Create a list of unique characters
    for character_id in unique_character_ids:
        unique_character_list.append({
            'character_id': character_id,
            'character_name': character_mapping.get(character_id, "Unknown Character")
        })

    mini_map_coordinates = []

    for death in death_coordinates:
        mini_x = death['x']
        mini_y = death['y']
        mini_map_coordinates.append({
            'x': mini_x,
            'y': mini_y,
            'player_puuid': death['player_puuid'],
            'player_tier': death['player_tier'],
            'character_id': death['character_id'],  # Store the UUID here
        })


    image_path = "valorant-app/static/map_images/lotus_image.png"

    return render_template('lotus.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates, 
                        unique_character_list=unique_character_list, x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, 
                        x_ScalarToAdd=x_ScalarToAdd, y_ScalarToAdd=y_ScalarToAdd)

# ----------------------- pearl -----------------------
@app.route("/pearl")
def pearl():
    selected_tier = request.args.get('tier')  # Get the selected tier from request args

    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)
    with open("..//valorant-app/json/characterMapping.json", "r") as char_map_file:
        character_mapping = json.load(char_map_file)

    mapURL = '/Game/Maps/Pitt/Pitt'
    death_coordinates = []

    map_data = maps['data'][9]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    matches = match_data['matches']

    # Create a set to store unique character IDs
    unique_character_ids = set()
    unique_character_list = []

    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

            # Create a dictionary to map player puuids to competitive tiers, character IDs, and character names
            player_data_dict = {
                player['puuid']: {
                    'competitiveTier': player['competitiveTier'],
                    'characterId': player['characterId'],
                    'characterName': character_mapping.get(player['characterId'], "Unknown Character")
                }
                for player in match['players']
            }

            # Iterate through player stats for each round
            for round_result in round_results:
                for player_stat in round_result['playerStats']:
                    kills = player_stat['kills']

                    # Iterate through kills for each player
                    for kill in kills:
                        if 'victimLocation' in kill:
                            victim_location = kill['victimLocation']

                            # Check if the competitive tier matches the selected tier
                            player_puuid = player_stat['puuid']
                            player_tier = player_data_dict.get(player_puuid, {}).get('competitiveTier')
                            character_id = player_data_dict.get(player_puuid, {}).get('characterId')
                            character_name = player_data_dict.get(player_puuid, {}).get('characterName')

                            # Filter by competitive tier and set mini_x and mini_y
                            if selected_tier is None or player_tier == selected_tier:
                                death_coordinates.append({
                                    'x': victim_location['y'] * x_Multiplier + x_ScalarToAdd,
                                    'y': victim_location['x'] * y_Multiplier + y_ScalarToAdd,
                                    'player_puuid': player_puuid,
                                    'player_tier': player_tier,
                                    'character_id': character_id,
                                    'character_name': character_name  # Include character name
                                })

                                # Add character IDs to the set for uniqueness
                                unique_character_ids.add(character_id)

    # Create a list of unique characters
    for character_id in unique_character_ids:
        unique_character_list.append({
            'character_id': character_id,
            'character_name': character_mapping.get(character_id, "Unknown Character")
        })

    mini_map_coordinates = []

    for death in death_coordinates:
        mini_x = death['x']
        mini_y = death['y']
        mini_map_coordinates.append({
            'x': mini_x,
            'y': mini_y,
            'player_puuid': death['player_puuid'],
            'player_tier': death['player_tier'],
            'character_id': death['character_id'],  # Store the UUID here
        })


    image_path = "valorant-app/static/map_images/pearl_image.png"

    return render_template('pearl.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates, 
                        unique_character_list=unique_character_list, x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, 
                        x_ScalarToAdd=x_ScalarToAdd, y_ScalarToAdd=y_ScalarToAdd)

# ----------------------- icebox -----------------------
@app.route("/icebox")
def icebox():
    selected_tier = request.args.get('tier')  # Get the selected tier from request args

    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)
    with open("..//valorant-app/json/characterMapping.json", "r") as char_map_file:
        character_mapping = json.load(char_map_file)

    mapURL = '/Game/Maps/Port/Port'
    death_coordinates = []

    map_data = maps['data'][10]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    matches = match_data['matches']

    # Create a set to store unique character IDs
    unique_character_ids = set()
    unique_character_list = []

    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

            # Create a dictionary to map player puuids to competitive tiers, character IDs, and character names
            player_data_dict = {
                player['puuid']: {
                    'competitiveTier': player['competitiveTier'],
                    'characterId': player['characterId'],
                    'characterName': character_mapping.get(player['characterId'], "Unknown Character")
                }
                for player in match['players']
            }

            # Iterate through player stats for each round
            for round_result in round_results:
                for player_stat in round_result['playerStats']:
                    kills = player_stat['kills']

                    # Iterate through kills for each player
                    for kill in kills:
                        if 'victimLocation' in kill:
                            victim_location = kill['victimLocation']

                            # Check if the competitive tier matches the selected tier
                            player_puuid = player_stat['puuid']
                            player_tier = player_data_dict.get(player_puuid, {}).get('competitiveTier')
                            character_id = player_data_dict.get(player_puuid, {}).get('characterId')
                            character_name = player_data_dict.get(player_puuid, {}).get('characterName')

                            # Filter by competitive tier and set mini_x and mini_y
                            if selected_tier is None or player_tier == selected_tier:
                                death_coordinates.append({
                                    'x': victim_location['y'] * x_Multiplier + x_ScalarToAdd,
                                    'y': victim_location['x'] * y_Multiplier + y_ScalarToAdd,
                                    'player_puuid': player_puuid,
                                    'player_tier': player_tier,
                                    'character_id': character_id,
                                    'character_name': character_name  # Include character name
                                })

                                # Add character IDs to the set for uniqueness
                                unique_character_ids.add(character_id)

    # Create a list of unique characters
    for character_id in unique_character_ids:
        unique_character_list.append({
            'character_id': character_id,
            'character_name': character_mapping.get(character_id, "Unknown Character")
        })

    mini_map_coordinates = []

    for death in death_coordinates:
        mini_x = death['x']
        mini_y = death['y']
        mini_map_coordinates.append({
            'x': mini_x,
            'y': mini_y,
            'player_puuid': death['player_puuid'],
            'player_tier': death['player_tier'],
            'character_id': death['character_id'],  # Store the UUID here
        })


    image_path = "valorant-app/static/map_images/icebox_image.png"

    return render_template('icebox.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates, 
                        unique_character_list=unique_character_list, x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, 
                        x_ScalarToAdd=x_ScalarToAdd, y_ScalarToAdd=y_ScalarToAdd)

# ----------------------- haven -----------------------
@app.route("/haven")
def haven():
    selected_tier = request.args.get('tier')  # Get the selected tier from request args

    with open("..//valorant-app/json/valorantmaps.json", "r") as json_file:
        maps = json.load(json_file)
    with open("..//valorant-app/json/valorantmatches.json", "r") as map_file:
        match_data = json.load(map_file)
    with open("..//valorant-app/json/characterMapping.json", "r") as char_map_file:
        character_mapping = json.load(char_map_file)

    mapURL = '/Game/Maps/Triad/Triad'
    death_coordinates = []

    map_data = maps['data'][12]
    x_Multiplier = map_data['xMultiplier']
    y_Multiplier = map_data['yMultiplier']
    x_ScalarToAdd = map_data['xScalarToAdd']
    y_ScalarToAdd = map_data['yScalarToAdd']

    matches = match_data['matches']

    # Create a set to store unique character IDs
    unique_character_ids = set()
    unique_character_list = []

    # Iterate through rounds and their results
    for match in matches:
        if match['matchInfo']['mapId'] == mapURL:
            round_results = match['roundResults']

            # Create a dictionary to map player puuids to competitive tiers, character IDs, and character names
            player_data_dict = {
                player['puuid']: {
                    'competitiveTier': player['competitiveTier'],
                    'characterId': player['characterId'],
                    'characterName': character_mapping.get(player['characterId'], "Unknown Character")
                }
                for player in match['players']
            }

            # Iterate through player stats for each round
            for round_result in round_results:
                for player_stat in round_result['playerStats']:
                    kills = player_stat['kills']

                    # Iterate through kills for each player
                    for kill in kills:
                        if 'victimLocation' in kill:
                            victim_location = kill['victimLocation']

                            # Check if the competitive tier matches the selected tier
                            player_puuid = player_stat['puuid']
                            player_tier = player_data_dict.get(player_puuid, {}).get('competitiveTier')
                            character_id = player_data_dict.get(player_puuid, {}).get('characterId')
                            character_name = player_data_dict.get(player_puuid, {}).get('characterName')

                            # Filter by competitive tier and set mini_x and mini_y
                            if selected_tier is None or player_tier == selected_tier:
                                death_coordinates.append({
                                    'x': victim_location['y'] * x_Multiplier + x_ScalarToAdd,
                                    'y': victim_location['x'] * y_Multiplier + y_ScalarToAdd,
                                    'player_puuid': player_puuid,
                                    'player_tier': player_tier,
                                    'character_id': character_id,
                                    'character_name': character_name  # Include character name
                                })

                                # Add character IDs to the set for uniqueness
                                unique_character_ids.add(character_id)

    # Create a list of unique characters
    for character_id in unique_character_ids:
        unique_character_list.append({
            'character_id': character_id,
            'character_name': character_mapping.get(character_id, "Unknown Character")
        })

    mini_map_coordinates = []

    for death in death_coordinates:
        mini_x = death['x']
        mini_y = death['y']
        mini_map_coordinates.append({
            'x': mini_x,
            'y': mini_y,
            'player_puuid': death['player_puuid'],
            'player_tier': death['player_tier'],
            'character_id': death['character_id'],  # Store the UUID here
        })


    image_path = "valorant-app/static/map_images/haven_image.png"

    return render_template('haven.html', image_path=image_path, mini_map_coordinates=mini_map_coordinates, 
                        unique_character_list=unique_character_list, x_Multiplier=x_Multiplier, y_Multiplier=y_Multiplier, 
                        x_ScalarToAdd=x_ScalarToAdd, y_ScalarToAdd=y_ScalarToAdd)


if __name__ == "__main__":
    app.run(debug=True)
