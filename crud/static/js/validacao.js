function validar_ideia(){
var area = document.getElementById("area").value;
var ideia_para = document.getElementById("ideia_para").value;
var tipo = document.getElementById("tipo").value;
var ideia = document.getElementById("ideia").value;

var erro = false;
if(area === "1"){
	document.getElementById("area").style.boxShadow="1px 1px 1px 1px #ff4040";
	document.getElementById("area").style.color="#ff4040";
	erro=true;
}
if(ideia_para === "1"){
		
		document.getElementById("ideia_para").style.color="#ff4040";
		document.getElementById("ideia_para").style.boxShadow="1px 1px 1px 1px #ff4040";
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

}

function mudarcor(campo){

	document.getElementById(campo).style.boxShadow="0px 0px 0px 0px";
	document.getElementById(campo).style.color="black";

}

function validar_registro(){
	var nome = document.getElementById("r_nome").value;
	var empresa = document.getElementById("r_empresa").value;
	var cep = document.getElementById("r_cep").value;
	var endereco = document.getElementById("r_endereco").value;
	var telefone = document.getElementById("r_telefone").value;
	var email = document.getElementById("r_email").value;
	var passworrd = document.getElementById("r_password").value;
	var erro = false;

	if(nome === ""){
		document.getElementById("r_nome").style.boxShadow="1px 1px 1px 1px #ff4040";
		document.getElementById("r_nome").style.color="#ff4040";
		erro=true;
	}
	if(empresa === ""){
		document.getElementById("r_empresa").style.boxShadow="1px 1px 1px 1px #ff4040";
		document.getElementById("r_empresa").style.color="#ff4040";
		erro=true;
	}
	if(cep === ""){
		document.getElementById("r_cep").style.boxShadow="1px 1px 1px 1px #ff4040";
		document.getElementById("r_cep").style.color="#ff4040";
		erro=true;
	}
	if(endereco === ""){
		document.getElementById("r_endereco").style.boxShadow="1px 1px 1px 1px #ff4040";
		document.getElementById("r_endereco").style.color="#ff4040";
		erro=true;
	}
	if(telefone === ""){
		document.getElementById("r_telefone").style.boxShadow="1px 1px 1px 1px #ff4040";
		document.getElementById("r_telefone").style.color="#ff4040";
		erro=true;
	}
	if(email === ""){
		document.getElementById("r_email").style.boxShadow="1px 1px 1px 1px #ff4040";
		document.getElementById("r_email").style.color="#ff4040";
		erro=true;
	}
	if(passworrd === ""){
		document.getElementById("r_password").style.boxShadow="1px 1px 1px 1px #ff4040";
		document.getElementById("r_password").style.color="#ff4040";
		erro=true;
	}
	if(erro==true){
	alert("Preencha os campos destacados");
}
}