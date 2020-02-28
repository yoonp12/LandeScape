
    function initMap() {
        //map options
        var options, map, marker, searchBox, infoWindow = '';
		addressEl = document.querySelector( '#map-search' ),
		latEl = document.querySelector( '.latitude' ),
		longEl = document.querySelector( '.longitude' ),
		map = document.getElementById( 'map' );
        city = document.querySelector( '.reg-input-city' );
    
        input = document.getElementById('search');
        searchBox = new google.maps.places.SearchBox(addressEl);
        
        infoWindow = new google.maps.InfoWindow;
        
        if (navigator.geolocation) {
            
            navigator.geolocation.getCurrentPosition(function (p) {
                var position = {
                    lat: p.coords.latitude,
                    lng: p.coords.longitude
                };
                var options = {
                    zoom:8,
                    center:{lat:p.coords.latitude, lng:p.coords.longitude},
                    disableDefaultUI: false, 
                    scrollWheel: true, 
                    draggable: true, 
                };
                var map = new google.maps.Map(document.getElementById('map'), options);
                
                marker = new google.maps.Marker({
                    position: options.center,
                    map: map,
                    draggable: true
                });

                map.addListener('bounds_changed', function(){
                    searchBox.setBounds(map.getBounds());
                });

                infoWindow.setPosition(position);
                infoWindow.setContent('<h3>You are here!</h3>');
                infoWindow.open(map);

                google.maps.event.addListener( marker, "dragend", function ( event ) {
                    var lat, long, address;
            
                    console.log( 'i am dragged' );
                    lat = marker.getPosition().lat();
                    long = marker.getPosition().lng();
                    
                    $.get(`https://www.hikingproject.com/data/get-trails?maxResults=20&lat=${lat}&lon=${long}&maxDistance=50&sort=distance&key=200692212-0c29a6ccde17f1eeb5873b8087e497d2`, function(data) {
                    console.log(data)
                    $('#trail_info').empty();
                    for(i=0; i<data.trails.length; i++){  
                        $('#trail_info').append("<tr><td>" + data.trails[i].id + `</td><td><a href='trail/${data.trails[i].id}'>` + data.trails[i].name + "</a></td><td>" + data.trails[i].stars + "</td></tr>")                
                    }
                    
                    });

                

                    var geocoder = new google.maps.Geocoder();
                    geocoder.geocode( { latLng: marker.getPosition() }, function ( result, status ) {
                        if ( status == google.maps.GeocoderStatus.OK ) {  
                            address = result[0].formatted_address;
                            addressEl.value = address;
                            latEl.value = lat;
                            longEl.value = long;
            
                        } else {
                            console.log( 'Geocode was not successful for the following reason: ' + status )
                        }
        
                        if( infoWindow) {
                            infoWindow.close();
                        }
        
                        infoWindow = new google.maps.InfoWindow({
                            content: address
                        });
            
                        infoWindow.open( map, marker );
                    } );
                });

            }, function (){
                handleLocationError('No service!', map.center());
            })
        } else {
            handleLocationError('No location available', map.center());
        }
    
        google.maps.event.addListener( searchBox, 'places_changed', function () {
            var places = searchBox.getPlaces(),
                bounds = new google.maps.LatLngBounds(),
                i, place, lat, long;
                address = places[0].formatted_address;
    
            for( i = 0; place = places[i]; i++ ) {
                bounds.extend( place.geometry.location );
                marker.setPosition( place.geometry.location ); 
            }
    
            map.fitBounds( bounds );
            map.setZoom( 15 );
    
            lat = marker.getPosition().lat();
            long = marker.getPosition().lng();
            latEl.value = lat;
            longEl.value = long;
    
        } );

    }

