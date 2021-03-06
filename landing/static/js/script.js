$(document).ready(function(){

    var firstSlide = 1;
    $(function(){
            var hash = location.hash;
            if(hash){
                var reg  = new RegExp("[0-9]+$");
                firstSlide = $(".slide").index($("[data-tour=" + parseInt(reg.exec(hash)) + "]")) + 1;
            }
        });

    (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = "//connect.facebook.net/ru_RU/sdk.js#xfbml=1&version=v2.0";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));


    $("#popup-close").click(function(){
        $("#popup").hide();
    });


    $(function() {
      $('input[name="tour"]').val($('.slide:eq('+ 0 +')').data('tour'));
      $('.slidesjs-pagination').hide(0);
      $('#slider').slidesjs({
        width: 700,
        height: 265,
        start: firstSlide,
        callback: {
          loaded: function(){
          $('.slidesjs-pagination').hide(0);
        },
        complete: function(number) {
            var $currentSlide = $('.slide:eq(' + (number-1) + ')'),
                tourName = $currentSlide.find('.description .name p').text(),
                tourId = $currentSlide.attr("data-tour");
            $('input[name="tour"]').val($currentSlide.data('tour'));
            history.pushState(null, "BrokerTour. " + tourName, "#tour/" +  tourId);
            dataLayer.push({
                event:'VirtualPageView',
                'virtualPageURL': '/tour/' + tourId,
                'virtualPageTitle' : tourName
            });
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
          $('a[data-slidesjs-item="' + $(this).attr("data-item") + '"]').trigger('click');
          $.scrollTo("0", 800);
        });
    });

    $(function(){
        $('#user-phone').each(function(){
            $(this).inputmask("(999) 999-99-99");
        });

        var $form = $('.phone-form'),
        btn = $form.find('.button-select-tour');


        btn.click(function(){
            $("#popup").fadeIn(600);
            $.ajax({
                method: "POST",
                url: $form.attr('action'),
                data: $form.serialize(),
                success: function(){
                    dataLayer.push({'event': 'phoneSubmit'});
                }
            })
        });

        $form.submit(function(e){
            e.preventDefault();
            var $this = $(this);
            $this.find('.info-error').remove();
            $.ajax({
                method: "POST",
                url: $this.attr('action'),
                data: $this.serialize(),
                success: function(data){
                    if (typeof data === "string") data = JSON.parse(data);
                    if(data.success){
                        $this.find('.info')
                            .show().text('Всё удалось, спасибо за обращение');
                        dataLayer.push({'event': 'formSubmit'});
                    }else{
                        var _ref, error, fieldError, errors = data.form;
                        for (fieldError in errors) {
                            if (!errors.hasOwnProperty(fieldError)) continue;
                            _ref = errors[fieldError];
                            for (var _i = 0, _len = _ref.length; _i < _len; _i++) {
                                error = _ref[_i];
                                $this.find("[name='" + fieldError + "']").after("<p class='info-error'>" + error + "</p>");
                            }
                        }

                        $this.find('.info')
                            .show().text("Ваши данные, к сожалению, не удалось сохранить. Напишите, пожалуйста, на help@kredit.online.")
                    }
                },
                fail:function(data){
                    $this.find('.info')
                        .show().text("Ваши данные, к сожалению, не удалось сохранить. Напишите, пожалуйста, на help@kredit.online.")
                },
                crossDomain: true
            });
            return false
        });

    });
});