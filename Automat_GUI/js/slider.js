var progress=0;
var slideIndex = 0;
var Slider_timer;

function showSlides() {
var i;
var slides = document.getElementsByClassName("Slider-Item");
$(".Slider-Item").fadeOut(200);
slideIndex++;
if (slideIndex > slides.length) {slideIndex = 1}
//$(slides[slideIndex-1]).fadeIn(200);
$(slides[4]).fadeIn(200);

}

function Start_Slideshow(){
if(Slider_timer === "undefined"){
} else {
  progress=0;
  slideIndex=0;
}

showSlides();

Slider_timer = setInterval(function(){
    progress = progress+0.1;
    $("#Slider-prog").width(progress + "%");
    if(progress >= 100){
      progress=0;
      showSlides();
    }
  }, 50);

  $(".Slider-Container").fadeIn(200);
}

function Stop_Slideshow(){
clearInterval(Slider_timer);
$(".Slider-Container").fadeOut(200);

}
