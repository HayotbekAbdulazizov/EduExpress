if (document.getElementById('map')) {
  var googleMap = document.querySelector('#map'),
    googleMapData = googleMap.dataset;

  var mapCenter = googleMapData.center.split(','),
      mapMarker = googleMapData.coordinates.split(',');


  function initialize() {
    var map = new google.maps.Map(
      document.getElementById('map'), {
        center: new google.maps.LatLng(parseFloat(mapCenter[0]), parseFloat(mapCenter[1])),
        zoom: parseInt(googleMapData.zoom),
        scrollwheel: false,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        styles: [{"featureType":"all","elementType":"labels.text.fill","stylers":[{"saturation":36},{"color":"#333333"},{"lightness":40}]},{"featureType":"all","elementType":"labels.text.stroke","stylers":[{"visibility":"on"},{"color":"#ffffff"},{"lightness":16}]},{"featureType":"all","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"administrative","elementType":"geometry.fill","stylers":[{"lightness":20}]},{"featureType":"administrative","elementType":"geometry.stroke","stylers":[{"color":"#fefefe"},{"lightness":17},{"weight":1.2}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#f7f2ed"},{"lightness":20}]},{"featureType":"landscape.natural.landcover","elementType":"geometry.fill","stylers":[{"color":"#000000"}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#f5f5f5"},{"lightness":21}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#dedede"},{"lightness":21}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#ffffff"},{"lightness":17}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#ffffff"},{"lightness":29},{"weight":0.2}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#ffffff"},{"lightness":18}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#ffffff"},{"lightness":16}]},{"featureType":"transit","elementType":"geometry","stylers":[{"color":"#f2f2f2"},{"lightness":19}]},{"featureType":"water","elementType":"geometry","stylers":[{"color":"#cbf2f2"}]}]
      });

    var marker = new google.maps.Marker({
      position: new google.maps.LatLng(parseFloat(mapMarker[0]), parseFloat(mapMarker[1])),
      map: map,
      icon: {
        url: "img/placeholder-filled-point.svg",
        scaledSize: new google.maps.Size(64, 64)
      }
    });
  }

  function loadMap() {
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.setAttribute('defer','');
    script.setAttribute('async','');
    script.src = 'https://maps.googleapis.com/maps/api/js?v=3' +
      '&key=' + googleMapData.key +'&callback=initialize'; //& neededP
    document.body.appendChild(script);
  }

  window.onload = loadMap;
}





window.chartColors = {
  red: 'rgb(255, 99, 132)',
  orange: 'rgb(255, 159, 64)',
  yellow: 'rgb(255, 205, 86)',
  green: 'rgb(75, 192, 192)',
  blue: 'rgb(54, 162, 235)',
  purple: 'rgb(153, 102, 255)',
  grey: 'rgb(201, 203, 207)'
};


window.randomScalingFactor = function() {
  return (Math.random() > 0.5 ? 1.0 : -1.0) * Math.round(Math.random() * 100);
};

var piChart = $("#piChart");
var lineChart = $("#lineChart");

if (piChart.length) {
  var myChart = new Chart(piChart, {
    type: 'pie',
    data: {
      labels: ["Option 1", "Option 2", "Option 3"],
      datasets: [{
        data: [12, 19, 3],
        backgroundColor: [
          'rgba(18, 73, 117, 1)',
          'rgba(23, 199, 193, 1)',
          'rgb(77, 166, 223)'
        ],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      legend: {
        labels: {
          fontColor: '#41617a',
          fontSize: 13
        },
        position: 'bottom'
      }
    }
  });
}


if (lineChart.length) {
  var lineChart = new Chart(lineChart, {
    type: 'line',
    data: {
      labels: ["1", "2", "3", "4", "5"],
      datasets: [{
        label: "Attribute 1",
        backgroundColor: "#124975",
        data: [
          randomScalingFactor(),
          randomScalingFactor(),
          randomScalingFactor(),
          randomScalingFactor(),
          randomScalingFactor()
        ],
        fill: true
      }, {
        label: "Attribute 1",
        backgroundColor: "#4da6df",
        data: [
          randomScalingFactor(),
          randomScalingFactor(),
          randomScalingFactor(),
          randomScalingFactor(),
          randomScalingFactor()
        ],
        fill: true
      }]
    },
    options: {
      legend: {
        position: 'bottom'
      },
      responsive: true,
      tooltips: {
        mode: 'index',
        intersect: false
      },
      hover: {
        mode: 'nearest',
        intersect: true
      },
      scales: {
        xAxes: [{
          display: true,
          scaleLabel: {
            display: false,
            labelString: 'Month'
          }
        }],
        yAxes: [{
          display: true,
          scaleLabel: {
            display: false,
            labelString: 'Value'
          }
        }]
      }
    }
  });
}
(function ($, window, document, undefined) {
	'use strict';

  var elements = {
    $root: $("html, body"),
    $bannerSlider: $(".banner-slider"),
    $testimonialsCarousel: $(".testimonials-carousel"),
    $testimonialsCarouselFull: $(".testimonials-carousel-full"),
    $partnersCarousel: $(".partners-carousel"),
    $aboutUsCarousel: $(".about-us-carousel"),
    $singleCarousel: $('.single-carousel'),
    $casesArea: $('.cases-area'),
    $form: $('#contact-form'),
    $formHome: $('#contact-form-home'),
    $formSubscribe: $('#form-subscribe'),
    $formSubscribeSidebar: $('#form-subscribe-sidebar'),
    $backTop: $('.back-to-top')
  };

  // Mobile Navigation
  // -------------------------
  var navigation = function(navItem) {
    var $menuList = $('.menu'),
      $hamburgerIcon = $('.btn--menu-mobile'),
      $hesChildrenItem = $('.menu_item-has-children');

    $hamburgerIcon.click(function() {
      $menuList.slideToggle();
      $(this).toggleClass('open');
    });

    $hesChildrenItem.click(function() {
      var $subMenu = $(this).find(".sub-menu");
      if ($(window).width() < 768) {
        $(this).toggleClass('active');
        $subMenu.slideToggle();
      }
    });
  };

  navigation($('.menu_list .menu_item'));


  // Banner Slider
  // -------------------------
  if (elements.$bannerSlider) {
    var swiper = new Swiper('.banner-slider', {
      paginationClickable: true,
      nextButton: '.swiper-button-next',
      prevButton: '.swiper-button-prev',
      loop: true,
      effect: 'fade',
      autoplay: 5000,
      onTransitionEnd: function(swiper) {
        toggleSwiperCaptionAnimation(swiper);
        $(window).trigger("resize");
      }
    });
  }


  // toggleSwiperCaptionAnimation
  // @description  toggle swiper animations on active slides
  // ---------------------------------------------------------
  function toggleSwiperCaptionAnimation(swiper) {
    var prevSlide = $(swiper.container),
      nextSlide = $(swiper.slides[swiper.activeIndex]);

    prevSlide
      .find("[data-caption-animate]")
      .each(function() {
        var $this = $(this);
        $this
          .removeClass("animated")
          .removeClass($this.attr("data-caption-animate"))
          .addClass("not-animated");
      });

    nextSlide
      .find("[data-caption-animate]")
      .each(function() {
        var $this = $(this),
          delay = $this.attr("data-caption-delay");

        setTimeout(function() {
          $this
            .removeClass("not-animated")
            .addClass($this.attr("data-caption-animate"))
            .addClass("animated");
        }, delay ? parseInt(delay) : 0);
      });
  }

  // Testimonials Carousels Options
  // -------------------------------
  var carouselsOptions = {
    slidesPerView: 3,
    spaceBetween: 30,
    nextButton: '.btn-next',
    prevButton: '.btn-prev',
    loop: true,
    // autoplay: 4000,
    breakpoints: {
      640: {
        slidesPerView: 1,
        spaceBetween: 30
      },
      920: {
        slidesPerView: 2,
        spaceBetween: 30
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 30
      }
    }
  };


  // Carousel Index
  // -------------------------
  if (elements.$testimonialsCarousel.length) {
    var testimonials = new Swiper(elements.$testimonialsCarousel, carouselsOptions);
  }

  // Carousel Testimonials Full
  // -------------------------
  if (elements.$testimonialsCarouselFull.length) {
    var testimonials = new Swiper(elements.$testimonialsCarouselFull, carouselsOptions);
  }

  // Partners carousel
  // -------------------------
  if (elements.$partnersCarousel.length) {
    var partners = new Swiper(elements.$partnersCarousel, {
      spaceBetween: 30,
      slidesPerView: 'auto',
      loop: true,
      nextButton: '.btn.btn--next',
      prevButton: '.btn.btn--prev',
      autoplay: 6000,
      breakpoints: {
        500: {
          slidesPerView: 1
        },
        640: {
          slidesPerView: 3
        }
      }
    });
  }

  // Partners carousel
  // -------------------------
  if (elements.$singleCarousel.length) {
    var partners = new Swiper(elements.$singleCarousel, {
      slidesPerView: 1,
      loop: true,
      nextButton: '.swiper-button-next',
      prevButton: '.swiper-button-prev',
      autoplay: 6000
    });
  }


  if (elements.$aboutUsCarousel.length) {
    var aboutUs = new Swiper(elements.$aboutUsCarousel, {
      pagination: '.swiper-pagination',
      paginationClickable: true,
      spaceBetween: 30
    });
  }


  // Accordion
  // -------------------------
  (function() {
    $(".accordion_item > a").on("click", function(e){
      e.preventDefault();

      if($(this).hasClass('active')) {
        $(this).removeClass("active");
        $(this).siblings('.accordion_content').slideUp(200);
        $(".accordion_item > a i").removeClass("fi-minus").addClass("fi-plus");
      } else {
        $(".accordion_item > a i").removeClass("fi-minus").addClass("fi-plus");
        $(this).find("i").removeClass("fi-plus").addClass("fi-minus");
        $(".accordion_item > a").removeClass("active");
        $(this).addClass("active");
        $('.accordion_content').slideUp(200);
        $(this).siblings('.accordion_content').slideDown(200);
      }
    });
  })();


  // Masonry View
  // -------------------------
  $(window).load(function() {
    var $container = $('.portfolio');

    setTimeout(function() {
      if ($container.length) {
        $container.masonry({
          itemSelector: '.portfolio_item',
          percentPosition: true
        });
      }
    }, 200);
  });


  // Cases filters. Mixitup init
  // -----------------------------
  if (elements.$casesArea.length) {
    var containerEl = document.querySelector('.cases-area');
    var mixer = mixitup(containerEl);
  }


  // Tabs
  $(document).on('click', '.tabs-nav a', function(e) {
    var $this = $(this).parent('li'),
      $index = $this.index();

    $this.siblings().removeClass('tabs-nav_item--active').end().addClass('tabs-nav_item--active');
    $this.parent().next().children('.tabs-content').stop(true, true).hide().eq($index).stop(true, true).fadeIn(250);
    e.preventDefault();
  });


  // Back To Top
  // -------------------------
  if (elements.$backTop.length) {
    var scrollTrigger = 100, // px
      backToTop = function () {
        var scrollTop = $(window).scrollTop();
        if (scrollTop > scrollTrigger) {
          elements.$backTop.addClass('show');
        } else {
          elements.$backTop.removeClass('show');
        }
      };
    backToTop();
    $(window).on('scroll', function () {
      backToTop();
    });

    elements.$backTop.on('click', function (e) {
      e.preventDefault();
      $('html,body').animate({
        scrollTop: 0
      }, 700);
    });
  }


  // Form jQuery validator
  // -----------------------
  $.validator.setDefaults({
    debug: true,
    success: "valid"
  });


  // form sent message
  $.validator.setDefaults({
    submitHandler: function(form) {
      var sentMessage = 'Thank you for your message. It has been sent';

      $(form).append("<div class='sent-msg'><span>" + sentMessage + "</span></div>");

      setTimeout(function() {
        $('.sent-msg').remove();
      }, 5000);
    }
  });

  var validateRules = {
    contact: {
      rules: {
        "first-name": "required",
        email: {
          required: true,
          email: true
        },
        phone: {
          required: true
        }
      },
      messages: {
        "first-name": "Please enter your first name",
        email: "Please enter a valid email address",
        phone: "Please enter a phone number"
      }
    },
    home: {
      rules: {
        name:  "required",
        phone: "required"
      },
      messages: {
        name: "Please enter your first name",
        phone: "Please enter a phone number"
      }
    },
    subscribe: {
      rules: {
        email: {
          required: true
        }
      },
      messages: {
        email: "Please enter a valid email address"
      }
    }
  };

  // form validator
  elements.$form.validate(validateRules.contact);
  elements.$formHome.validate(validateRules.home);
  elements.$formSubscribe.validate(validateRules.subscribe);
  elements.$formSubscribeSidebar.validate(validateRules.subscribe);

})(jQuery, window, document);