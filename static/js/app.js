// function setPosition(element, x, y) {
//     element.style.left = x + 'px';
//     element.style.top = y + 'px';
// }
// // console.log("DOMContentLoaded event fired");

// function deathCoordinatesAscent() {
//     // console.log("Function called");

//     fetch("../json/valorantmatches.json")
//         .then(response => response.json())
//         .then(data01 => {
//             return Promise.all([
//                 data01,
//                 fetch("../json/valorantmaps.json").then(response => response.json())
//             ]);
//         })
//             .then(([data01, data02]) => {
//                 const matches = data01.matches;
//                 const deathsLocations = [];
//                 const mapUrl = "/Game/Maps/Ascent/Ascent";
//                 const mapContainer = document.getElementById('mapContainer'); 

//                 if (data02 && data02.data) {
//                     const mapData = data02.data.find(map => map.mapUrl === mapUrl);

//                     if (mapData) {
//                         const xMulti = mapData.xMultiplier;
//                         const xScalar = mapData.xScalarToAdd;
//                         const yMulti = mapData.yMultiplier;
//                         const yScalar = mapData.yScalarToAdd;
//                         // console.log("Stuff: ", xMulti, xScalar, yMulti, yScalar);

//                         for (const match of matches) {
//                             if (match.matchInfo.mapId === mapUrl) {
//                                 const roundResults = match.roundResults;

//                                 for (const roundResult of roundResults) {
//                                     for (const player_stat of roundResult.playerStats) {
//                                         const kills = player_stat.kills;

//                                         for (const kill of kills) {
//                                             if ('victimLocation' in kill) {
//                                                 const victim_location = kill.victimLocation;
//                                                 deathsLocations.push(victim_location);
//                                                 // console.log(deathsLocations);
//                                             }
//                                         }
//                                     }
//                                 }
//                             }
//                         }

//                         const mapImage = document.getElementById('mapImage');
//                         mapImage.onload = function () {
//                             console.log("Map Image loaded")
//                             const mapWidth = mapImage.width;
//                             const mapHeight = mapImage.height;

//                             deathsLocations.forEach(death => {
//                                 const mini_x = death.y * xMulti + xScalar;
//                                 const mini_y = death.x * yMulti + yScalar;
//                                 console.log("x: ", mini_x, "y: ", mini_y)

//                                 const marker = document.createElement('div');
//                                 marker.className = 'coordinateMarker';
//                                 setPosition(marker, mini_x * mapWidth, mini_y * mapHeight);
//                                 mapContainer.appendChild(marker);
//                             });
//                         };
//                     } else {
//                         console.error(`Map data not found for map URL: ${mapUrl}`);
//                     }
//                 }
//             })
//             .catch(error => {
//                 console.error('Error fetching match data:', error);
//             });
//     }
// document.addEventListener("DOMContentLoaded", function () {
//     deathCoordinatesAscent();
// });