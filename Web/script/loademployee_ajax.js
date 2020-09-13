$(document).ready(function(){
loadContent();
    
});

function loadContent()
{
    $.ajax({
    url: '../data/employee.json',
    type: 'GET',
    success: function (data) {
        $("#lbl").html(data.name + "  " + data.age  + "  " + data.car);
    },
    error: function (data) {
      console.log('oops error occured!'); //or whatever     
    
    }
  });
}