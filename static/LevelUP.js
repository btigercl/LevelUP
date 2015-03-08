//Landing page


// Skill Set Tab Event Listener  
function emptyClusterdiv(evt){
  $('#cluster_results').empty()
}

$('#skill_cluster_button').click(function() {
  $( "#fade_in_cluster_text" ).fadeIn( "slow", function() {
    $("#fade_in_cluster_text" ).html("<p>Find out what other skills frequently show up with in the same joblistings on Angel List Want to know what other skills employers are looking for on AngelList.</p>");
    });
});

var clusterData;

function startCluster(evt){
  evt.preventDefault();
  var skillName= $( "select[name='selected_skill']" ).val();
  console.log(skillName)
  var encodedSkill = encodeURIComponent(skillName);

  d3.json( "/skill_angelList_call?selected_skill=" + skillName, function(error, json) {
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
  var linkData = processDataIntoLinks(nodes);
                  

// var links = d3.layout().links(nodes);
// console.log(links);
                 
  var width = 800,
    height = 700,
    nodesValues = d3.values(nodes);

  //main force function 
  var force = d3.layout.force()
    .nodes(nodes)
    .links(linkData)
    .size([width, height])
    .linkDistance(125)
    .linkStrength(0.1)
    .charge(-300)
    .on("tick", tick)
    .start();

  //canvas
  var svg = d3.select("#cluster_results").append("svg")
    .attr("width", width)
    .attr("height", height);  
       
  var div = d3.select("#cluster_results").append("div")   
    .attr("class", "tooltip")               
    .style("opacity", 0);

  // add the links
  var path = svg.append("svg:g").selectAll("path")
    .data(force.links())
    .enter().append("svg:path")
    .attr("class", "link");
  

                      
  // define the nodes
  var node = svg.selectAll(".node")
    .data(force.nodes())
    .enter().append("g")
    .attr("class", "node")
    .on("click", click)
    .call(force.drag);
    

  
  //color scale                 
  var color = d3.scale.category20c();

  //adds nodes to canvas
  node.append("circle")
    .attr("r", function(d) { return d.count/6})
    .style("fill", function(d) { return color(d.count); });
                      
  // add the text 
  node.append("text")
    .attr("x", 25)
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
  
  function click() {
    if (d3.event.defaultPrevented) return;
    var d = d3.select(this).node().__data__;
    var tagDisplayname = d.name;
    encodedNodeskill = encodeURIComponent(tagDisplayname);
    d3.json( "/skill_angelList_call?selected_skill=" + encodedNodeskill, function(error, json) {
    newData = json;
      path.exit().remove();
      node.exit().remove();
    visualizeCluster(newData);
    });
  }
}

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

      // $('#trend_button').click(function () {
      //   $("trends_results").replaceWith("<div id='trends_results'></div>");
      // });

// Loading trends tab
// $( document ).ready(function() {(

//   d3.json( "/db_call_trend?selected_trend1=" + "css" + "&selected_trend2=" + "javascript" + "&selected_trend3=" + "html", 
//   function(error, json)  {
//   var trendData = json;
//   console.log(trendData)
//   draw_line_graph(trendData)};  
// }


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
    draw_line_graph(trendData);
  });  
}

$('#trend_button').on('click', get_graph_data);


function draw_line_graph(multiLinedata) { 
         

  var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

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
    .x(function(d) {return x(d.date);})
    .y(function(d) {return y(d.percent);
  });

  var svg = d3.select("#trends_results").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  var data1 = parseData(multiLinedata);

  data1.forEach(function(d) {
    d.date = parseDate(d.date);
  });

  x.domain(d3.extent(data1, function(d) { return d.date; }));
  y.domain(d3.extent(data1, function(d) { return d.percent; }));

  var div = d3.select("#trends_results").append("div")   
    .attr("class", "tooltip")               
    .style("opacity", 0);

  var dataNest = d3.nest()
    .key(function(d) {return d.trendName;})
    .entries(data1);

  var color = d3.scale.category20c()

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
      .attr("d", line(d.values))
      .on("mouseover", function() {
      var x0 = x.invert(d3.mouse(this)[0]);
      var bisectDate = d3.bisector(function (d) {
        return d.date;}).left;
                      
  var i = bisectDate(d.values, x0, 1),
    entry0 = d.values[i - 1],
    entry1 = d.values[i],
    y = x0 - entry0.date > entry1.date - x0 ? entry1.percent : entry0.percent;

  div.transition()
    .duration(500)
    .style("opacity", 1);
  div.html(y + "%")
    .style("left", (d3.event.pagex) + "px")
    .style("top", (d3.event.pageY - 28) + "px");
  })
  .on("mouseout", function(){
    div.transition()
      .duration(500)
      .style("opacity", 0);
  })
  
  var legendName = d.key;
  var legendColor = d.color 
  var legendContainer = $('#trends_legend');
  var newLegendText = $('<div class="legend-text">' + legendName + '</div>');
  var newLegendColor = $('<div class="legend-box" style="background-color:'+ legendColor + '"></div>');
  legendContainer.append(newLegendText, newLegendColor); 

  });
}

// Parse out the line graph data
function parseData(xydata){
          var xy = [];
                // parseDate = d3.time.format("%y").parse()
          _.each(xydata.trends, function(item, index){
              xy.push({trendName: item.trendName, date: item.date, percent: item.percent});
              });
          return xy;
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
