$(document).ready(function() {
	 $( "#slider" ).slider({
		    value:1855,
			min: 1855,
			max: 2017,
			step: 1,
			slide: function( event, ui ) {
			    $( "#year" ).val( ui.value );
			    applyFiltery( ui.value );
		        }
		});
	    $( "#year" ).val( $( "#slider" ).slider( "value" ) );
 });