$(window).scroll(function() {    
    var scroll = $(window).scrollTop();

    if (scroll >= 200) {
        $(".theame-header").addClass("sticky-header");
    } else {
        $(".theame-header").removeClass("sticky-header");
    }
});

// client-slider-end
  
$(document).ready(function(){
    $('.counter').each(function(){
        $(this).prop('Counter',0).animate({
            Counter: $(this).text()
        },{
            duration: 3500,
            easing: 'swing',
            step: function (now){
                $(this).text(Math.ceil(now));
            }
        });
    });
});

// counter-js-end

// agent-slider-start
$('#agent-slider').owlCarousel({
    margin: 0,
    center: true,
    autoplay:true,
    loop: true,
    dots: false,
    nav: false,
    dots: false,
    responsive: {
    0: {
       items: 1
    },
    767: {
       items: 1,
    },
    768: {
       items: 3,
    },
    1000: {
       items: 3,
    }
    }
});
// agent-slider-end

// testimonial-slider-start
$('#testimonial-slider').owlCarousel({
    margin: 10,
    autoplay:true,
    loop: true,
    nav: false,
    dots: false,
    dots: false,
    responsive: {
    0: {
       items: 1
    },
    767: {
       items: 1,
    },
    991: {
       items: 2,
    },
    1000: {
       items: 3,
    }
    }
});
// testimonial-slider-end

// partner-slider-start

$('#partner-slider').owlCarousel({
    margin: 10,
    autoplay:true,
    loop: true,
    dots: false,
    nav: false,
    responsive: {
    0: {
       items: 1
    },
    600: {
       items: 2,
    },
    768: {
       items: 3,
    },
    1000: {
       items: 4,
    }
    }
});
// partner-slider-end

// testimonial-slider-start
$('#location-slider').owlCarousel({
    margin: 10,
    center: true,
    autoplay:false,
    loop: true,
    dots: false,
    nav: false,
    responsive: {
    0: {
       items: 1
    },
    767: {
       items: 1,
    },
    768: {
       items: 3,
    },
    1000: {
       items: 3,
    }
    }
});
// testimonial-slider-end


// project-slider-start

$('#project-slider').owlCarousel({
    autoplay:false,
    loop:true,
    margin:10,
    dots:true,
    nav:false,
    navText: ['<span class="fas fa-arrow-alt-circle-left"></span>','<span class="fas fa-arrow-alt-circle-right"></span>'],
    items:1
    });
// project-slider-end

// gallery-slider-start

$('#gallery-slider').owlCarousel({
    autoplay:false,
    loop:true,
    margin:0,
    dots:false,
    nav:true,
    navText: ['<span class="far fa-chevron-left owl-arrow"></span>','<span class="far fa-chevron-right owl-arrow"></span>'],
    items:1
    });
// gallery-slider-end
