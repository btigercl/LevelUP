

// $('#myTab a').click(function (e) {
//  	e.preventDefault();
// 	$(this).tab('show');
// })

// window.onload(){
// 	function onclick
// 	var name = clickevent
// 	change to active 
// 	toogle active = true to false...
// }

// event listner 



$('a[data-nexttab]').on('click', function () {
    var id = $(this).data('nexttab');
    $('.nav-tabs li:eq(' + id + ') a').tab('show');   
});