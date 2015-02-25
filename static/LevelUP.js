// <script type=text/javascript>
function updateGeo(evt){
  evt.preventDefault();

  $.post("/geographic_demand_skill",
        $('#geo_skill').serialize(), 
        function(result) {
        console.log(result);
        // var sum = "";
        //   for(var i = 0; i < result.length; i++) {
        //       // tup = result[i];
        //       sum += "Job Location: " + result[i][0] + " Latitude : " + result[i][1] + "<br>";
        //   }
        $("#geo_results").html(result); 
        }
    );	
}
$('#geo_skill_button').on('click', updateGeo);



$('a[data-nexttab]').on('click', function () {
    var id = $(this).data('nexttab');
    $('.nav-tabs li:eq(' + id + ') a').tab('show');   
});