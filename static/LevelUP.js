// <script type=text/javascript>
function updateGeo(evt){
  evt.preventDefault();

  $.post("/geographic_demand_skill",
        $('#geo_skill_button').serialize(), 
        function(result) {
        console.log(result);
        $("#geo_results").html(result); 
        }
    );	
}

var data;
function updateCluster(evt){
  evt.preventDefault();


  var skill_id= $( "select[name='selected_skill']" ).val();
  console.log(skill_id)

  d3.json( "/skill_angelList_call?selected_skill=" + skill_id, function(error, json) {
      data = json;
      visualizeCluster(data);
    });  
}
$('#skill_cluster_button').on('click', updateCluster);


function makeNodes(data){
      var nodes = [{name: data.name, weight: data.children.length}];
      _.each(data.children, function(item, index){
        nodes.push({name: item.name, count: item.count, weight: 1});
      });
      return nodes;

}

function processDataIntoLinks(nodes){
    var result = [];
    for (var index = 0; index < _.size(nodes); index++){
        result.push({ source: 0, target: index });
    }
    return result;
}

function visualizeCluster(datapassed){  



    var nodes = makeNodes(datapassed);
    var link = processDataIntoLinks(nodes);
            

            // var links = d3.layout().links(nodes);
            // console.log(links);
           
            var width = 800,
                height = 700,
                nodesValues = d3.values(nodes);

            var force = d3.layout.force()
                .nodes(nodes)
                .links(link)
                .size([width, height])
                .linkDistance(125)
                .linkStrength(0.1)
                .charge(-300)
                .on("tick", tick)
                .start();

            var svg = d3.select("#cluster_results").append("svg")
                .attr("width", width)
                .attr("height", height);  
 


            // add the links and the arrows
            var path = svg.append("svg:g").selectAll("path")
                .data(force.links())
                .enter().append("svg:path")
                .attr("class", "link");
                
            // define the nodes
            var node = svg.selectAll(".node")
                .data(force.nodes())
                .enter().append("g")
                .attr("class", "node")
                .call(force.drag);
            
            var color = d3.scale.category20();

            node.append("circle")
                .attr("r", function(d) { return d.count/6});;
                // .style("fill", function(d) { return color(d.source); });
                
            // add the text 
            node.append("text")
                .attr("x", 35)
                .attr("dy", ".35em")
                .text(function(d) { return d.name; });

            function tick() {
                path.attr("d", function(d) {
                    var dx = d.target.x - d.source.x,
                        dy = d.target.y - d.source.y,
                        dr = Math.sqrt(dx * dx + dy * dy);
                    return "M" + 
                        d.source.x + "," + 
                        d.source.y + "A" + 
                        dr + "," + dr + " 0 0,1 " + 
                        d.target.x + "," + 
                        d.target.y;
                });

                node
                    .attr("transform", function(d) { 
                    return "translate(" + d.x + "," + d.y + ")"; });
            }
}




$('a[data-nexttab]').on('click', function () {
    var id = $(this).data('nexttab');
    $('.nav-tabs li:eq(' + id + ') a').tab('show');   
});
