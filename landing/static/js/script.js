var _currentSlideNumber;

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
      $('input[name="tour-id"]').val($('.slide:eq('+ 0 +')').data('tour-id'));
      $('.slidesjs-pagination').hide(0);
      $('#slider').slidesjs({
        width: 700,
        height: 265,
        callback: {
            loaded: function(){
          $('.slidesjs-pagination').hide(0);
        },
        complete: function(number) {
          $('input[name="tour-id"]').val($('.slide:eq('+ (number - 1) +')').data('tour-id'))
        }
        },
        navigation: {
            active: false,
            effect: "fade"
        },
        pagination: {
            effect: "fade"
        },
        effect: {
            fade: {
                speed: 600,
                crossfade: true
            }
        }
     });
        $(".banner").click(function(e){
          e.preventDefault();
          // use data-item value when triggering default pagination link
          $('a[data-slidesjs-item="' + ($(this).attr("data-item") - 1) + '"]').trigger('click');
          $.scrollTo("0", 800);
        });
    });

//    $("#send-order").click(function(){
//        $("#popup").fadeIn(600);
//    });

    $(function(){
        $('#user-phone').each(function(){
            $(this).mask("(999) 999-99-99");
        });

        var form = $('.phone-form'),
        btn = form.find('.button-submit');

        setInterval(function(){
            var pmc = $('#user-phone');
            if ( (pmc.val().length != 15) || pmc.val() == '' ) {
              pmc.addClass('empty-field');
            } else {
                pmc.removeClass('empty-field');
            }

            var sizeEmpty = form.find('.empty-field').size();

            if(sizeEmpty > 0){
            if(btn.hasClass('disabled')){
              return false
            } else {
              btn.addClass('disabled')
            }
            } else {
            btn.removeClass('disabled')
            }

            },200);

            btn.click(function(){
            if($(this).hasClass('disabled')){
                $(".phone-form-error").show();
            } else {
                $(".phone-form-error").hide();
                $("#popup").fadeIn(600);
            }
        });

    });

});