$(document).ready(function(){
    loadContent();
        
    });
    
    function loadContent()
    {
        $.ajax({
        url: 'https://api.mocki.io/v1/c5298d00',
        type: 'GET',
        success: function (data) {
            $("#lbl").html(data.name);
        },
        error: function (data) {
          console.log('oops error occured!'); //or whatever     
        
        }
      });
    }