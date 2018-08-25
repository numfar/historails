function onEachFeature(feature, layer){
    layer.bindPopup(feature.properties.popupContent);
}

function filterFeature(feature, layer){

    if(feature.properties.year.substring(0,4) > $( "#year" ).val()){
        return false;
    }

    return true;
}

function setupMap(route, token, startYear) {
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

    var mymap = L.map('mapid').setView([58.3251172, 15.0710935], 6);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
		maxZoom: 18,
		id: 'mapbox.streets',
		accessToken: token
    }).addTo(mymap);
    var myLayer = L.geoJSON(route, {onEachFeature: onEachFeature, filter:filterFeature}).addTo(mymap);

}
