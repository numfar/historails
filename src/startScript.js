var myLayer;
var geoStations;
var mymap;
var yearSet = 1855;

function onEachFeature(feature, layer){
    layer.bindPopup(feature.properties.popupContent);
}

function filtrera(feature,layer){

    if(feature.properties.year.substring(0,4) > yearSet){
        return 0;
    }

    return 1;
}

function showMap() {
    mymap = L.map('mapid').setView([58.3251172, 15.0710935], 6);
    var accessToken = 'pk.eyJ1IjoibnVtZmFyIiwiYSI6ImNqN2F2NXdhcjBlcGMzMnN0a2wxaDd3YnoifQ.HZKACURfmAwSBLKkGVOprA';
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
		maxZoom: 18,
		id: 'mapbox.streets',
		accessToken: 'pk.eyJ1IjoibnVtZmFyIiwiYSI6ImNqN2F2NXdhcjBlcGMzMnN0a2wxaDd3YnoifQ.HZKACURfmAwSBLKkGVOprA'
		}).addTo(mymap);

    geoStations = getPoints();
    rendreraSkiten(geoStations);
  
}

function rendreraSkiten(geoS){
    var stations = [];
    for(i = 0; i < geoS.length ; i++){
	for(j=0 ; j < geoS[i].length ; j++){
            stations.push(geoS[i][j]);
        }
    }
    myLayer = L.geoJSON(stations,{onEachFeature: onEachFeature, filter:filtrera}).addTo(mymap);

    for(t = 0; t < geoS.length; t++){
        c = [];
        for(q = 0; q < geoS[t].length ; q++ ) {
	    pathCoords = geoS[t][q].geometry.coordinates;
            c.push([pathCoords[0],pathCoords[1]]);
        }
        //console.log(c);
        line = L.polyline(c,{color: 'red', weight: 12});
	geoline = line.toGeoJSON();
	L.geoJSON(geoline).addTo(mymap);
    }
}

function applyFiltery(yearIn) {
    myLayer.clearLayers();
    yearSet = yearIn;
    rendreraSkiten(geoStations);
}

$(document).ready( function() {
	$( "#slider" ).slider();
	showMap();
    });
  