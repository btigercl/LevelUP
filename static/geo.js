//Geographic Demand Tab Javascript

function startGeo(){
  $.ajax({
  url: "/cookies"})
  .done(function(data, error){
      var jsonSkill = JSON.parse(data);
      var skill = jsonSkill.skill;
      console.log(skill);
      encodedSkill =  encodeURIComponent(skill)
      $("#map_header").append("<h2>geographic demand for " + skill + "</h2>");
      var url = ("/geographic_demand_skill?selected_geo_skill=" + encodedSkill);
      $.get(url, function(result) {
        var geoResults= result;
        console.log(geoResults);
        addToOverlay(geoResults);
    });
  });
}
 
function updateGeo(evt){
  evt.preventDefault();
  clearOverlays();

  var geoSkill = $( "select[name='selected_geo_skill']" ).val();
  $("#map_header").empty()
  $("#map_header").append("<h2>geographic demand for " + geoSkill + "</h2>");
  var encodedGeoskill = encodeURIComponent(geoSkill);
  var url = "/geographic_demand_skill?selected_geo_skill=" + encodedGeoskill
  // map.data.loadGeoJson(url);
  $.get(url, function(result) {
      var geoResults= result;
      console.log(geoResults);
    addToOverlay(geoResults);
  });  

}

$('#geo_skill_button').on('click', updateGeo);


