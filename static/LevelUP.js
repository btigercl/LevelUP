//Skill Set Tab Event Listener  
function emptyClusterdiv(evt){
  $('#cluster_results').empty()
}

$('#skill_cluster_button').click(function() {
  $( "#fade_in_cluster_text" ).fadeIn( "slow", function() {
    $("#fade_in_cluster_text" ).html("<p>Find out what other skills frequently show up with in the same joblistings on Angel List Want to know what other skills employers are looking for on AngelList.</p>");
  });
});

var clusterData;
$()
function startCluster(evt){
  evt.preventDefault();


  var skill_id= $( "select[name='selected_skill']" ).val();
  console.log(skill_id)

  d3.json( "/skill_angelList_call?selected_skill=" + skill_id, function(error, json) {
      clusterData = json;
      visualizeCluster(clusterData);
    });  
}
$('#skill_cluster_button').on('click', startCluster);
$('#skill_cluster_button').on('click', emptyClusterdiv);

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
 
            var div = d3.select("#cluster_results").append("div")   
                .attr("class", "tooltip")               
                .style("opacity", 0);

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
            
            var color = d3.scale.category20c();

            node.append("circle")
                .attr("r", function(d) { return d.count/6})
                .on("mouseover", mouseover)
                .on("mouseout", mouseout)
                .style("fill", function(d) { return color(d.count); });
                
            // add the text 
            node.append("text")
                .attr("x", 25)
                .attr("dy", ".35em")    
                .text(function(d) { return d.name; });

            function mouseover() {
              // _.each(fullData, function(d, index) {

                div.transition()
                    .duration(500)
                    .style("opacity", 1)
                div. html(function (d) { return d.count; })
                    .style("left", (d3.event.pagex) + "px")
                    .style("top", (d3.event.pageY - 28) + "px");
                // });
              }

            function mousemove() {
                div
                  .text(d3.event.pageX + ", " + d3.event.pageY)
                  .style("left", (d3.event.pageX - 34) + "px")
                  .style("top", (d3.event.pageY - 12) + "px");
              }

            function mouseout() {
                div.transition()
                  .duration(500)
                  .style("opacity", 0);
            }

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
// 
//Trends Tab Javascript
$('#trend_button').click(function() {
  $( "#trend_write_up" ).fadeOut( "slow", function() {
    $('#trend_write_up').empty()
  });
});

$('#trend_button').click(function() {
  $( "#fade_in_trend_text" ).fadeIn( "slow", function() {
    $("#fade_in_trend_text" ).html("<p>We can learn about a skill's popularity today, but what about a skills popularity over time? Check out how many people are asking about a skill on Stack Overflow since 2008 to today.</p>");
  });
});


// Parse out the line graph data 

function parseData(xydata){
    var xy = [];
          // parseDate = d3.time.format("%y").parse()
    _.each(xydata.trends, function(item, index){
        xy.push({trendName: item.trendName, date: item.date, percent: item.percent});
        });
    return xy;
}

//trend: xydata.trend


function get_graph_data(evt){
    evt.preventDefault();


        var trend1= $( "select[name='selected_trend1']" ).val();
        var trend2= $( "select[name='selected_trend2']" ).val();
        var trend3= $( "select[name='selected_trend3']" ).val();
        var encoded1 = encodeURIComponent(trend1);
        var encoded2 = encodeURIComponent(trend2);
        var encoded3 = encodeURIComponent(trend3);

      d3.json( "/db_call_trend?selected_trend1=" + encoded1 + "&selected_trend2=" + encoded2 + "&selected_trend3=" + encoded3, 
      function(error, json)  {
        var trendData = json;
        console.log(trendData)
        multiLinegraph(trendData);
    });  
}

$('#trend_button').on('click', get_graph_data);

