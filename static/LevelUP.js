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
$('#geo_skill_button').on('click', updateGeo);

function updateCluster(evt){
  evt.preventDefault();

  $.post("/skill_angelList_call",
        $('#skill_dropdown').serialize(), 
        function(results) {
        console.log(results);
        // pass this to d3
        visualizeCluster(results); 
        }
    );	
}
$('#skill_cluster_button').on('click', updateCluster);



function visualizeCluster(link){  
            debugger;
            console.log(links)

            // var mainSkill = links.main_skill
            // var nodes = {};
    var width = 960,
        height = 500;

    var force = d3.layout.force()
        .nodes(d3.values(nodes))
        .links(links)
        .size([width, height])
        .linkDistance(60)
        .charge(-300)
        .on("tick", tick)
        .start();

    var svg = d3.select("#cluster_results").append("svg")
        .attr("width", width)
        .attr("height", height);  




  function update(link) {
      var nodes = flatten(link),
      links = d3.layout.tree().links(nodes);
                // Restart the force layout.
      force
          .nodes(nodes)
          .links(links)
          .start();

      // Update links.
      link = link.data(links, function(d) { return d.target.id; });

      link.exit().remove();

      link.enter().insert("line", ".node")
          .attr("class", "link");

        // Update nodes.
      node = node.data(nodes, function(d) { return d.id; });

      node.exit().remove();

      var nodeEnter = node.enter().append("g")
          .attr("class", "node")
          .on("click", click)
          .call(force.drag);

      nodeEnter.append("circle")
          .attr("r", function(d) { return Math.sqrt(d.size) / 10 || 4.5; });

      nodeEnter.append("text")
          .attr("dy", ".35em")
          .text(function(d) { return d.name; });

      node.select("circle")
          .style("fill", color);
}


          

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
                .attr("r", 5);
                // .style("fill", function(d) { return color(d.source); });
                
            // add the text 
            node.append("text")
                .attr("x", 12)
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

$('#skill_cluster_button').on('click', updateCluster);



$('a[data-nexttab]').on('click', function () {
    var id = $(this).data('nexttab');
    $('.nav-tabs li:eq(' + id + ') a').tab('show');   
});



//code bone yard 
            // nodes[mainSkill] = {source:mainSkill, count: links.total}
            // Compute the distinct nodes from the links.
            
            // $.each()
            // links.forEach(function(link) {
            //     // sourceNode = nodes[link.name] || 
            //     //     (nodes[link.name] = {source: mainSkill, count: link.count});
            //     link.targetNode = nodes[link.name] || 
            //         (nodes[link.name] = {source: mainSkill, count: link.count});
            //     link.value = +link.value;;
            // });


            // console.log(links);
            // console.log(nodes);
