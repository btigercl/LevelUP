//Landing page

// function entryData(evt){
//   evt.preventDefault();
//   var entrySkill= $("select[name='selected_landing_skill']" ).val();
//   console.log("hi")
//   var encodedEntryskill = encodeURIComponent(entrySkill);

//   d3.json("/skill_sets?selected_skill=" + encodedEntryskill function(error, json) {
//     startData = json;
//     visualizeCluster(startData)
//   });
// }
// $("#landing_button").on('click', entryData);


// Skill Set Tab 



var clusterData;

function startCluster(evt){
  evt.preventDefault();
  $("#cluster_results").empty()
  var skillName= $( "select[name='selected_skill']" ).val();
  console.log(skillName)
  var encodedSkill = encodeURIComponent(skillName);

  d3.json( "/skill_angelList_call?selected_skill=" + encodedSkill, function(error, json) {
    clusterData = json;
    visualizeCluster(clusterData);
  });  
}

$('#skill_cluster_button').on('click', startCluster);
// $('#landing_button').on('click', startCluster);
// $('#skill_cluster_button').on('click', emptyClusterdiv);

//Skill Set D3 code 

function visualizeCluster(datapassed){  

  console.log(datapassed);
  var roleList = createRoletaglist(datapassed);
  var nodes = makeNodes(datapassed);
  var linkData = processDataIntoLinks(nodes);
                  

// var links = d3.layout().links(nodes);
// console.log(links);
                 
  var width = 1000,
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
    $("#cluster_results").empty();
      // path.exit().remove();
      // node.exit().remove();
    visualizeCluster(newData);
    });
  }
}

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

function createRoletaglist(dict){
  $("#dynamic_list").empty()
   _.each(dict.roletag_list, function(item, index){
      var front = "<li>";
      var middle = String(item) 
      var back = "</li>";
      var fullListiem = front.concat(middle, back);
      // var fullListiem = front.concat(back);
      $("#dynamic_list").append(fullListiem)
    return
  });
}


//Trends Tab Javascript

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
  $("#trends_results").empty()
  $("#trends_legend").empty()
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
    // update(trendData);
  });  
}

$('#trend_button').on('click', get_graph_data);


function draw_line_graph(multiLinedata) { 
  console.log(multiLinedata);

  var margin = {top: 30, right: 20, bottom: 25, left: 30},
    width = 800 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

  var parseDate = d3.time.format("%Y-%m").parse;

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
    .text("Percent of Stackoverflow Activity (%)");

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

  // if(svg.selectAll(".yAxis"))[0].length < 1){
  //   sv.append("g")
  //     .attr("class", "y axis")
  //     .call(yAxis)
  // } else {
  //   svg.selectAll(".y.axis").transition()duration(1500).call(yAxis)
  // }

  // lines.transition().duration(1500)
  //   .attr("d", line)
  //   .style("stroke", function(){

  //   })

  // lines.enter()
  //   .append("path")
  //   .attr("class", "line")
  //   .attr("d", line)
  //   .style("stroke", function(){
      
  //   });
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

function update(secondData){
    console.log(secondData)
    var parseDate = d3.time.format("%Y-%m").parse;
    var data2 = parseData(secondData);

    data2.forEach(function(d) {
      d.date = parseDate(d.date);
    });

    x.domain(d3.extent(data2, function(d) { return d.date; }));
    y.domain(d3.extent(data2, function(d) { return d.percent; }));

    var svg =d3.select("#trends_results").transition();

    svg.select(".line")
      .duration(750)
      .attr("d", path(data2));
    svg.select(".x.axis")
      .duration(750)
      .call(xAxis);
    svg.select(".y.axis")
      .duration(750)
      .call(yAxis);
}



//Bootstrap Javascript 
$('a[data-nexttab]').on('click', function () {
  var id = $(this).data('nexttab');
    $('.nav-tabs li:eq(' + id + ') a').tab('show');   
});
