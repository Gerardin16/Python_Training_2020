$(document).ready(function(){
    // Get value on button click and show alert
    $("#myBtn").click(function(){
        var str = $("#myInput").val();
        alert(str);
    });

     $("#myBtn1").click(function(){
        var str = $("#myInput").val();      
        $("#demo").text(str);
        $("#lbl").html(str);
        $("#myOutput").val(str);
    });
});