// serie di funzioni per rendere visibili le varie opzioni in base ai checkbox selezionati
/* Dopo aver scelto il grado societario mette a disposizione la scelta del ruolo */
function cbCheck(){
	var elem = document.getElementById("sceltaRuolo");
	var grados1 = document.getElementById("amministratore");
	var grados2 = document.getElementById("dipendente");
	var ruolo1 = document.getElementById("mangerHide");
	var ruolo2 = document.getElementById("allenatHide");
if ((grados1.checked) || (grados2.checked)) {
	elem.style.display = "block";

	if (grados1.checked){
		ruolo1.style.display = "block";
		ruolo2.style.display = "none";		
		}

		else{
		ruolo2.style.display = "block";
		ruolo1.style.display = "none";
		}
	}
};
/* Dopo aver scelto il ruolo mette a disposizione la compilazione dei campi dati */
function cbCheck1(){
	var elem = document.getElementById("listaDati");
	var ruolo1 = document.getElementById("manager");
	var ruolo2 = document.getElementById("allenatore");

if ((ruolo1.checked) || (ruolo2.checked)) {
	elem.style.display = "block";

	}
};
function hideRuolo () {
     document.getElementById("sceltaRuolo").style.display = "none";
};

function hideDati () {
     document.getElementById("listaDati").style.display = "none";
};


/* Dopo aver scelto la categoria delle partite, mette a disposizione la compilazione dei campi dati */
function cbCheckPartite(){
	var elem = document.getElementById("listaDati");
	var ruolo1 = document.getElementById("piccoliAmici");
	var ruolo2 = document.getElementById("esordienti");
	var ruolo3 = document.getElementById("giovanissimi");

if ((ruolo1.checked) || (ruolo2.checked) || (ruolo3.checked)) {
	elem.style.display = "block";

	}
};

