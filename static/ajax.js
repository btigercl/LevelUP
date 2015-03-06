// function get_graph_data(evt){
//   evt.preventDefault();

//   var trend1= $( "select[name='selected_trend1']" ).val();
        
//   d3.json( "/db_call_trend?selected_trend1=" + trend1, function(error, json) {
//     var lineGraphdata = json;
    
//     visualizeLines(lineGraphdata);
//   });
// }
// $('#trend_button').on('click', get_graph_data);


// // Create line graph  
// function visualizeLines(ldata){

//     var margin = {top: 20, right: 20, bottom: 30, left: 50},
//         width = 960 - margin.left - margin.right,
//         height = 500 - margin.top - margin.bottom;

//     var parseDate = d3.time.format("%d-%m-%Y").parse;

//     var x = d3.time.scale()
//         .range([0, width]);

//     var y = d3.scale.linear()
//         .range([height, 0]);

//     var xAxis = d3.svg.axis()
//         .scale(x)
//         .orient("bottom");

//     var yAxis = d3.svg.axis()
//         .scale(y)
//         .orient("left");

//     var line = d3.svg.line()
//         .x(function(d) { return x(d.date); })
//         .y(function(d) { return y(d.percent); });

//     var svg = d3.select("#trends_results").append("svg")
//         .attr("width", width + margin.left + margin.right)
//         .attr("height", height + margin.top + margin.bottom)
//       .append("g")
//         .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

//     var linedata = parseData(ldata);

//     linedata.forEach(function(d) {
//         d.date = parseDate(d.date);
//     });

//       x.domain(d3.extent(linedata, function(d) { return d.date; }));
//       y.domain(d3.extent(linedata, function(d) { return d.percent; }));

//       svg.append("g")
//           .attr("class", "x axis")
//           .attr("transform", "translate(0," + height + ")")
//           .call(xAxis);

//       svg.append("g")
//           .attr("class", "y axis")
//           .call(yAxis)
//         .append("text")
//           .attr("transform", "rotate(-90)")
//           .attr("y", 6)
//           .attr("dy", ".71em")
//           .style("text-anchor", "end")
//           .text("Percent (%)");

//       svg.append("path")
//           .datum(linedata)
//           .attr("class", "line")
//           .attr("d", line);
// }


  <script type=text/javascript>
function updateGeo(evt){
  evt.preventDefault();

  $.post("/geographic_demand_skill",
        $('#geo_skill').serialize() {
        function(result){
        console.log(result):
          // for(var i = 0, i < result.length, i++) {
          //     tup = result[i];
          //     output = "Job Location": tup[0], "Latitude :" tup[1],  
        $("#geo_results").html(result); 
          }
        }

$('#geo_skill_button').on('click', updateGeo);

//   var vis = d3.select("#visualisation"),
//       WIDTH = 1000,
//       HEIGHT = 500,
//       MARGINS = {
//           top: 20,
//           right: 20,
//           bottom: 20,
//           left: 50
//       },

//     xScale = d3.time.scale().range([MARGINS.left, WIDTH - MARGINS.right]).domain([2008, 2014]);
//     yScale = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([0, 100]);

//     // x.domain(2008, 2014);
//     // y.domain(0, 50);

//     xAxis = d3.svg.axis()
//     .scale(xScale),
  
//     yAxis = d3.svg.axis()
//     .scale(yScale)
//     .orient("left");


//     vis.append("svg:g")
//     .attr("class","axis")
//     .attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")")
//     .call(xAxis);

//     vis.append("svg:g")
//     .attr("class", "y axis")
//     .attr("transform", "translate(" + (MARGINS.left) + ",0)")
//     .call(yAxis);

//     var lineGen = d3.svg.line()
//         .x(function(d) {
//           return xScale(d.year);
//         })
//         .y(function(d) {
//           return yScale(d.percent);
//         })
//         .interpolate("basis");

//     vis.append('svg:path')
//     .attr('d', lineGen(data1))
//     .attr('stroke', 'green')
//     .attr('stroke-width', 2)
//     .attr('fill', 'none');

//     vis.append('svg:path')
//     .attr('d', lineGen(data2))
//     .attr('stroke', 'blue')
//     .attr('stroke-width', 2)
//     .attr('fill', 'none');

//     vis.append('svg:path')
//     .attr('d', lineGen(data3))
//     .attr('stroke', 'yellow')
//     .attr('stroke-width', 2)
//     .attr('fill', 'none');
// }




//   var 
//     // Opera 8.0+, Firefox, Safari
//     ajaxRequest = new XMLHttpRequest();
//   } catch (e){
//     // Internet Explorer Browsers
//     try{
//       ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
//     } catch (e) {
//       try{
//         ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
//       } catch (e){
//         // Something went wrong
//         alert("Your browser broke!");
//         return false;
//       }
//     }
//   }
// }


  
// Create a function that will receive data sent from the server
// ajaxRequest.onreadystatechange = function(){
//   if(ajaxRequest.readyState == 4){
//     document.myForm.time.value = ajaxRequest.responseText;
//   }
// }



// var response = JSON.parse(httpRequest.responseText)


// function updatepage(str){
//     document.getElementById("geo_results").innerHTML = str


//     $(function() {
//       $('a#calculate').bind('click', function() {
//         $.getJSON('/_add_numbers', {
//           a: $('input[name="a"]').val(),
//           b: $('input[name="b"]').val()
//         }, function(data) {
//           $("#result").text(data.result);
//         });
//         return false;
//       });
//     });
//   </script>

      // (function() {
    // var httpRequest;
    // document.getElementById("geo_skill").onclick = function() {
    //  makeRequest('"/geographic_demand_skill"'); };
    //  try{



// $( document ).ready(function trends_graph() {  
// var margin = {top: 20, right: 20, bottom: 30, left: 50},
//     width = 960 - margin.left - margin.right,
//     height = 500 - margin.top - margin.bottom;

// var parseDate = d3.time.format("%y-%b-%d").parse;

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

//    data.d3.forEach(function(d) {
//         d][0] = parseDate(d.date);
//         d.close = +d.close;
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
//       .text("Precent (%)");

//   svg.append("path")
//       .datum(data)
//       .attr("class", "line")
//       .attr("d", line);
//     });
// }