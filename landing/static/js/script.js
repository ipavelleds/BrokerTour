$(document).ready(function(){


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
        callback: {
            loaded: function(){
          $('.slidesjs-pagination').hide(0);
        },
        complete: function(number) {
          $('input[name="tour"]').val($('.slide:eq('+ (number - 1) +')').data('tour'))
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

        setInterval(function(){
            var pmc = $('#user-phone');
            if ( (pmc.val().length != 15) || pmc.val() == '' || (pmc.val().indexOf("_") != -1) ) {
              pmc.addClass('empty-field');
            } else {
                pmc.removeClass('empty-field');
            }

            var sizeEmpty = $form.find('.empty-field').size();

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
                $.ajax({
                    method: "POST",
                    url: $form.attr('action'),
                    data: $form.serialize()
                })
            }
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
                            .show().text('Всё удалось, спасибо за обращение')
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
                dataType: 'text',
                crossDomain: true
            });
            return false
        });

    });

});