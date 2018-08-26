function onEachFeature(feature, layer){
    layer.bindPopup(feature.properties.popupContent);
}

function filterFeature(feature, layer){

    if(feature.properties.year.substring(0,4) > $( "#year" ).val()){
        return false;
    }

    return true;
}

function setSlider(){
    $( "#slider" ).slider( "value", $( "#year" ).val() );
}

function setupSpinner(route, startYear, myLayer, mymap) {
    $( "#slider" ).slider({
	value:1855,
	min: startYear,
	max: 2017,
	step: 1,
	slide: function( event, ui ) {
            $( "#year" ).val( ui.value );
            myLayer.clearLayers();
            myLayer = L.geoJSON(route, {onEachFeature: onEachFeature, filter:filterFeature}).addTo(mymap);
	}
    });
    $( "#year" ).val( $( "#slider" ).slider( "value" ) );
    $( "#year" ).on('input', setSlider);
}

function setupMapWithFilter(route, token) {
    return setupMap(route, token, {onEachFeature: onEachFeature, filter:filterFeature}, [58.3251172, 15.0710935], 6);
}

function setupMapWithAdded(route, token) {
    setupMap(route, token, {onEachFeature: onEachFeature}, getCenterOfRoute(route), 6);
}

function setupMap(route, token, options, center, zoom) {

    var mymap = L.map('mapid').setView(center, zoom);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
		maxZoom: 18,
		id: 'mapbox.streets',
		accessToken: token
    }).addTo(mymap);
    var myLayer = L.geoJSON(route, options).addTo(mymap);
    return [mymap, myLayer];
}