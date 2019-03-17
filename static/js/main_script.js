$( document ).ready(function() {
  $( "#forward" ).click(function() {
    $.get("/car/forward", function( data ) {
      console.log("forward", data);
    });
  });
  $( "#left" ).click(function() {
    $.get("/car/left", function( data ) {
      console.log("left", data);
    });
  });
  $( "#right" ).click(function() {
    $.get("/car/right", function( data ) {
      console.log("right", data);
    });
  });
  $( "#backward" ).click(function() {
    $.get("/car/backward", function( data ) {
      console.log("backward", data);
    });
  });
});
