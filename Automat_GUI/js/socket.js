$.getScript("../js/slider.js", function() {
});

$.getScript("../js/sprintf.min.js", function() {
});

$.getScript("../js/language.js", function() {
});


function Set_Title(title,number=0){
    if(number == 0){
      bannertitle.innerHTML = Get_Lang("title",title);
    } else {
      bannertitle.innerHTML = "Test";
    }

}


function Button_Controll(key1 = 0,key2 = 0,key3 = 0){

  var footer = $(".Footer-Bar").empty();

  if(key1 != 0){
    Create_Div_Element("button button_left",Get_Lang("button",key1),footer);
  } else {
    Create_Div_Element("button","",footer);
  }

  if(key2 != 0){
    Create_Div_Element("button button_middle",Get_Lang("button",key2),footer);
  } else {
    Create_Div_Element("button","",footer);
  }

  if(key3 != 0){
    Create_Div_Element("button button_right",Get_Lang("button",key3),footer);
  } else {
    Create_Div_Element("button","",footer);
  }


}

function Create_new_Container(container_class){
  $(".Content-Center").empty();
  var container = Create_Div_Element(container_class,"", $(".Content-Center"));
  return container;
}

function Create_new_Overlay(container_class){
  $(".overlay").empty();
  var container = Create_Div_Element(container_class,"", $(".overlay"));
  return container;
}


function Create_Div_Element(element_class,text=0,parent_class = 0,id = 0){
  var element = document.createElement("div");
  element.setAttribute("class", element_class);
  if(id != 0){
    element.setAttribute("id", id);
  }
  element.innerHTML = text;

  if(parent_class != 0){
    parent_class.append(element);
  }

  return element;
}


function Create_Table_Element(element_class,parent_class = 0,id = 0){
  var element = document.createElement("table");
  element.setAttribute("class", element_class);
  if(id != 0){
    element.setAttribute("id", id);
  }

  if(parent_class != 0){
    parent_class.append(element);
  }

  return element;
}

function Table_Add_2_Entrys(element_class,Entry1,Entry2,parent_class){
  var row = document.createElement("tr");

  var entry1_obj = document.createElement("td");
  entry1_obj.setAttribute("class", element_class);
  entry1_obj.innerHTML = Entry1;

  var entry2_obj = document.createElement("td");
  entry2_obj.setAttribute("class", element_class);
  entry2_obj.innerHTML = Entry2;

  parent_class.append(row);

  row.append(entry1_obj);
  row.append(entry2_obj);
}


function Add_Picture_Element(element_class,source_class,source=0,parent_class){
  var picture = document.createElement("picture");
  picture.setAttribute("class", element_class);

  if(source != 0){
    var image = document.createElement("img");
    image.setAttribute("src", source);
    image.setAttribute("class", source_class);

  }
  parent_class.append(picture);

  picture.append(image);
}


function Time_for_Array(time){
  switch (time){
    case "today":
        return 0;
    break;

    case "week":
        return 1;
    break;

    case "month":
        return 2;
    break;

    case "year":
        return 3;
    break;

    case "total":
        return 4;
    break;

  }

}




$( document ).ready(function() {
    var websocket = new WebSocket("ws://127.0.0.1:6789/");


websocket.onmessage = function (event) {
    data = JSON.parse(event.data);

    $(".Content-Center").empty();    Button_Controll(data.display.key1,data.display.key2,data.display.key3);

    temperature.innerHTML = data.display.temperature;

    switch(data.display.screen){

      case "startup":
        var container = Create_new_Container("Startup");
        Create_Div_Element("Header",Get_Lang("startup","start"),container);
        Create_Div_Element("CText",Get_Lang("startup","wait"),container);
        Button_Controll("","","");
        Set_Title("startup");
      break;




      case "slider":
        Create_new_Container("Slider-Container");
        $(".Slider-Container").empty();

        var item = Create_Div_Element("Slider-progress","", $(".Content-Center"));
        Create_Div_Element("Slider-progress-status","",item,"Slider-progress-status");

        for (var i = 0; i < data.display.slider.content.length; i++){
          var item = Create_Div_Element("Slider-Item","", $(".Slider-Container"));
          var container = Create_Div_Element("Slider-Item-Container","", item);

          switch(data.display.slider.content[i].id){
            case "about":
              Create_Div_Element("Header",Get_Lang("slider","about-header"),container);
              for (var t=0;t<Get_Lang("slider","about").length;t++){
                Create_Div_Element("NText",Get_Lang("slider","about",t),container);
              }
            break;

            case "telegramm":
              Create_Div_Element("Header",Get_Lang("slider","telegramm-header"),container);
              Create_Div_Element("NText",Get_Lang("slider","telegramm",0),container);
              Create_Div_Element("NText",sprintf(Get_Lang("slider","telegramm",1),data.display.slider.content[i].username),container);
              Create_Div_Element("NText",Get_Lang("slider","telegramm",2),container);
            break;


            case "winner":
              Create_Div_Element("Header",Get_Lang("slider","winner",Time_for_Array(data.display.slider.content[i].time)),container);


              Add_Picture_Element("Profil-Picture","Profil-Picture-Source","/pic/users/" + data.display.slider.content[i].picture,container);

              Create_Div_Element("CText", sprintf(Get_Lang("slider","winner-text"),data.display.slider.content[i].username, data.display.slider.content[i].number),container);
            break;


            case "top5-table":
            Create_Div_Element("Header",Get_Lang("slider","table-text",Time_for_Array(data.display.slider.content[i].time)),container);

            var table = Create_Table_Element("top5_table",container);

            Table_Add_2_Entrys("top5_table-header",Get_Lang("slider","table-name"),Get_Lang("slider","table-number"),table);
            for (var t = 0; t < data.display.slider.content[i].table.length; t++){
              Table_Add_2_Entrys("top5_table-entry",data.display.slider.content[i].table[t].name,data.display.slider.content[i].table[t].number,table);
            }

            break;

            case "total":
              Create_Div_Element("Header",Get_Lang("slider","total-header"),container);
              Create_Div_Element("CText_Big",data.display.slider.content[i].number,container);
            break;



          }
        }

        Start_Slideshow();
      break;
    }
};

websocket.onerror = function(event) {
  //var container = Create_new_Container("Error");
  //Create_Div_Element("Header",Get_Lang("error","error-header"),container);
  //Create_Div_Element("CText",Get_Lang("error","reason_no_connection"),container);
  //Button_Controll("","","");
  //Set_Title("error");

};


});
