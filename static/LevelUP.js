// <script type=text/javascript>
function updateGeo(evt){
  evt.preventDefault();

  $.post("/geographic_demand_skill",
        $('#geo_skill').serialize(), 
        function(result) {
        console.log(result);
        $("#geo_results").html(result); 
        }
    );	
}
$('#geo_skill_button').on('click', updateGeo);

function updateCluster(evt){
  evt.preventDefault();

  $.post("/skill_angelList_call",
        $('#skill_cluster').serialize(), 
        function(result) {
        console.log(result);
        $("#cluster_results").html(result); 
        }
    );	
}
$('#skill_cluster_button').on('click', updateCluster);


$('a[data-nexttab]').on('click', function () {
    var id = $(this).data('nexttab');
    $('.nav-tabs li:eq(' + id + ') a').tab('show');   
});