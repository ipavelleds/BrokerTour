$(document).ready(function(){
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
      }
     });
    });
});