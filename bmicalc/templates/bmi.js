{% load static %}
<script>
function convertHeight() {
    alert('convertHeight function accessed');
    var h_unit = document.getElementById("h_unit").value;
    var h_input = document.getElementById("h_input").value;

    switch (h_unit){
    case "inch2cm":
        convert = h_input * 2.54;
        alert(convert);
        document.getElementById("h_input").value=convert;
        break;
    case "cm2inch":
        convert = h_input  /  2.54;
        alert(convert);
        document.getElementById("h_input").value=convert;
    break;
    }
}



function convertWeight() {
    alert('convertWeight function accessed');
    var w_unit = document.getElementById("w_unit").value;
    var w_input = document.getElementById("w_input").value;

    switch (w_unit){
    case "pound2kg":
        convert = w_input / 2.2;
        alert(convert);
        document.getElementById("w_input").value=convert;

        break;
    case "kg2pound":
        convert = w_input  * 2.2;
        alert(convert);
        document.getElementById("w_input").value=convert;
        break;
    }
}


function clearform() {
  document.getElementById("myform").reset();
}

var image_tracker = '1';

 function changeimg(){
     alert('function');
     var image = document.getElementById('imgs');
     if (image_tracker=='1') {
         image.src="{% static '/reg/img/7i.gif' %}";
         image_tracker='2';
    } else {
         image.src="{% static '/reg/img/click.png' %}";
         image_tracker='1';
    }
 }
</script>

