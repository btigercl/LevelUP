//Trends Tab Javascript

// Loading trends tab
function startTrends(){
  $.ajax({
    url: "/cookies"})
    .done(function(data, error){
      var jsonSkill = JSON.parse(data);
      var skill = jsonSkill.skill;
      console.log(skill);
      encodedSkill =  encodeURIComponent(skill)
      d3.json( "/db_call_trend?selected_trend1=" + encodedSkill, function(error, json) {
        var trendData = json;
        console.log(trendData)
        draw_line_graph(trendData);
   });  
  });
}

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

  var margin = {top: 30, right: 20, bottom: 25, left: 40},
    width = 1000 - margin.left - margin.right,
    height = 600 - margin.top - margin.bottom;

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
        // debugger;
        var x0 = x.invert(d3.mouse(this)[0]);
        console.log("x" + x0)
        var bisectDate = d3.bisector(function (d) {
          return d.date;
        }).left;

                    
        var i = bisectDate(d.values, x0, 1),
          entry0 = d.values[i - 1],
          entry1 = d.values[i],
          y = x0 - entry0.date > entry1.date - x0 ? entry1.percent : entry0.percent;
          console.log("y" + y);
        div.transition()
          .duration(500)
          .style("opacity", 1);
        div.html("<br>" + d.key + "<br>" + y + "%")
          .attr('id', 'checking')
          .style("left", (d3.event.pageX) + "px")
          .style("top", (d3.event.pageY) + "px");
          })
  
      .on("mouseout", function(){
        div.transition()
        .duration(2000)
        .style("opacity", 0);
      })
  
  var legendName = d.key;
  var legendColor = d.color 
  var legendContainer = $('#trends_legend');
  var newLegendText = $('<div class="legend-text">' + legendName + '</div>');
  var newLegendColor = $('<div class="legend-box" style="background-color:'+ legendColor + '"></div>');
  legendContainer.append(newLegendText, newLegendColor); 

  });

var curtain = svg.append('rect')
    .attr('x', -1 * width)
    .attr('y', -1 * height)
    .attr('height', height)
    .attr('width', width)
    .attr('class', 'curtain')
    .attr('transform', 'rotate(180)')
    .style('fill', '#ffffff')

  /* Optionally add a guideline */
  var guideline = svg.append('line')
    .attr('stroke', '#333')
    .attr('stroke-width', 0)
    .attr('class', 'guide')
    .attr('x1', 1)
    .attr('y1', 1)
    .attr('x2', 1)
    .attr('y2', height)
  var t = svg.transition()
    .delay(750)
    .duration(3000)
    .ease('linear')
    .each('end', function() {
      d3.select('line.guide')
        .transition()
        .style('opacity', 0)
        .remove()
    });

  /* Create a shared transition for anything we're animating */
  t.select('rect.curtain')
    .attr('width', 0);
  t.select('line.guide')
    .attr('transform', 'translate(' + width + ', 0)')
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
