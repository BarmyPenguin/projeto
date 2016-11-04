function validar_ideia(){
var nomefun = document.getElementById("nomefun").value;
var area = document.getElementById("area").value;
var ideiapara = document.getElementById("ideiapara").value;
var tipo = document.getElementById("tipo").value;
var ideia = document.getElementById("ideia").value;
var erro = false;

if(nomefun === ""){
	document.getElementById("nomefun").style.boxShadow="1px 1px 1px 1px #ff4040";
	document.getElementById("nomefun").style.color="#ff4040";
	erro=true;
}
if(area === "1"){
	document.getElementById("area").style.boxShadow="1px 1px 1px 1px #ff4040";
	document.getElementById("area").style.color="#ff4040";
	erro=true;
}
if(ideiapara === "1"){
		
		document.getElementById("ideiapara").style.color="#ff4040";
		document.getElementById("ideiapara").style.boxShadow="1px 1px 1px 1px #ff4040";
		erro=true;
}
if(tipo === "1"){
	document.getElementById("tipo").style.boxShadow="1px 1px 1px 1px #ff4040";
	document.getElementById("tipo").style.color="#ff4040";
	erro=true;
		
}
if(ideia === ""){
	document.getElementById("ideia").style.boxShadow="1px 1px 1px 1px #ff4040";
	document.getElementById("ideia").style.color="#ff4040";
	erro=true;
}

if(erro==true){
	alert("Preencha os campos destacados");
}
else{
	document.getElementById("telaPrincipal").submit();
}

}

function mudarcor(campo){

	document.getElementById(campo).style.boxShadow="0px 0px 0px 0px";
	document.getElementById(campo).style.color="black";

}

function validar_registro(){
	var nome = document.getElementById("nome").value;
	var empresa = document.getElementById("empresa").value;
	var cep = document.getElementById("cep").value;
	var endereco = document.getElementById("endereco").value;
	var telefone = document.getElementById("telefone").value;
	var email = document.getElementById("email").value;
	var password = document.getElementById("password").value;
	var erro = false;

	if(nome === ""){
		document.getElementById("nome").style.boxShadow="1px 1px 1px 1px #ff4040";
		document.getElementById("nome").style.color="#ff4040";
		erro=true;
	}
	if(empresa === ""){
		document.getElementById("empresa").style.boxShadow="1px 1px 1px 1px #ff4040";
		document.getElementById("empresa").style.color="#ff4040";
		erro=true;
	}
	if(cep === ""){
		document.getElementById("cep").style.boxShadow="1px 1px 1px 1px #ff4040";
		document.getElementById("cep").style.color="#ff4040";
		erro=true;
	}
	if(endereco === ""){
		document.getElementById("endereco").style.boxShadow="1px 1px 1px 1px #ff4040";
		document.getElementById("endereco").style.color="#ff4040";
		erro=true;
	}
	if(telefone === ""){
		document.getElementById("telefone").style.boxShadow="1px 1px 1px 1px #ff4040";
		document.getElementById("telefone").style.color="#ff4040";
		erro=true;
	}
	if(email === ""){
		document.getElementById("email").style.boxShadow="1px 1px 1px 1px #ff4040";
		document.getElementById("email").style.color="#ff4040";
		erro=true;
	}
	if(password === ""){
		document.getElementById("password").style.boxShadow="1px 1px 1px 1px #ff4040";
		document.getElementById("password").style.color="#ff4040";
		erro=true;
	}
	if(erro==true){
	alert("Preencha os campos destacados");
	}
	else{
	document.getElementById("registro").submit();
	}
}