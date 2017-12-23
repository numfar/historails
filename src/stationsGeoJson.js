function getPoints() {

    var geojsonFeature = {
        "type": "Feature",
        "properties": {
	    "name": "Kärrgruvan",
	    "amenity": "Tågstation",
	    "popupContent": "Kärrgruvan utanför Norberg",
	    "year": "1856-06-29"
        },
        "geometry": {
	    "type": "Point",
	    "coordinates": [15.9365462,60.0913360]
        }
    };

    var geojsonFeature2 = {
        "type": "Feature",
        "properties": {
	    "name": "Ängelsberg station",
	    "amenity": "Tågstation",
	    "popupContent": "Ängelsberg station",
	    "year": "1856-06-29"
        },
        "geometry": {
	    "type": "Point",
	    "coordinates": [16.0098471, 59.9585172]
        }
    };

    var geojsonFeature3 = {
        "type": "Feature",
	"properties": {
            "name": "Södertälje station",
            "amenity": "Tågstation",
            "popupContent": "Start på Stockholms järnväg",
	    "year": "1860-01-01"
        },
        "geometry": {
            "type": "Point",
            "coordinates": [17.6271663,59.1964289]
        }
    };

    var geojsonFeature4 = {
        "type": "Feature",
        "properties": {
            "name": "Stockholm centralstation",
            "amenity": "Tågstation",
            "popupContent": "Stockholm C",
	    "year": "1860-01-01"
        },
        "geometry": {
            "type": "Point",
            "coordinates": [18.0710935,59.3251172]
        }
    };

    var geojsonFeature5 = {
        "type": "Feature",
	"properties": {
            "name": "Göteborg C",
            "amenity": "Tågstation",
            "popupContent": "Västra stambanan",
	    "year": "1862-01-01"
        },
        "geometry": {
            "type": "Point",
            "coordinates": [11.9670171,57.7072326]
        }
    };

    var geojsonFeature6 = {
        "type": "Feature",
        "properties": {
            "name": "Malmö Station",
            "amenity": "Tågstation",
            "popupContent": "Södra stambanan",
	    "year": "1864-01-01"
        },
        "geometry": {
            "type": "Point",
            "coordinates": [13.0001566, 55.6052931]
        }
    };

    var geojsonFeature7 = {
        "type": "Feature",
        "properties": {
            "name": "Nora station",
            "amenity": "Tågstation",
            "popupContent": "Nora station i Danderyd",
            "year": "1856-06-05"
        },
        "geometry": {
            "type": "Point",
            "coordinates": [ 18.0198648, 59.4130938]
        }
    };

	var geojsonFeature8 = {
	    "type": "Feature",
	    "properties": {
		"name": "Örebro station",
		"amenity": "Tågstation",
		"popupContent": "Välkommen till Örebro",
		"year": "1856-06-05"
	    },
	    "geometry": {
		"type": "Point",
		"coordinates": [ 15.2149988, 59.2747378 ]
	    }
	};


    var pointsR = [[geojsonFeature,geojsonFeature2],
		   [geojsonFeature3,geojsonFeature4],
		   [geojsonFeature5,geojsonFeature6],
		   [geojsonFeature7,geojsonFeature8]];

    return pointsR;
}