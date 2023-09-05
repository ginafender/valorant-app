# Project 4
## An interactive data analysis of the video game VALORANT that helps new players better understand the game and its current metas.
Link to presentation: (https://github.com/ginafender/valorant-app/blob/main/Valorant%20PowerPoint.pptx)

- Group Members:
	- Gina Fender
	- John Xuereb
	- Oliver Einarsson
	- Acarie Jenkins
	- Naomi Martin

## Project Description
Our project was to create an interactive website that would allow new players to better understand the game Valorant. By using our website and looking at our data, these players can analyze the gameplay of others areound their own skill level, and begin to improve their own gameplay. When loading the website, the player starts out on the main page. Each individual map has a tab that links to a new page for that map. Once loaded into the new page, an image of the map and all of the death coordinate markers will populate. These markers can be filtered by competitive tier, by what character the person was playing, or by both. This will help the player to see where common death locations are, and what areas of the map should be played passively or aggresively. On the analysis side, the data helps players to understand current meta picks for agents, and other various data points within the game.

- Data Source:
  - Match Data: https://stelar7.no/valorant/
  - Character Data: https://valorant-api.com/v1/agents
  - Map Data: https://valorant-api.com/v1/maps

# File Structure
There are four folders in this repository which contain the files of primary importance. The templates folder contains all html files for the website. The json folder holds all the data used for the project. The static folder contains all relevant images for the project. The SQLite folder contains all files pertaining to the SQL databases. A brief description of each is provided below. 

## Templates Folder
1. index.html
	- This file contains the html and css styling for the main page of the website. Within this file contains ```url_for``` links to each individual map page.
2. Individual map files
   	- Each individual map has its own html file for clarity/readability purposes, but each file is structured the same way. The file starts off with css styling, and then heads into the html portion. Within the html portion, there is code for the header, the map image, and both dropdown buttons. Following the html section is the JavaScript section. Within the JS section, several functions are called. The ```updateMarkers``` function is used to update the markers on the webpage every time a change is made, or one of the dropdowns are selected. Within this function, the coordinate calculations are performed. The original coordinates given within the data are scaled to the in-game map, and need to be scaled down to fit on the image of the mini map. The following conversions are given by the api documents and had to be integrated into our code to fit our needs:
   	      ```x = game_y * valorant-api_map_x_multiplier + valorant-api_map_x_scalar_add;
y = game_x * valorant-api_map_y_multiplier + valorant-api_map_y_scalar_add;
x *= image.Width;
y *= image.Height;```. The last function used is the ```mapImage.onload```. By calling the other functions within this function, we can ensure the map image is loaded onto the page before trying to perform any other functions.
-- This code is repeated on all the html files and adjusted to fit each map accordingly. 

## Json Folder
1. maps.ipynb
   - This jupyter notebook was used to extract json information about the maps from the api.
3. valorant.ipynb
   - This jupyter notebook was used to extract json information about the matches from the api.
4. characters.ipynb
   - This jupyter notebook was used to extract json information about the characters from the api
5. characterMapping.json
   - This json file was created to be used to dynamically map character options to the webpage dropdown. By creating this json file where every ```key``` is the uuid of the character, and every ```value``` is the name of the character, the flask routes can link the two together and and the **name** value to the dropdown box for better readability. By dynamically coding the dropdown box, we can have only the characters that we have data for populate the dropdown box and avoid potentially cluttering the readability of the options list.

## Static Folder
1. map_images
	- This folder contains all the images pertaining to each map. The images titled ```image```, i.e ```ascent_image.png```, are the full size map images used to populate the death coordinate markers. The images titled ```splash```, i.e ```ascent_splash.png```, are the header images displayed at the top of each page.
2. website_images
	- This folder contains any other images used on the site.

## SQLite Folder
1. Valorant.sqlite
   - This
3. schema.ipynb
   - This
4. ER.PNG
   - This

# Run Sequence 

The dashboard is ran through Flask, so to deploy it, one must download the relevant files and launch the site using ```python app.py``` in the terminal. This will return a local host link. Following the link will take you directly to the web page. 
