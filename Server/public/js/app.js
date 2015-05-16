function encode()
{

	var message = $('#input').val();
	$.get(
	    "/encode",
	    {m: message},
	    function(data) {
	       console.log('encode return: ', data);
	       $('#output').html(data.message);
	    }
	);
}

function decode()
{
	var message = $('#input').val();
	$.get(
	    "/decode",
	    {m: message},
	    function(data) {
	       console.log('decode return: ', data);
	       $('#output').html(data.message);
	    }
	);
}

function encodeTwilio()
{

	var message = $('#input').val();
	$.get(
	    "/encodesms",
	    {m: message},
	    function(data) {
	       console.log('encode return: ', data);
	       $('#output').html(data.message);
	    }
	);
}

function decodeTwilio()
{
	var message = $('#input').val();
	$.get(
	    "/decodesms",
	    {m: message},
	    function(data) {
	       console.log('decode return: ', data);
	       $('#output').html(data.message);
	    }
	);
}