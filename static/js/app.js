const match_url = "http://stelar7.no/valorant/eu/1641211632.json";
const map_url = "https://valorant-api.com/v1/maps";
const character_url = "https://valorant-api.com/v1/agents";

// Get all death coordinates
function deathCoordinates(deaths) {
    Promise.all([
        d3.json(match_url),
        d3.json(map_url)
    ]).then(function([data01, data02]){
        let matches = data01.matches;
        let mapId = matches.mapId;
        
    });
};
