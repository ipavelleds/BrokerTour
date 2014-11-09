$(document).ready(function(){

    (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = "//connect.facebook.net/ru_RU/sdk.js#xfbml=1&version=v2.0";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));


//    $("#popup").hide();
    $("#popup-close").click(function(){
        $("#popup").hide();
    });

    $(function() {
      $('#slider').slidesjs({
        width: 700,
        height: 265,
        navigation: {
            active: false
        },
        pagination: {
            active: false
        },
        effect: {
            slide: {
            // Slide effect settings.
            speed: 1200
            // [number] Speed in milliseconds of the slide animation.
            }
        }
     });
    });

    $("#send-order").click(function(){
        $("#popup").fadeIn(600);
    });

});