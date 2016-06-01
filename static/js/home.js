$(function(){
var x = '{% url "scraper" %}';
console.log(document.getElementsByName('csrfmiddlewaretoken')[0].value);
console.log(x);
var arr = {
		csrfmiddlewaretoken:document.getElementsByName('csrfmiddlewaretoken')[0].value,
		query : $('#query').val(),
}

$('#submit').click(function(){


$.ajax({
	url : '{% url "home" %}',
	type: 'POST',
	dataType: 'json',
	async: false,
	data: JSON.stringify(arr),
    contentType: 'application/json; charset=utf-8', 
	success: function(data){

	}

});


});

});



                // headers: temp,
                
                
