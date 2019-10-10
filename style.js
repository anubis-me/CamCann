const instant = new TypeIt('#motto', {
  strings: ["What You Can't,", "CamCann."],
  speed: 90,
  breakLines: false,
  waitUntilVisible: true,
  loop: true
}).go();

$(window).scroll(function(){
  $('nav').toggleClass('scrolled', $(this).scrollTop() > 50);
});

ScrollReveal().reveal('.introduction');
ScrollReveal().reveal('.problems',);
ScrollReveal().reveal('.achievements');
ScrollReveal().reveal('.ourTeam');
ScrollReveal().reveal('.affiliates');

ScrollReveal().reveal('.card', {delay: 300});
