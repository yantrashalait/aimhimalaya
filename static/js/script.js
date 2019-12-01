

$(document).ready(function() {
  $('select').niceSelect();
});

$('.banner-slide').owlCarousel({
    loop: true,
    margin: 0,
    nav: true,
    autoplay:false,
    dots: false,
    autoplayTimeout: 5000,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
})

$('.spet-car').owlCarousel({
    loop: false,
    margin: 0,
    nav: true,
    autoplay:false,
    dots: false,
    responsive: {
        0: {
            items: 2
        },
        600: {
            items: 3
        },
        1000: {
            items: 5
        }
    }
})

$('.b-offer').owlCarousel({
    loop: true,
    margin: 30,
    nav: true,
    autoplay:false,
    dots: false,
    autoplayTimeout: 5000,
    responsive: {
        0: {
            items: 2,
            margin: 10,
        },
        600: {
            items: 2,
            margin: 20,
        },
        1000: {
            items: 3
        }
    }
})

$('.a-offer').owlCarousel({
    loop: true,
    margin: 30,
    nav: true,
    autoplay:false,
    dots: false,
    autoplayTimeout: 6000,
    responsive: {
        0: {
            items: 1,
            margin: 10,
        },
        600: {
            items: 2,
            margin: 20,
        },
        1000: {
            items: 3
        }
    }
})

$('.spec-tabcon').owlCarousel({
    loop: true,
    margin: 30,
    nav: true,
    autoplay:false,
    dots: false,
    autoplayTimeout: 6000,
    responsive: {
        0: {
            items: 2,
            margin: 10,
        },
        600: {
            items: 3,
            margin: 20,
        },
        1000: {
            items: 4
        }
    }
})

$('.p-offer').owlCarousel({
    loop: true,
    margin: 0,
    nav: true,
    autoplay:false,
    dots: false,
    autoplayTimeout: 6000,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
})


$('.frm-galle').owlCarousel({
   loop:true,
   dots:false,
   autoplayTimeout: 6000,
   nav:true,
   responsiveClass: false,
   responsive: {
    0: {
      items: 2,
      nav: false
    },
    600: {
      items: 3,
    },
    1000: {
      items: 4,
      loop: true,
      
    }
  }
});


$('.client-rev').owlCarousel({
    loop: true,
    margin: 20,
    nav: true,
    autoplay:false,
    dots: false,
    autoplayTimeout: 3000,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
})





$(document).ready(function(){
  $('ul li a').click(function(){
    $('li a').removeClass("active");
    $(this).addClass("active");
});
});


  $('.clk-open').click(function(){
    $('.mb-mnu').toggleClass("mb-nav-show");
  })



$(document).ready(function(){
  $('.spet-car .item').click(function(){
    $('.spet-car .item').removeClass("active");
    $(this).addClass("active");
});
});



var tag = document.createElement('script');

  tag.src = "https://www.youtube.com/iframe_api";
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

  var player;
  function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
      height: '350',
      width: '680',
      videoId: '_ojeQRNOOt8',
      events: {
        'onStateChange': onPlayerStateChange
      }
    });
  }

  function onPlayerReady(event) {
    event.target.playVideo();
  }


  var done = false;
  function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.PLAYING && !done) {
      //setTimeout(stopVideo, 6000);
      done = true;
    }
  }
  function stopVideo() {
    player.stopVideo();
  }



$(document).ready(function() {
    var $tabs = $('#horizontalTab');
    $tabs.responsiveTabs({
        rotate: false,
        startCollapsed: 'accordion',
        collapsible: 'accordion',
        setHash: true,
        click: function(e, tab) {
            $('.info').html('Tab <strong>' + tab.id + '</strong> clicked!');
        },
        activate: function(e, tab) {
            $('.info').html('Tab <strong>' + tab.id + '</strong> activated!');
        },
        activateState: function(e, state) {
            //console.log(state);
            $('.info').html('Switched from <strong>' + state.oldState + '</strong> state to <strong>' + state.newState + '</strong> state!');
        }
    });

    $('#start-rotation').on('click', function() {
        $tabs.responsiveTabs('startRotation', 1000);
    });
    $('#stop-rotation').on('click', function() {
        $tabs.responsiveTabs('stopRotation');
    });
    $('#start-rotation').on('click', function() {
        $tabs.responsiveTabs('active');
    });
    $('#enable-tab').on('click', function() {
        $tabs.responsiveTabs('enable', 3);
    });
    $('#disable-tab').on('click', function() {
        $tabs.responsiveTabs('disable', 3);
    });
    $('.select-tab').on('click', function() {
        $tabs.responsiveTabs('activate', $(this).val());
    });

});



 $('.slider-for').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  fade: true,
  asNavFor: '.slider-nav'
});
$('.slider-nav').slick({
  slidesToShow: 4,
  slidesToScroll: 1,
  asNavFor: '.slider-for',
  dots: false,
  // arrows: true,
  centerMode: true,
  focusOnSelect: true,
  vertical: true,
  responsive: [
    
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]

});
           


// the below codes are available in detail.html
// $(function() {
//     var top = $("#sidebar").offset();
//     console.log(top);
//     var top = $('#sidebar').offset().top - parseFloat($('#sidebar').css('marginTop').replace(/auto/, 0));
//     var footTop = $('#footer').offset().top - parseFloat($('#footer').css('marginTop').replace(/auto/, 0));

//     var maxY = footTop - $('#sidebar').outerHeight();

//     $(window).scroll(function(evt) {
//         var y = $(this).scrollTop();
//         if (y > top) {
            
//             if (y < maxY) {
//                 $('#sidebar').addClass('fixed').removeAttr('style');
//             } else {
                
//                 $('#sidebar').removeClass('fixed').css({
//                     position: 'absolute',
//                     top: (maxY - top) + 'px'
//                 });
//             }
//         } else {
//             $('#sidebar').removeClass('fixed');
//         }
//     });
// });