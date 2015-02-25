  <script type=text/javascript>
function updateGeo(evt){
  evt.preventDefault();

  $.post("/geographic_demand_skill",
        $('#geo_skill').serialize() {
        function(result){
        console.log(result):
          // for(var i = 0, i < result.length, i++) {
          //     tup = result[i];
          //     output = "Job Location": tup[0], "Latitude :" tup[1],  
        $("#geo_results").html(result); 
          }
        }

$('#geo_skill_button').on('click', updateGeo);






//   var 
//     // Opera 8.0+, Firefox, Safari
//     ajaxRequest = new XMLHttpRequest();
//   } catch (e){
//     // Internet Explorer Browsers
//     try{
//       ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
//     } catch (e) {
//       try{
//         ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
//       } catch (e){
//         // Something went wrong
//         alert("Your browser broke!");
//         return false;
//       }
//     }
//   }
// }


  
// Create a function that will receive data sent from the server
// ajaxRequest.onreadystatechange = function(){
//   if(ajaxRequest.readyState == 4){
//     document.myForm.time.value = ajaxRequest.responseText;
//   }
// }



// var response = JSON.parse(httpRequest.responseText)


// function updatepage(str){
//     document.getElementById("geo_results").innerHTML = str


//     $(function() {
//       $('a#calculate').bind('click', function() {
//         $.getJSON('/_add_numbers', {
//           a: $('input[name="a"]').val(),
//           b: $('input[name="b"]').val()
//         }, function(data) {
//           $("#result").text(data.result);
//         });
//         return false;
//       });
//     });
//   </script>

      // (function() {
    // var httpRequest;
    // document.getElementById("geo_skill").onclick = function() {
    //  makeRequest('"/geographic_demand_skill"'); };
    //  try{