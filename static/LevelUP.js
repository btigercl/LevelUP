// Skill Set Tab 
//Calls skill set cluster graph when page loads
function loadCluster(){
  $.ajax({
    url: "/cookies"})
    .done(function(data, error){
      var jsonSkill = JSON.parse(data);
      var skill = jsonSkill.skill;
      console.log(skill);
      encodedSkill =  encodeURIComponent(skill)
      d3.json( "/skill_angelList_call?selected_skill=" + encodedSkill , function(error, json) {
        clusterData = json;
        visualizeCluster(clusterData);
    });  
  });
}

//Inserts name of graph into header div
function headerOnLoad(name){
    $.ajax({
    url: "/cookies"})
    .done(function(data, error){
      var jsonSkill = JSON.parse(data);
      var skill = jsonSkill.skill;
      $("#cluster_header").append("<h2>skill set graph for " + skill + "</h2>");
    });
}


// $(document).ready(loadCluster())


//Calls skill set cluster graph when drop down is used 
var clusterData;

function startCluster(evt){
  evt.preventDefault();
  $("#cluster_results").empty()
  var skillName= $( "select[name='selected_skill']" ).val();
  console.log(skillName)
  $("#cluster_header").empty()
  $("#cluster_header").append("<h1>skill set graph for " + skillName + "</h1>");
  var encodedSkill = encodeURIComponent(skillName);

  d3.json( "/skill_angelList_call?selected_skill=" + encodedSkill, function(error, json) {
    clusterData = json;
    visualizeCluster(clusterData);
  });  
}

$('#skill_cluster_button').on('click', startCluster);

//Skill Set D3 code that creates graph 

function visualizeCluster(datapassed){  

  //parses and binds data for nodes and links
  console.log(datapassed);
  var roleList = createRoletaglist(datapassed);
  var nodes = makeNodes(datapassed);
  var linkData = processDataIntoLinks(nodes);
                  

// var links = d3.layout().links(nodes);
// console.log(links);
                 
  var width = 1000,
    height = 600,
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
  
  //add tooltip div to SVG     
  var div = d3.select("#cluster_results").append("div")   
    .attr("class", "tooltip")               
    .style("opacity", 0);

  // adds the links
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

  //This is the animation and movement of the graph  
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
  
  //Allows user to click on a node and create a new graph based on skill node clicked on
  function click() {
    if (d3.event.defaultPrevented) return;
    $("#cluster_header").empty()
    var d = d3.select(this).node().__data__;
    var tagDisplayname = d.name;
    $("#cluster_header").append("<h1>skill set graph for " + d.name + "</h1>");
    encodedNodeskill = encodeURIComponent(tagDisplayname);
    d3.json( "/skill_angelList_call?selected_skill=" + encodedNodeskill, function(error, json) {
    newData = json;
    $("#cluster_results").empty();
    visualizeCluster(newData);
    });
  }
}
//Parses and formats data to create the nodes
function makeNodes(data){
  var nodes = [{name: data.name, weight: data.children.length}];
    _.each(data.children, function(item, index){
      nodes.push({name: item.name, count: item.count, weight: 1});
    });
  return nodes;
}

//Parses and formats data to create links
function processDataIntoLinks(nodes){
  var result = [];
  for (var index = 0; index < _.size(nodes); index++){
     result.push({ source: 0, target: index });
  }
  return result;
}

//This parses out the roletag information from the dictionary and inserts ranked list items into the DOM
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


//Bootstrap Javascript for tabs and tab animation
$('a[data-nexttab]').on('click', function () {
  var id = $(this).data('nexttab');
    $('.nav-tabs li:eq(' + id + ') a').tab('show');   
});