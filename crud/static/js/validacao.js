function validar(){
var area = document.getElementById("area").value;
var ideia = document.getElementById("ideia").value;
var tipo = document.getElementById("tipo").value;
var erro = false;
if(area === "" ){
	document.getElementById("area").style.backgroundColor="#ff4040";
	erro=true;
}else{
	if(ideia ===""){
		document.getElementById("ideia").style.backgroundColor="#ff4040";
		erro=true;
	} else {
		if(tipo === ""){
	document.getElementById("tipo").style.backgroundColor="#ff4040";
	erro=true;
		}
	}
}



if(erro==true){
	alert("Preencha os campos destacados");
}

}
function mudarcor(campo){

	document.getElementById(campo).style.backgroundColor="white";
}