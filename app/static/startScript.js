var myLayer;
var geoStations;
var mymap;
var yearSet = 1855;
var polyline = [];

function onEachFeature(feature, layer){
    layer.bindPopup(feature.properties.popupContent);
}

function filterFeature(feature, layer){

    if(feature.properties.year.substring(0,4) > yearSet){
        return 0;
    }

    return 1;
}

function showMap(accesstoken) {
    mymap = L.map('mapid').setView([58.3251172, 15.0710935], 6);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
		maxZoom: 18,
		id: 'mapbox.streets',
		accessToken: accesstoken
		}).addTo(mymap);

    geoStations = getPoints();
    renderRouteMap(geoStations);
  
}

function renderRouteMap(geoS){
    var stations = [];
    for(ii = 0; ii < polyline.length ; ii++ ) {
	mymap.removeLayer(polyline[ii]);
    }
    for(i = 0; i < geoS.length ; i++){
	for(j=0 ; j < geoS[i].length ; j++){
            stations.push(geoS[i][j]);
        }
    }
    myLayer = L.geoJSON(stations,{onEachFeature: onEachFeature, filter:filterFeature}).addTo(mymap);

    for(t = 0; t < geoS.length; t++){
	c = [];
        for(q = 0; q < geoS[t].length ; q++ ) {
	    pathCoords = geoS[t][q].geometry.coordinates;
	    year = geoS[t][q].properties.year;
	    year = parseInt(year.split("-")[0])
	    if (year <= yearSet){
		c.push([pathCoords[1],pathCoords[0]]);
            }
        }
	polyline.push(L.polyline(c).addTo(mymap));
    }

}

function applyYearFilter(yearIn) {
    myLayer.clearLayers();
    yearSet = yearIn;
    renderRouteMap(geoStations);
}