function multiLinegraph(multiLinedata) { 
   

    var margin = {top: 20, right: 20, bottom: 30, left: 50},
      width = 960 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom;

    var bluescale4 = ["#8BA9D0", "#6A90C1", "#066CA9", "#004B8C"];
    var color = d3.scale.ordinal().range(bluescale4);

    var parseDate = d3.time.format("%Y").parse;

    var x = d3.time.scale()
        .range([0, width]);

    var y = d3.scale.linear()
        .range([height, 0]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left");

    var line = d3.svg.line()
        .interpolate("basis")
        .x(
          function(d) {
           return x(d.date);
            })
        .y(function(d) {
         return y(d.percent);
          });

    var svg = d3.select("#trends_results").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
        
        // .on("mousemove", mousemove)

    // var data1 = parseData(multiLinedata.trendData1);
    // var data2 = parseData(multiLinedata.trendData2);
    // var data3 = parseData(multiLinedata.trendData3);
    var data1 = parseData(multiLinedata);
    console.log(data1);

    data1.forEach(function(d) {
        d.date = parseDate(d.date);
    });

    // data2.forEach(function(d) {
    //     d.date = parseDate(d.date);
    // });

    // data3.forEach(function(d) {
    //     d.date = parseDate(d.date);
    // });
    // var fullData = data1.concat(data2).concat(data3);

      x.domain(d3.extent(data1, function(d) { return d.date; }));
      y.domain(d3.extent(data1, function(d) { return d.percent; }));

    var div = d3.select("#trends_results").append("div")   
      .attr("class", "tooltip")               
      .style("opacity", 0);

    var dataNest = d3.nest()
        .key(function(d) {return d.trendName;})
        .entries(data1);

    var color = d3.scale.category10()

      svg.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(xAxis);

      svg.append("g")
          .attr("class", "y axis")
          .call(yAxis)
        

        .append("text")
          .attr("transform", "rotate(-90)")
          .attr("y", 6)
          .attr("dy", ".71em")
          .style("text-anchor", "end")
          .text("Percent (%)");

      dataNest.forEach(function(d) {
            svg.append("path")
              .attr("class", "line")
              .style("stroke", function() { // Add dynamically
                  return d.color = color(d.key); })
              .attr("d", line(d.values));
            var legendName = d.key;
            var legendColor = d.color 
            var legendContainer = $('#trends_legend');
            var newLegendText = $('<div class="legend-text">' + legendName + '</div>');
            var newLegendColor = $('<div class="legend-box" style="background-color:'+ legendColor + '"></div>');
            legendContainer.append(newLegendText, newLegendColor);            
       //});
      });

      function mouseover() {
          div.transition()
              .duration(500)
              .style("opacity", 1)
          div. html(d.key + "<br/>" + d.date + "<br/>" + d.percent)
              .style("left", (d3.event.pagex) + "px")
              .style("top", (d3.event.pageY - 28) + "px");
        }

      function mousemove() {
          div
            .text(d3.event.pageX + ", " + d3.event.pageY)
            .style("left", (d3.event.pageX - 34) + "px")
            .style("top", (d3.event.pageY - 12) + "px");
        }

      function mouseout() {
          div.transition()
            .duration(500)
            .style("opacity", 0);
  }
}


//Geo tab javascript
// function emptyGeodiv(evt){
//   $('#geo_results').empty()
// }
// //Geographic Demand Tab Javascript 
function updateGeo(evt){
  evt.preventDefault();
  var skill_id = $( "select[name='selected_geo_skill']" ).val();
  console.log(skill_id)
  var url = "/geographic_demand_skill?selected_geo_skill=" + skill_id
  $.get(url, function(result) {
     var geoResults= result;
     console.log(geoResults);
     geoMap(geoResults);
   });  
}

$('#geo_skill_button').on('click', updateGeo);
// $('#geo_skill_button').on('click', emptyGeodiv);



// MapBox Javascript
function geoMap(geoResults){
    L.mapbox.accessToken = 'pk.eyJ1IjoiYnRpZ2VyY2wiLCJhIjoiTnd3OWp5OCJ9.bSkS-vF6k8g_jeV25fC7sw';
    var map = L.mapbox.map('mapdiv', 'btigercl.lb66g6k0')
        .setView([38, -95], 4);

    var myLayer = L.mapbox.featureLayer().addTo(map);

    myLayer.setGeoJSON(geoResults);
}


//Bootstrap Javascript 
$('a[data-nexttab]').on('click', function () {
    var id = $(this).data('nexttab');
    $('.nav-tabs li:eq(' + id + ') a').tab('show');   
});
