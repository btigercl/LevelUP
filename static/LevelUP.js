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
// $(document).ready(loadCluster())

function loadCluster(){
  d3.json( "/skill_angelList_call?selected_skill=" + "python", function(error, json) {
  clusterData = json;
  visualizeCluster(clusterData);
  });  
}

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
    .attr("r", function(d) { return d.count/15})
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


//Bootstrap Javascript 
$('a[data-nexttab]').on('click', function () {
  var id = $(this).data('nexttab');
    $('.nav-tabs li:eq(' + id + ') a').tab('show');   
});
