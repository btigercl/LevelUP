//Geographic Demand Tab Javascript

function startGeo(){
  $.ajax({
  url: "/cookies"})
  .done(function(data, error){
      var jsonSkill = JSON.parse(data);
      var skill = jsonSkill.skill;
      console.log(skill);
      var url = ("/geographic_demand_skill?selected_geo_skill=" + skill);
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


