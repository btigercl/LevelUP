//Skill Set Tab Event Listener  

var clusterData;
function startCluster(evt){
  evt.preventDefault();


  var skill_id= $( "select[name='selected_skill']" ).val();
  console.log(skill_id)

  d3.json( "/skill_angelList_call?selected_skill=" + skill_id, function(error, json) {
      clusterData = json;
      visualizeCluster(data);
    });  
}
$('#skill_cluster_button').on('click', startCluster);

//Skill Set D3 code 

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

//Cluster Function to make a new call when node is clicked
// function update() {
//   var nodes = flatten(root),
//       links = d3.layout.tree().links(nodes);

//   // Restart the force layout.
//   force
//       .nodes(nodes)
//       .links(links)
//       .start();

//   // Update links.
//   link = link.data(links, function(d) { return d.target.id; });

//   link.exit().remove();

//   link.enter().insert("line", ".node")
//       .attr("class", "link");

//   // Update nodes.
//   node = node.data(nodes, function(d) { return d.id; });

//   node.exit().remove();

//   var nodeEnter = node.enter().append("g")
//       .attr("class", "node")
//       .on("click", click)
//       .call(force.drag);

//   nodeEnter.append("circle")
//       .attr("r", function(d) { return Math.sqrt(d.size) / 10 || 4.5; });

//   nodeEnter.append("text")
//       .attr("dy", ".35em")
//       .text(function(d) { return d.name; });

//   node.select("circle")
//       .style("fill", color);
// }

// //  on click.
// function click(d) {
//   if (d3.event.defaultPrevented) return; // ignore drag
//   if (d.children) {
//     d._children = d.children;
//     d.children = null;
//   } else {
//     d.children = d._children;
//     d._children = null;
//   }
//   update();
// }

//Trends Tab Javascript 


//Add lines to Trend graph
// $( document ).ready(function trends_graph() {  
// var margin = {top: 20, right: 20, bottom: 30, left: 50},
//     width = 960 - margin.left - margin.right,
//     height = 500 - margin.top - margin.bottom;

// var parseDate = d3.time.format("%d-%b-%y").parse;

// var x = d3.time.scale()
//     .range([0, width]);

// var y = d3.scale.linear()
//     .range([height, 0]);

// var xAxis = d3.svg.axis()
//     .scale(x)
//     .orient("bottom");

// var yAxis = d3.svg.axis()
//     .scale(y)
//     .orient("left");

// var line = d3.svg.line()
//     .x(function(d) { return x(d.date); })
//     .y(function(d) { return y(d.close); });

// var svg = d3.select("trends_results").append("svg")
//     .attr("width", width + margin.left + margin.right)
//     .attr("height", height + margin.top + margin.bottom)
//   .append("g")
//     .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
// });



// function add_data_to_graph(){
// d3.json("data.tsv", function(error, data) {
//   data.forEach(function(d) {
//     d.date = parseDate(d.date);
//     d.close = +d.close;
//   });

//   x.domain(d3.extent(data, function(d) { return d.date; }));
//   y.domain(d3.extent(data, function(d) { return d.close; }));

//   svg.append("g")
//       .attr("class", "x axis")
//       .attr("transform", "translate(0," + height + ")")
//       .call(xAxis);

//   svg.append("g")
//       .attr("class", "y axis")
//       .call(yAxis)
//     .append("text")
//       .attr("transform", "rotate(-90)")
//       .attr("y", 6)
//       .attr("dy", ".71em")
//       .style("text-anchor", "end")
//       .text("Price ($)");

//   svg.append("path")
//       .datum(data)
//       .attr("class", "line")
//       .attr("d", line);
//     }
// });

// Trend get data on click 
// var trendData;
// function startTrends(evt){
//   evt.preventDefault();

function add_data_to_graph(){
    var trend1= $( "select[name='selected_trend1']" ).val();
    console.log(trend1);
//   var trend2= $( ).val();
//   var trend3= $( ).val();
 
  // d3.json( "/db_call_trend?selected_trend1=" + trend1 + "?selected_trend2" + trend2 + "?selected_trend3" + trend3, function(error, json) {
    d3.json( "/db_call_trend?selected_trend1=" + trend1, function(error, json) {
        trendData = json;
        visualizeCluster(data);
    });  
}
$('#trend_button').on('click', add_data_to_graph);





//Geographic Demand Tab Javascript 
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

//MapBox Javascript



// var iDiv = document.createElement('div');
// iDiv.id = 'geo_results';
// document.getElementsByTagName('geo_table').appendChild(iDiv);
function renderMap(evt){
    var mapContainerParent = geo_results.parentNode;
    mapContainerParent.removeChild(geo_results);

    var newMapContainer = document.createElement('div'); newMapContainer.setAttribute("id", "geo_results")

    mapContainerParent.appendChild(newMapContainer);

    L.mapbox.accessToken = '';
    var map = L.mapbox.map('geo_results', 'btigercl.lb66g6k0')
        .setView([40, -74.50], 9);
}




//Bootstrap Javascript 
$('a[data-nexttab]').on('click', function () {
    var id = $(this).data('nexttab');
    $('.nav-tabs li:eq(' + id + ') a').tab('show');   
});
