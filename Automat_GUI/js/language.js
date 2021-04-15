language = "DE"
lang_str=0;

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function Get_Lang(region,id,value){


  if (typeof(value) !== 'undefined') {
    if(value == "random"){
      return lang_str[language][region][id][getRandomInt(lang_str[language][region][id].length)]
    } else {
      return lang_str[language][region][id][value];
    }

  } else {
    return lang_str[language][region][id];
  }

}

$( document ).ready(function() {
  $.ajaxSettings.async = false;
   $.get("../lang/lang.json",function (data){
     lang_str=data;
   });



});
