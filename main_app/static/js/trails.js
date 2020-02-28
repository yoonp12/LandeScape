
$(document).ready(function() {
    
    // $('#current_condition').click(function() {
        var lat = $('#lat').val()
        var lon = $('#lon').val()
        console.log(lat,lon)
        var url = `http://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=f19a7565420055738c1e7e0b12fd55e8`
        
        $.get(url, function(data) { 
            console.log(data);

            function degToCompass(num) { 
                x=0;
                while( num < 0 ) num += 360 ;
                while( num >= 360 ) num -= 360 ; 
                val= Math.round( (num -11.25 ) / 22.5 ) ;
                arr=["N","NNE","NE","ENE","E","ESE", "SE", 
                      "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"] ;
                x=arr[ Math.abs(val) ] ;
            }
            num = data.wind.speed;
            degToCompass(num);

            $('.current_sky').html("<h5> Description: <h2>" + data.weather[0].description +" </h2></h5>")
            $('.current_temp').html("<h5> Temperature: <h2>" +
            Math.floor((((data.main.temp - 273) * (9/5)) + 32))
            +" ℉</h2></h5>")
            $('.current_humidity').html("<h5> Humidity: <h2>" + data.main.humidity + "%</h2> </h5>")
            $('.current_wind').html("<h5> Wind: <h2>"+ x + " " + data.wind.speed +" mph</h2></h5>")
            

        
        }, 'json');

    

        
});
