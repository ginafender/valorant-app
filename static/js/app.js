const match_url = "../json/valorantmatches.json";
const map_url = "../json/valorantmaps.json";
const character_url = "../json/valorantcharacters.json";

// Get all death coordinates
const mini_map_coordinates = [];

function deathCoordinates(mapName) {
    Promise.all([
        d3.json(match_url),
        d3.json(map_url)
    ]).then(function([data01, data02]){
        let matches = data01.data.matches;
        let mapId = data02.data.find(map => map.displayName === mapName).uuid;
        let deathsLocations = [];

        for (const match of matches) {
            // Iterate through rounds and their results
            if (match.matchInfo.mapId === mapId){ 
                let roundResults = match.roundResults;

                // Iterate through player stats for each round
                for (const roundResult of roundResults) {
                    for (const player_stat of roundResult.playerStats) {
                        const kills = playerStat.kills;
                        
                    // Iterate through kills for each player
                        for (const kill of kills) {
                            if ('victimLocation' in kill) {
                                const victim_location = kill.victimLocation;
                                deathsLocations.push(victim_location);
                            }
                        }
                    }
                }
            }
        }
        const xMulti = data02.data.xMultiplier;
        const xScalar = data02.data.xScalarToAdd;
        const yMulti = data02.data.yMultiplier;
        const yScalar = data02.data.yScalarToAdd;

        for (const death of deathsLocations) {
            const mini_x = death.y * xMulti + xScalar;
            const mini_y = death.x * yMulti + yScalar;
            mini_map_coordinates.push({ 'x': mini_x, 'y': mini_y });
            console.log("Adding coordinates:", { 'x: ': mini_x, 'y: ': mini_y})
        }
    });
}