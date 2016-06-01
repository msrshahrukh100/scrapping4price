$(function(){

console.log(document.getElementsByName('csrfmiddlewaretoken')[0].value);

$('#submit').click(function(){

var arr = {
		csrfmiddlewaretoken:document.getElementsByName('csrfmiddlewaretoken')[0].value,
		query : $('#query').val(),
};
var temp = {
	'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
};

$.ajax({
	url : '/app/scrap/',
	type: 'POST',
	dataType: 'json',
	async: false,
	headers: temp,
	data: JSON.stringify(arr),
    contentType: 'application/json; charset=utf-8', 
	success: function(data){
		// console.log(data['amazon']);

		for (i = 0; i<data['amazon']['models'].length - 1; i++)
			{	
				$('#items').append('<li><h3>' + data["amazon"]["models"][i] + '</h3><h5>'+data["amazon"]["price"][i]+'</h5></li>')
			}
	}

});


});

});



                // headers: temp,
                
                
