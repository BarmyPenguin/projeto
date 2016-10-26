var gbWS = "https://viacep.com.br/ws/";
var end = "/json";
var skey = "";

$( init );

function init() {
// Register listeners
$('#gbook').click( findBook );
}

function findBook() {
	findAll();
	return false;
}


function findAll() {
	console.log('findAll');
	surl = gbWS + $('#cep').val() + end;
	$.ajax({
		type: 'GET',
		url: surl,
		dataType: "json", // data type of response
		success: renderList
	});
}

function renderList(data) {
	
		 $('#logradouro').text(data.logradouro);
		 $('#complemento').text(data.complemento);
		 $('#bairro').text(data.bairro);
		 $('#cidade').text(data.localidade);
		 $('#estado').text(data.uf);
	}